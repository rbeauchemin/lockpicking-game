import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

x0, y0, r0 = 297, 223.5, 30


def _transform_x_y(x, y):
    theta = np.arctan((y - y0) / (x - x0))
    xnew = x0 + (r0 * np.cos(theta))
    ynew = y0 + (r0 * np.sin(theta))
    return theta, xnew, ynew


def pick_plot(guess, x_previous=[], y_previous=[]):
    def on_click(event):
        global pick_loc
        for handle in pick_loc:
            handle.remove()
        x, y = event.xdata, event.ydata
        theta, xnew, ynew = _transform_x_y(x, y)
        if x > x0:
            xup = xnew
            yup = ynew
            ang = theta

        elif x < x0:
            xup = x0 - (xnew - x0)
            yup = y0 - (ynew - y0)
            ang = theta + np.pi

        pick_loc = plt.plot([x0, xup], [y0, yup], 'k')
        on_click.xprev = xup
        on_click.yprev = yup
        on_click.guess = np.degrees(ang)
        fig.canvas.draw()
    fig, ax = plt.subplots()
    ax.set_xlim(0, 600)
    ax.set_ylim(400,0)
    chest = Image.open('chest.png')
    ax.imshow(chest)
    ax.axis('off')
    for i in range(len(x_previous)):
        plt.plot([x0, x_previous[i]], [y0, y_previous[i]], 'r')
        fig.canvas.draw()
    x = x_previous[-1] if len(x_previous) > 0 else 327.
    y = y_previous[-1] if len(y_previous) > 0 else 224.
    global pick_loc
    pick_loc = plt.plot([x0, x], [y0, y], 'k')
    fig.canvas.mpl_connect('button_press_event', on_click)
    plt.show(block=True)
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
    plt.show(block=True)
    