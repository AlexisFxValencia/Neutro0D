import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import time
import cinetique_lente as cl

class RealTimeGraphApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Graphique en Temps Réel")

        # Configuration de la figure Matplotlib
        self.figure = Figure(figsize=(6, 4), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.ax.set_title("Évolution en Temps Réel")
        self.ax.set_xlabel("Temps")
        self.ax.set_ylabel("Valeur")
        self.ax.set_yscale('log')
        self.ax.grid()

        # Initialisation des données
        self.x_data = []
        self.y_data = []

        # Création du Canvas Tkinter pour afficher le graphique
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Boutons de contrôle
        self.start_button = tk.Button(root, text="Démarrer", command=self.start)
        self.start_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.stop_button = tk.Button(root, text="Arrêter", command=self.stop)
        self.stop_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.running = False
        
        self.dt = 0.1
        self.core = cl.Core0D(dt = self.dt)
        self.nb_pas = int(1/self.dt)

    def update_graph(self):
        if self.running:
            # Mise à jour des données
            t = time.time() % 60  # Utilisation de l'heure en secondes pour simuler du temps réel
            self.x_data.append(t)
            #self.y_data.append(np.sin(t))  # Par exemple, une sinusoïde
            for i in range(self.nb_pas):
                self.core.take_one_step()
            self.y_data.append(self.core.alpha)
            #print(self.core.alpha)
            if len(self.x_data) > 100:  # Limite de données affichées
                self.x_data.pop(0)
                self.y_data.pop(0)

            # Mise à jour du graphique
            self.ax.clear()
            self.ax.plot(self.x_data, self.y_data, label="Signal")
            self.ax.set_title("Évolution en Temps Réel")
            self.ax.set_xlabel("Temps")
            self.ax.set_ylabel("Valeur")
            self.ax.set_yscale('log')
            self.ax.legend()
            self.ax.grid()
            self.canvas.draw()

            # Appeler cette méthode à nouveau après 100 ms
            self.root.after(100, self.update_graph)

    def start(self):
        if not self.running:
            self.running = True
            self.update_graph()

    def stop(self):
        self.running = False

# Lancer l'application
if __name__ == "__main__":
    root = tk.Tk()
    app = RealTimeGraphApp(root)
    root.mainloop()
