import numpy as np

file_name = 'acp_bandwidth_d_d.txt'
data_bandwidth_d_d = np.loadtxt( file_name ).T

file_name = 'acp_bandwidth_h_h.txt'
data_bandwidth_h_h = np.loadtxt( file_name ).T

file_name = 'acp_latency_d_d.txt'
data_latency_d_d = np.loadtxt( file_name ).T

file_name = 'acp_latency_h_h.txt'
data_latency_h_h = np.loadtxt( file_name ).T

factor_latency = data_latency_h_h[1] / data_latency_d_d[1]
factor_bandwidth = data_bandwidth_d_d[1] / data_bandwidth_h_h[1]