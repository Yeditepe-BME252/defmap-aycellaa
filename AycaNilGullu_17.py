import numpy as np
import matplotlib.pyplot as plt

def plotgrid(map_func, xlim=(-3, 3), ylim=(-3, 3), grid_size=21):
    """
    Plots a regular grid and its deformation by map_func.
    """
    x = np.linspace(xlim[0], xlim[1], grid_size)
    y = np.linspace(ylim[0], ylim[1], grid_size)
    X, Y = np.meshgrid(x, y)

    X_deformed, Y_deformed = map_func(X, Y)

    fig, ax = plt.subplots(figsize=(8, 8))

    for i in range(grid_size):
        ax.plot(X[i, :], Y[i, :], color='lightgrey', linewidth=1)
        ax.plot(X[:, i], Y[:, i], color='lightgrey', linewidth=1)

    for i in range(grid_size):
        ax.plot(X_deformed[i, :], Y_deformed[i, :], color='C0', linewidth=1)
        ax.plot(X_deformed[:, i], Y_deformed[:, i], color='C0', linewidth=1)

    ax.axhline(0, color='black', linewidth=1.2)
    ax.axvline(0, color='black', linewidth=1.2)

    ax.set_xticks(range(int(xlim[0]), int(xlim[1]) + 1))
    ax.set_yticks(range(int(ylim[0]), int(ylim[1]) + 1))
    ax.tick_params(axis='both', direction='inout', length=6)

    ax.set_xlabel(r'$a_1$', fontsize=13)
    ax.set_ylabel(r'$a_2$', fontsize=13, rotation=0, labelpad=12)

    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_aspect('equal')

    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    plt.show()