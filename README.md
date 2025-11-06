fig, ax = plt.subplots()
ax.set(xlim=(-15,15), ylim=(-15,15), xlabel="x", ylabel="y", title = 'Shapes')
ax.grid(linestyle="--", linewidth=0.5, color='.25', zorder=-10)
ax.spines[["top", "right"]].set_visible(False)