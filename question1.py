import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve


def plotIntersection(rng, func1, func2):
    # plotting the functions
    plt.title("Line graph")
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.plot(rng, func1(rng), color="red")
    plt.plot(rng, func2(rng), color="blue")

    diff = lambda x: func1(x) - func2(x)

    # adding points of intersection
    intersection_points = fsolve(diff, rng)
    for point in intersection_points:
        if np.math.isclose(func1(point), func2(point), abs_tol=0.1):
            plt.plot(point, func2(point), marker="o", markersize=10, markerfacecolor="green")
    plt.show()


if __name__ == '__main__':
    f = lambda x: np.cos(x)*x
    g = lambda x: np.log10(x)
    plotIntersection(np.linspace(0.00001, 15, 1000), f, g)
