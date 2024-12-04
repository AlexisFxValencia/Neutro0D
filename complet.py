import numpy as np


from datas import *

n = 100.0 #100 neutrons 
reactivity = 150 * 1e-5 #5 pcm
dt = 1e-3 #secs 
t_end = 150
N_points = (t_end - 0) / dt
N_points = int(N_points)
print(N_points)

c = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
#c = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
n_list = []

for i in range (N_points):
    dn = n * (reactivity - beta_tot)/l + np.dot(lamb, c)
    dn *= dt
    dc = (n/l) * beta 
    dc = dc - np.multiply(lamb, c)
    dc *= dt
    n += dn
    c += dc
    #print(n)
    #print(c)
    n_list.append(n)

import matplotlib.pyplot as plt

time = np.linspace(0, t_end, N_points)
plt.plot(time, n_list, label=f"Indice {0}")
plt.show()