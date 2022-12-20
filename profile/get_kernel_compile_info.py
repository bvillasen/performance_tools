import sys, os
import subprocess


def print_kernel_info( id, kernels, text, n_to_print=11 ):
  kernel_name = kernels[id]['name']  
  line_id = kernels[id]['line_id']
  print( f'\n#############################################')
  print( f'Kernel: {kernel_name}')
  lines_text = ''
  lines = text[line_id:line_id+n_to_print]
  for line in lines:
    start_indx = line.find("remark") + 6
    if start_indx < 0: continue
    end_indx = line.find('[-Rpass')
    if end_indx < 0: end_indx = len(line) 
    lines_text += line[start_indx:end_indx] + '\n'
  print( lines_text )


args = sys.argv[1:]
file_name = args[0]

print( f'Calling hipcc for file: {file_name} ')

cmd = f'hipcc -Rpass-analysis=kernel-resource-usage --amdgpu-target=gfx90a {file_name}'

p = subprocess.Popen(cmd, stderr=subprocess.PIPE, shell=True) 
(output, err) = p.communicate()
p_status = p.wait()
output = str(err)
lines = output.split("\\n")


kernels = {}
n_kernels = 0
for  line_id, line in enumerate(lines): 
  if line.find('Function Name') > 0:
    indx_start = line.find('Function Name') + 19
    indx_end = line.find('iii')
    kernel_name = line[indx_start:indx_end]
    kernels[n_kernels] = { 'name': kernel_name, 'line_id':line_id }
    n_kernels += 1


print( f'Kernel names: ')
for id in kernels :
  name = kernels[id]['name']
  print( f'id: {id}   name: {name}')    

ids =  input('Kernel id to get info: ').split(' ')
ids = [ int(id) for id in ids ]
for id in ids:
  print_kernel_info( id, kernels, lines )  