import sys, os

def find_keywords( text, keywords ):
  if keywords == []: return True
  found_one = False
  for keyword in keywords:
    if text.find( keyword ) >= 0: return True
  return False  

def find_kernel_names( text ):
  keywords = ['symbol']
  n_lines = len(text)
  kernel_lines =  [ line for line in text if find_keywords(line, keywords)  ]
  kernel_names = {} 
  for id,line in enumerate(kernel_lines):
    start_indx = line.find('Z') + 1
    end_indx   = line.find('ii')
    name = line[start_indx:end_indx]
    while name[0].isnumeric():
      name = name[1:] 
    kernel_names[id] = name 
    
  return kernel_names

def print_kernel_info( id, kernel_names, text, n_to_print=21 ):
  kernel_name = kernel_names[id]  
  print( f'\n#############################################')
  print( f'Searching for kernel: {kernel_name}')
  keywords = [ 'size' ]
  # keywords = []
  kernel_lines =  [ line_id for line_id in range(n_lines) if  text[line_id].find( kernel_name ) >= 0 and find_keywords(text[line_id], keywords)  ]
  for line_id in kernel_lines:
    print( f'\nLine: {line_id}')
    lines = text[line_id:line_id+n_to_print]
    lines_text = ''
    for line in lines: 
      lines_text += line
    print( lines_text )

args = sys.argv[1:]
file_name = args[0]
kernel_names = args[1:]

print( f'Loading file: {file_name}' ) 
file = open( file_name, 'r' )
text = file.readlines()
n_lines = len(text)

kernel_names = find_kernel_names( text )
print( f'Kernel names: ')
for id in kernel_names :
  name = kernel_names[id]
  print( f'id: {id}   name: {name}')

ids =  input('Kernel id to get info: ').split(' ')
ids = [ int(id) for id in ids ]
for id in ids:
  print_kernel_info( id, kernel_names, text)