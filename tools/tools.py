import sys, os
import numpy as np

n_total = 101
n_split = 10

n_per_level = np.zeros(n_split)
level_offset = np.zeros(n_split)

n_local = n_total // n_split
offset = 0
for i in range(n_split):
  n_per_level[i] = n_local
  if i < ( n_total % n_split ): n_per_level[i] += 1 
  level_offset[i] = offset
  offset += n_per_level[i]