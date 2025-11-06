import matplotlib.pyplot as plt

class Shape2dPlotter:
    def __init__(self, fig = None, ax = None):
        if fig is None or ax is None:
            fig, ax = plt.subplots()            
        self.fig = fig
        self.ax = ax
        self.ax.set(xlim=(-15,15), ylim=(-15,15), xlabel="x", ylabel="y", title = 'Shapes')
        self.ax.grid(linestyle="--", linewidth=0.5, color='.25', zorder=-10)
        self.ax.spines[["top", "right"]].set_visible(False)
       
        def add_plot(self):
            plt.show()
