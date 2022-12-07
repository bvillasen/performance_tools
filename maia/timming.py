import numpy as np



# copy active cells for update
##############################################################################

ngpu2 = np.array([[ 11.4317, 10.4104, 6.41437, 2.98903, 36.9867 ],
                  [ 14.2598, 12.9336, 6.41554, 3.47066, 37.0894 ]])

ngpu4 = np.array([[ 1.82066, 1.20276, 6.84095, 0.75617, 29.7252 ],
                  [ 7.11873, 7.32704, 6.84065, 1.74770, 28.9646 ],
                  [ 7.45189, 7.56951, 6.84087, 1.81904, 28.0917 ],
                  [ 10.4257, 8.63401, 6.84094, 2.23582, 30.6281 ]])


ngpu8 = np.array([[ 0.73198, 0.45950, 6.50904, 0.370256, 20.7900 ],
                  [ 1.03404, 0.72768, 6.50968, 0.424569, 20.6207 ],
                  [ 3.85225, 3.52753, 6.50901, 0.947858, 19.7183 ],
                  [ 6.01712, 5.28417, 6.51010, 1.318290, 21.3212 ],
                  [ 2.31092, 2.00163, 6.50870, 0.661112, 20.6438 ],
                  [ 4.85522, 4.54663, 6.50934, 1.119180, 20.7474 ],
                  [ 5.27625, 5.36863, 6.50864, 1.231950, 19.5455 ],
                  [ 2.25434, 2.47428, 6.50872, 0.648813, 21.0004 ]])


# ngpu2 = np.array([[ 19.738, 10.4119, 6.43414, 2.81392, 48.0603 ],
#                   [ 25.344, 13.0385, 6.43375, 3.27964, 48.4354 ]])

# ngpu4 = np.array([[ 2.38653, 1.19807, 8.64024, 0.73930, 39.1648 ],
#                   [ 13.1312, 7.34161, 8.63983, 1.64928, 37.5003 ],
#                   [ 13.8059, 7.56170, 8.64019, 1.71334, 38.4932 ],
#                   [ 17.6988, 8.66807, 8.64037, 2.08646, 40.0925 ]])

# ngpu8 = np.array([[ 0.94065, 0.46150, 6.19309, 0.361556, 24.644 ],
#                   [ 1.51709, 0.72796, 6.19297, 0.412463, 24.991 ],
#                   [ 3.85173, 2.46871, 6.19259, 0.615440, 25.346 ],
#                   [ 3.98351, 1.99779, 6.19275, 0.627986, 25.159 ],
#                   [ 6.93547, 3.50919, 6.19338, 0.883506, 23.954 ],
#                   [ 8.68361, 5.01080, 6.19263, 1.045670, 25.094 ],
#                   [ 10.6603, 5.29331, 6.19306, 1.231370, 25.481 ],
#                   [ 9.63276, 5.15465, 6.19295, 1.151260, 23.972 ]])


# ngpu2_nmpi2 = np.array([[ 25.4484, 10.4307, 6.45465, 2.82227, 55.4451 ],
#                         [ 32.7914, 13.0088, 6.45434, 3.27833, 56.3388 ]])

# ngpu4_nmpi4 = np.array([[ 3.04098, 1.19328, 8.64869, 0.74085, 44.1034 ],
#                         [ 16.0847, 7.90376, 8.64863, 1.64863, 42.5756 ],
#                         [ 16.1468, 8.41551, 8.64832, 1.71008, 43.3603 ],
#                         [ 22.4060, 9.06468, 8.64918, 2.08181, 44.5292 ]])

# ngpu8_nmpi8 = np.array([[ 1.13692, 0.70418, 6.03483, 0.362981, 27.4239 ],
#                         [ 1.87090, 1.00155, 6.03460, 0.413152, 27.3890 ],
#                         [ 4.78344, 2.46919, 6.03430, 0.618539, 27.2342 ],
#                         [ 4.96289, 1.99936, 6.03452, 0.626499, 27.4660 ],
#                         [ 8.43327, 3.51915, 6.03488, 0.886161, 26.3547 ],
#                         [ 10.7404, 5.00703, 6.03369, 1.048410, 27.3468 ],
#                         [ 13.1951, 5.28815, 6.03589, 1.236590, 27.6875 ],
#                         [ 11.7299, 5.09477, 6.03446, 1.155130, 26.2432 ]])                                                

##############################################################################

# ##############################################################################
# ngpu2_nmpi2 = np.array([[ 26.2890, 10.0748, 6.38542, 6.02176, 60.4014 ],
#                         [ 33.5898, 12.5855, 6.38482, 7.89230, 61.6191 ]])

# ngpu4_nmpi4 = np.array([[ 3.16335, 1.11789, 8.63988, 0.91287, 46.4237 ],
#                         [ 17.0581, 7.13653, 8.63983, 4.08282, 45.7161 ],
#                         [ 16.8594, 7.04464, 8.63922, 3.95636, 45.6142 ],
#                         [ 23.1870, 8.34008, 8.63992, 5.22291, 46.9103 ]])                        

# ngpu8_nmpi8 = np.array([[ 1.16892, 0.44258, 6.08092, 0.39283, 29.8054 ],
#                         [ 1.95202, 1.03612, 6.08105, 0.57698, 29.7108 ],
#                         [ 4.98322, 2.35227, 6.08164, 1.27819, 30.2668 ],
#                         [ 5.18314, 1.94297, 6.08029, 1.29165, 30.3020 ],
#                         [ 8.77221, 3.35270, 6.08136, 2.05769, 28.8746 ],
#                         [ 11.1657, 4.80327, 6.08059, 2.71110, 30.0542 ],
#                         [ 13.8344, 5.07165, 6.08216, 3.32461, 30.2141 ],
#                         [ 12.2321, 4.68283, 6.08027, 2.93923, 28.8069 ]])
# ##############################################################################


# # copy active cells for collision and update
# ##############################################################################

# ngpu2_nmpi2 = np.array([[ 26.1867, 10.1094, 6.38163, 7.95073, 62.3827 ],
#                         [ 33.349 , 12.5574, 6.38156, 10.1006, 63.8033 ]])

# ngpu4_nmpi4 = np.array([[ 3.09482, 1.1229 , 8.63656, 0.937116, 48.2549 ],
#                         [ 16.5193, 7.03955, 8.63643, 5.21119,  47.3296 ],
#                         [ 16.9693, 7.14543, 8.63652, 5.27692,  47.0802 ],
#                         [ 23.1055, 8.34332, 8.63648, 6.97915,  48.0357 ]])

# ngpu8_nmpi8 = np.array([[ 1.16817, 0.44144, 6.21936, 0.397404, 31.0292 ],
#                         [ 1.91758, 1.04412, 6.21902, 0.636646, 31.1293 ],
#                         [ 4.98773, 2.3523 , 6.21908, 1.56737 , 31.2801 ],
#                         [ 5.18071, 2.24443, 6.21902, 1.60687 , 31.5203 ],
#                         [ 8.78465, 3.36237, 6.21956, 2.80434 , 29.9808 ],
#                         [ 11.1077, 4.80449, 6.21862, 3.54183 , 31.3594 ],
#                         [ 13.8035, 5.04703, 6.21946, 4.30245 , 31.5398 ],
#                         [ 12.167 , 5.03812, 6.21922, 3.94154 , 30.1902 ]])                         
# ##############################################################################


milan_nmpi16 = np.array([[ 13.9778, 11.8846, 73.3852, 6.01181, 344.372 ],
                         [ 13.1126, 11.1514, 73.381 , 3.82096, 344.391 ],
                         [ 16.3681, 12.1091, 73.3846, 6.40629, 344.386 ],
                         [ 24.5623, 24.6727, 73.3799, 5.91657, 344.948 ],
                         [ 73.1537, 49.4348, 73.3852, 8.14585, 346.046 ],
                         [ 114.182, 66.8318, 73.3813, 20.5604, 346.614 ],
                         [ 104.825, 87.1173, 73.3858, 18.5292, 346.760 ],
                         [ 113.456, 104.172, 73.3805, 19.5245, 347.032 ],
                         [ 49.8927, 32.6314, 73.3853, 9.2796 , 345.258 ],
                         [ 25.5576, 21.8702, 73.3809, 6.17979, 344.793 ],
                         [ 53.9662, 37.2303, 73.3852, 10.7999, 345.436 ],
                         [ 92.7812, 98.4767, 73.3798, 17.1125, 346.808 ],
                         [ 108.416, 92.8713, 73.3855, 20.016 , 346.908 ],
                         [ 112.414, 59.6154, 73.3753, 18.8313, 346.541 ],
                         [ 54.6031, 49.1035, 73.3851, 7.88813, 345.971 ],
                         [ 49.3648, 31.3761, 73.3798, 7.29598, 345.211 ]])

milan_nmpi32 = np.array([[ 12.5642, 11.3198, 82.4229, 3.89196, 331.507 ],
                         [ 14.4216, 11.3985, 82.4219, 3.45346, 331.519 ],
                         [ 12.8183, 10.7701, 82.4235, 3.56169, 331.499 ],
                         [ 15.0026, 10.7569, 82.4229, 3.69446, 331.509 ],
                         [ 15.6010, 11.2280, 82.4234, 3.79807, 331.554 ],
                         [ 15.6557, 11.0984, 82.4227, 3.42350, 331.491 ],
                         [ 19.0102, 15.2222, 82.4240, 4.90780, 331.657 ],
                         [ 34.0587, 29.2328, 82.4228, 6.49744, 332.191 ],
                         [ 48.7881, 27.3011, 82.4235, 6.93507, 332.221 ],
                         [ 70.7704, 37.6700, 82.4221, 6.38987, 332.676 ],
                         [ 88.1861, 43.1500, 82.4240, 9.89577, 332.861 ],
                         [ 83.9231, 35.4132, 82.4318, 10.3887, 332.619 ],
                         [ 115.961, 78.8733, 82.4240, 14.1572, 333.496 ],
                         [ 82.0438, 36.5923, 82.4229, 9.40853, 332.606 ],
                         [ 130.834, 100.118, 82.4246, 16.1845, 333.908 ],
                         [ 87.4777, 43.4876, 82.4251, 9.55610, 332.929 ],
                         [ 79.9131, 41.1893, 82.4230, 10.2041, 332.770 ],
                         [ 45.2173, 37.6427, 82.4217, 6.56582, 332.614 ],
                         [ 47.5390, 40.7799, 82.4237, 8.71749, 332.577 ],
                         [ 16.9808, 12.9112, 82.4229, 4.32205, 331.592 ],
                         [ 52.9547, 40.2754, 82.4234, 7.42371, 332.739 ],
                         [ 76.7020, 36.6792, 82.4227, 8.97024, 332.604 ],
                         [ 85.9323, 42.7724, 82.4241, 8.34151, 332.882 ],
                         [ 128.136, 101.606, 82.4232, 16.9727, 333.957 ],                         
                         [ 85.3137, 41.1590, 82.4234, 10.7595, 332.805 ],
                         [ 115.267, 79.7998, 82.4223, 14.0508, 333.476 ],
                         [ 89.2821, 39.0052, 82.4240, 9.45762, 332.768 ],
                         [ 87.1501, 35.9756, 82.4233, 10.7682, 332.644 ],
                         [ 70.5809, 43.5515, 82.4238, 9.23311, 332.863 ],
                         [ 20.1672, 19.0170, 82.4226, 5.04552, 331.893 ],
                         [ 49.7539, 28.4083, 82.4241, 6.09346, 332.243 ],
                         [ 42.6896, 29.1828, 82.4251, 6.16080, 332.236 ]])

rome_nmpi16 = np.array([[ 11.3686, 10.7843, 74.6876, 1.81741, 352.058 ],
                        [ 11.0002, 10.0022, 74.6819, 1.35273, 352.052 ],
                        [ 12.8759, 11.0242, 74.6889, 1.55323, 352.057 ],
                        [ 20.3772, 25.5903, 74.6883, 3.09522, 352.694 ],
                        [ 61.8936, 53.6591, 74.6885, 7.75478, 353.944 ],
                        [ 91.5934, 69.9593, 74.6804, 17.3505, 354.536 ],
                        [ 108.392, 95.9136, 74.6887, 18.0024, 354.719 ],
                        [ 117.945, 115.981, 74.6895, 17.6468, 355.038 ],
                        [ 53.8782, 34.9255, 74.6873, 8.04629, 353.104 ],
                        [ 25.3025, 23.077 , 74.6805, 3.76003, 352.559 ],
                        [ 58.2994, 39.8724, 74.6891, 8.28389, 353.245 ],
                        [ 105.858, 110.124, 74.6886, 16.7127, 354.830 ],
                        [ 106.794, 102.739, 74.6887, 17.1916, 354.905 ],
                        [ 95.5274, 64.1723, 74.6807, 18.5501, 354.458 ],
                        [ 43.9448, 52.2991, 74.6884, 7.1073 , 353.828 ],
                        [ 42.5181, 33.643 , 74.689 , 5.29984, 353.010 ]])

# rome_nmpi16 = np.array([[ 13.5893, 12.0988, 74.6904, 6.05751, 343.669 ],
#                         [ 12.9084, 10.724 , 74.6849, 3.75492, 343.673 ],
#                         [ 15.6708, 12.0827, 74.6891, 6.41829, 343.709 ],
#                         [ 23.9434, 24.5506, 74.6831, 5.9203 , 344.238 ],
#                         [ 72.2551, 49.3018, 74.6891, 8.2881 , 345.373 ],
#                         [ 112.426, 66.3999, 74.6794, 20.5209, 345.924 ],
#                         [ 102.374, 87.5639, 74.6889, 17.9145, 346.081 ],
#                         [ 111.677, 104.308, 74.6839, 19.3403, 346.349 ],
#                         [ 49.1665, 32.6247, 74.6901, 9.50148, 344.581 ],
#                         [ 24.7303, 22.4938, 74.6849, 6.21195, 344.129 ],
#                         [ 52.5332, 37.3649, 74.689 , 10.721 , 344.769 ],
#                         [ 91.4763, 98.8931, 74.6832, 16.7533, 346.123 ],
#                         [ 105.519, 93.4902, 74.6892, 19.9009, 346.223 ],
#                         [ 111.906, 59.7082, 74.6816, 18.8132, 345.862 ],
#                         [ 54.3354, 49.1801, 74.6884, 8.36086, 345.272 ],
#                         [ 49.2129, 31.3506, 74.6829, 7.17926, 344.518 ]])










# ngpu2_nmpi8 = np.array([[4.6931 ,  20.0148, 7.01891,  0.233035],
#                         [7.10498,  20.8412, 7.01757,  0.438238],
#                         [18.7186,  27.5579, 7.01779,  1.66763 ],
#                         [24.2231,  29.7178, 7.01836,  2.44847 ],
#                         [21.6039,  19.6651, 7.01861,  1.33813 ],
#                         [31.1578,  20.6435, 7.01713,  2.21377 ],
#                         [30.8771,  20.6436, 7.01734,  2.44641 ],
#                         [19.972 ,  19.4813, 7.01636,  1.45329 ]])

# ngpu4_nmpi8 = np.array([[ 2.72821,  19.8636,  7.29208,  0.534927 ], 
#                         [ 2.2344 ,  19.4247,  7.29242,  0.254222 ], 
#                         [ 17.9514,  26.5021,  7.29343,  2.00921  ], 
#                         [ 22.4293,  28.8567,  7.2917 ,  2.71612  ],                         
#                         [ 10.3871,  22.4768,  7.29192,  1.209    ], 
#                         [ 14.7961,  26.8888,  7.29154,  2.16787  ], 
#                         [ 15.9011,  27.313 ,  7.29286,  2.74204  ], 
#                         [ 11.2486,  22.3842,  7.29102,  1.42334  ]]) 