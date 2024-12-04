
import numpy as np
from datas import *

n = 100.0 #100 neutrons 
reactivity = 50 * 1e-5 #5 pcm c
reactivity = 0.0
dt = 1e-5 #secs 
t_end = 5.0
N_points = (t_end - 0) / dt
N_points = int(N_points)


def f(x):
    sum = 0
    for i in range(beta.size):
        sum += beta[i]/(lamb[i] + x)
        
    return x * (l + sum)    

import matplotlib.pyplot as plt

N = 100000
x = np.linspace(-1000, 10, N)
y = f(x)
plt.plot(x, y, label=f"Indice {0}")
plt.ylim([-0.005, 0.005])
#plt.xscale('log')
plt.show()
