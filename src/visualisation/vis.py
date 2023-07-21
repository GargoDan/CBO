from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

import matplotlib.pyplot as plt
import imageio
import numpy as np

def plot_1d(function, points, file_path=False):
    # plot 1d function

    plt.ion()
    fig = plt.figure(figsize=(3, 2), dpi=300)
    ax = fig.add_subplot(111)
    plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)
    params = {'legend.fontsize': 3,
                'legend.handlelength': 3}
    plt.rcParams.update(params)

    ax.set_xlim(-100, 500)
    ax.set_ylim(-10, 22)
    
    # lower the size of the axis ticks
    ax.tick_params(axis='both', which='major', labelsize=3)
    

    # input (x, y) and output (z) nodes of cost-function graph
    function_x = np.linspace(-100, 500, 10000)
    function_y = function(function_x)

    # plot cost-function graph
    ax.plot(function_x, function_y, color='blue', linewidth=0.5)

    # plot starting points
    ax.scatter(points, function(points), color='red', marker='o', s=1)

    if file_path:
        # save image to file 
        plt.savefig(file_path, bbox_inches='tight', pad_inches=0)

        # do not display image
        plt.close()
    else:
        plt.show()

def plot_2d(function, history):
    # plot Ackley function in 2D with CBO optimization path and colorbar
    plt.ion()
    fig = plt.figure(figsize=(3, 2), dpi=300)
    ax = fig.add_subplot(111)
    plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)
    params = {'legend.fontsize': 3,
                'legend.handlelength': 3}
    plt.rcParams.update(params)

    ax.set_xlim(-7, 7)
    ax.set_ylim(-7, 7)

    # input (x, y) and output (z) nodes of cost-function graph
    function_x = np.linspace(-7, 7, 100)
    function_y = np.linspace(-7, 7, 100)

    x_mesh, y_mesh = np.meshgrid(function_x, function_y)
    z_mesh = function((x_mesh, y_mesh))

    # plot initial point
    ax.scatter(history[0][0], history[0][1], color='black', marker='o', s=10)

    # plot sgf optimization path
    ax.plot([el[0] for el in history], [el[1] for el in history], color='black', marker='x', linewidth=0.5,
            markersize=1)
    
    # plot cost-function graph
    ax.contourf(x_mesh, y_mesh, z_mesh, cmap=cm.coolwarm, alpha=.4)

    # plot final point
    ax.scatter(history[-1][0], history[-1][1], color='black', marker='o', s=10)


def save_gif(history, function, file_path, step=10):
    for i in range(0, len(history), step):
        plot_1d(function, history[i], file_path='./images/1d_function_{}1.png'.format(i))

        images = []
    for i in range(0, len(history), step):
        filename = f'./images/1d_function_{i}1.png'
        images.append(imageio.imread(filename))

    for _ in range(10):
        images.append(imageio.imread(filename))

    imageio.mimsave(file_path, images, duration=0.1)
