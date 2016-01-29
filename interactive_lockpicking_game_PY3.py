import numpy
import matplotlib
from matplotlib import pylab, mlab, pyplot
from IPython.core.pylabtools import figsize, getfigs
from pylab import *
from numpy import *
import sys
import cStringIO
from PIL import Image
np = numpy
plt = pyplot
ioff()

print('You come across a dark cellar room and spot a chest with a lock in the corner')
yorn = input('Will you attempt to pick the lock? [y]/n: ') or 'y'
if yorn == 'y':
    x_previous=[]
    y_previous=[]
    def on_click(event):
        x, y = event.xdata, event.ydata
        x0, y0 = 297, 223.5
        r0 = 30
        theta = np.arctan((y-y0)/(x-x0))
        xnew = x0 + (r0 * np.cos(theta))
        ynew = y0 + (r0 * np.sin(theta))
        if x > x0:    
            plt.plot([x0,xnew],[y0,ynew],'k')
            on_click.xprev = xnew
            on_click.yprev = ynew
            on_click.guess = np.degrees(theta)
        elif x < x0:
            on_click.xprev = x0 - (xnew - x0)
            on_click.yprev = y0 - (ynew - y0)
            plt.plot([x0,x0 - (xnew - x0)],[y0,y0 - (ynew - y0)],'k')
            on_click.guess = np.degrees(theta+np.pi)
        fig.canvas.draw()
    correct_guess = randint(-90,270)
    print('You know that if you can apply leverage at the correct angle, the lock will free.')
    lockpicks = 5
    print('You have {0} lockpicks, and one will break if you force it too hard in the wrong direction.'.format(lockpicks))
    damage = 0
    guess = 0
    finished = 'n'
    x0, y0 = 297, 223.5
    while lockpicks != 0 and finished == 'n':
        print('Choose an angle with the mouse')
        fig, ax = plt.subplots()
        ax.set_xlim(0, 600)
        ax.set_ylim(400,0)
        chest = Image.open('chest.png')
        ax.imshow(chest)
        ax.axis('off')
        for i in range(len(x_previous)):
            plt.plot([x0,x_previous[i]],[y0,y_previous[i]],'r')
            fig.canvas.draw()
        fig.canvas.mpl_connect('button_press_event', on_click)
        show()
        guess = on_click.guess
        x_previous.append(on_click.xprev)
        y_previous.append(on_click.yprev)
        print(guess)
        force = int(input('Choose the force applied (1-5): '))
        
        if abs(correct_guess-guess) < 3:
            angle = 'correct'
        elif abs(correct_guess-guess) < 15 and abs(correct_guess-guess) >= 3:
            angle = 'close'
        elif abs(correct_guess-guess) < 30 and abs(correct_guess-guess) >= 15:
            angle = 'nearlyclose'
        elif abs(correct_guess-guess) < 60 and abs(correct_guess-guess) >= 30:
            angle = 'far'
        else:
            angle = 'realfar'
            
        if angle == 'correct':
            if force == 5:
                print('*Click*')
                print('The lock falls to the floor and the chest opens to reveal gold strewn with shining sapphires and rubies.')
                fig, ax = plt.subplots()
                treasure = Image.open('treasure.png')
                ax.imshow(treasure)
                ax.axis('off')
                finished = 'y'
                show()
            elif force < 5:
                print('The pick is pushed with no resistance.')
                
        elif angle == 'close':
            if force == 5:
                lockpicks -= 1
                print('The pick breaks. You now have {0} lockpicks.'.format(lockpicks))
                damage = 0
            elif force == 4:
                damage += 1
                if damage == 3:
                    lockpicks -= 1
                    print('The pick feels resistance and snaps from repeated stress. You now have {0} lockpicks.'.format(lockpicks))
                else:
                    print('The pick feels resistance.')
            else:
                print('The pick is pushed with no resistance.')
        elif angle == 'nearlyclose':
            if force >= 4:
                lockpicks -= 1
                print('The pick breaks. You now have {0} lockpicks.'.format(lockpicks))
                damage = 0
            elif force == 3:
                damage += 1
                if damage == 3:
                    lockpicks -= 1
                    print('The pick feels resistance and snaps from repeated stress. You now have {0} lockpicks.'.format(lockpicks))
                else:
                    print('The pick feels resistance.')
            else:
                print('The pick is pushed with no resistance.')
                
        elif angle == 'far':
            if force >= 3:
                lockpicks -= 1
                print('The pick breaks. You now have {0} lockpicks.'.format(lockpicks))
                damage = 0
            elif force == 2:
                damage += 1
                if damage == 3:
                    lockpicks -= 1
                    print('The pick feels resistance and snaps from repeated stress. You now have {0} lockpicks.'.format(lockpicks))
                else:
                    print('The pick feels resistance.')
            else:
                print('The pick is pushed with no resistance.')
                    
        elif angle == 'realfar':
            if force >= 2:
                lockpicks -= 1
                print('The pick breaks. You now have {0} lockpicks.'.format(lockpicks))
                damage = 0
            else:
                damage += 1
                if damage == 3:
                    lockpicks -= 1
                    print('The pick feels resistance and snaps from repeated stress. You now have {0} lockpicks.'.format(lockpicks))
                else:
                    print('The pick feels resistance.')
    if lockpicks == 0:
        print('You\'re all out of picks. You\'ll have to leave this treasure for a more skilled treasure hunter.')
