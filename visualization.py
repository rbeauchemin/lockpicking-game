import numpy
from matplotlib import pyplot
# from IPython.core.pylabtools import figsize, getfigs
from pylab import *
from numpy import *
from PIL import Image
np = numpy
plt = pyplot
ioff()

x0, y0 = 297, 223.5

def pick_plot(guess, x_previous=[], y_previous=[]):
    def on_click(event):
        x, y = event.xdata, event.ydata
        r0 = 30
        theta = np.arctan((y - y0) / (x - x0))
        xnew = x0 + (r0 * np.cos(theta))
        ynew = y0 + (r0 * np.sin(theta))
        if x > x0:
            plt.plot([x0, xnew], [y0, ynew], 'k')
            on_click.xprev = xnew
            on_click.yprev = ynew
            on_click.guess = np.degrees(theta)
        elif x < x0:
            on_click.xprev = x0 - (xnew - x0)
            on_click.yprev = y0 - (ynew - y0)
            plt.plot([x0, x0 - (xnew - x0)], [y0, y0 - (ynew - y0)], 'k')
            on_click.guess = np.degrees(theta + np.pi)
        fig.canvas.draw()
    print('Choose an angle with the mouse')
    fig, ax = plt.subplots()
    ax.set_xlim(0, 600)
    ax.set_ylim(400,0)
    chest = Image.open('chest.png')
    ax.imshow(chest)
    ax.axis('off')
    for i in range(len(x_previous)):
        plt.plot([x0, x_previous[i]], [y0, y_previous[i]], 'r')
        fig.canvas.draw()
    fig.canvas.mpl_connect('button_press_event', on_click)
    show(block=True)
    if hasattr(on_click, 'guess'):
        guess = on_click.guess
        x_previous.append(on_click.xprev)
        y_previous.append(on_click.yprev)
    return guess, x_previous, y_previous


def treasure_plot():
    fig, ax = plt.subplots()
    treasure = Image.open('treasure.png')
    ax.imshow(treasure)
    ax.axis('off')
    show(block=True)
    