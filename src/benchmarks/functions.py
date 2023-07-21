import numpy as np


def example_f(x):
    """
    Sinusoidal function with multiple local minima and one global minimum.
    """
    sinusoid_part = np.sin(x) + 20
    # Heaviside step function
    drop_part1 = -9.5 * (np.sign(x + 2) + np.sign(1 - x))
    drop_part2 = -4 * (np.sign(x + 5.2) + np.sign(-5 - x))

    return sinusoid_part + drop_part1


def example_f2(x):
    """
    Sinusoidal function with multiple local minima and one global minimum.
    """
    sinusoid_part = np.sin(x) + 20
    # Heaviside step function
    drop_part1 = -9.5 * (np.sign(x + 2) + np.sign(1 - x))
    drop_part2 = 5 * (np.sign(x - 152) + np.sign(150 - x))

    return sinusoid_part + drop_part1 + drop_part2

def ackley(xs, a=20, b=0.2, c=2*np.pi):
    x, y = xs[0], xs[1]
    return -a * np.exp(-0.2 * np.sqrt(0.5 * (x**2 + y**2))) - np.exp(0.5 * (np.cos(2 * np.pi * x) + np.cos(2 * np.pi * y))) + a + np.exp(1)
    
def Rastrigin(x):
    return 10 * 2 + np.sum(x**2 - 10 * np.cos(2 * np.pi * x), axis=1)