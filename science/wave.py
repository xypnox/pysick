import numpy as np
import matplotlib.pyplot as plt
import sympy as sm
from sympy.plotting import plot
from sympy.core.sympify import SympifyError

t = sm.Symbol('t')
x = sm.Symbol('x')
v = sm.Symbol('v')


class wave():
    """docstring for """
    def __init__(self, fn):
        self.fn = sm.sympify(fn)

    def plot(self):
        p = plot(self.fn, legend=True, show=False)
        p[0].line_color = 'r'
        p.show()

    def disp(self):
        pass


def show_shape(patch, snatch):
    ax = plt.gca()
    ax.add_patch(snatch)
    ax.add_patch(patch)
    ax.set_aspect('equal')
    plt.axis('scaled')
    plt.show()

xd = wave('x**2')
xd.plot()
c = plt.Circle((0, 0), radius=0.5)
g = plt.Circle((0.2, 0.3), radius=0.4)
show_shape(c, g)
