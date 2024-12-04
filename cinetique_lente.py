from datas import *
import numpy as np

class Core0D: 
    def __init__(self, dt = 0.1, t_end = 25.0, reactivity = 150): 
        self.dt = dt #secs 
        self.t_end = t_end
        self.reactivity = reactivity * 1e-5 #5 pcm
        self.n = 100.0 #100 neutrons 
        self.c = np.array([100.0, 100.0, 100.0, 100.0, 100.0, 100.0])
        #self.c = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
        self.N_points = (self.t_end - 0) / self.dt
        self.N_points = int(self.N_points)
        self.n_list = []
        self.alpha_list = []

    def simulate(self):
        for i in range (self.N_points):
            self.take_one_step()
    
    def take_one_step(self):
        self.alpha = self.compute_alpha()
        dc = self.compute_delta_concentration()
        self.c += dc
        self.alpha_list.append(self.alpha)
        
    def compute_alpha(self):
        return np.dot(lamb, self.c) / (beta_tot - self.reactivity)
        #print(alpha)
        
    def compute_delta_concentration(self):
        dc = beta * self.alpha  - np.multiply(lamb, self.c)
        dc *= self.dt
        return dc
  
    def change_reactivity(self, reactivity):
        self.reactivity = reactivity * 1e-5

    def plot(self):
        import matplotlib.pyplot as plt
        time = np.linspace(0, self.t_end, self.N_points)
        # plt.plot(time, n_list, label=f"Indice {0}")
        plt.plot(time, self.alpha_list, label=f"Indice {0}")
        plt.yscale('log')
        plt.show()


if __name__=="__main__":
    core = Core0D()
    core.simulate()
    core.plot()