import random
import visualization as vis

class Adventurer:
    def __init__(self):
        self.inventory = {'gold': random.randint(20,40),
                          'picks': random.randint(3,6),
                          'sapphires': 0,
                          'rubies': 0}
        self.interactive = True

    def get_inv_count(self, item):
        return self.inventory[item] if item in self.inventory else 0
    
    def alter_inv_count(self, item, alteration):
        if item not in self.inventory:
            self.inventory[item] = 0
        if self.get_inv_count(item) + alteration >= 0:
            self.inventory[item] = self.get_inv_count(item) + alteration
        return self.inventory[item]

    def set_inv_count(self, item, num):
        self.inventory[item] = num


class LockPicking(Adventurer):
    def __init__(self):
        super().__init__()
        self.pick_strain = 0
        self.picks = super().get_inv_count('picks')
    
    def _pick_breaks(self, from_repeat=False):
        self.picks -= 1
        self.pick_strain = 0
        if from_repeat:
            print('The pick feels resistance and snaps from repeated stress. You now have {0} picks.'.format(self.picks))
        else:
            print('The pick breaks. You now have {0} picks.'.format(self.picks))

    def lockpicking_sequence(self):
        print('You come across a dark cellar room and spot a chest with a lock in the corner.')
        print('You know that if you can apply leverage at the correct degree, the lock will free.')
        print('You have {0} picks, and one will break if you force it too hard at the wrong angle.'.format(self.picks))
        yorn = input('Will you attempt to pick the lock? [y]/n: ') or 'y'
        if yorn.lower()[0] == 'n':
            print('Not this time... You decide to continue on.')
        if yorn.lower()[0] == 'y':
            correct_guess = random.randint(-90,270) if self.interactive else random.randint(-180,180)
            self.pick_strain = 0
            guess, x_previous, y_previous = 0, [], []
            if self.interactive:
                print('Interactive Hints:\n'
                      'Choose an angle by clicking on the chest.\n'
                      'Red Angles represent previous attempts.\n'
                      'Close the plot to move on to force selection.\n'
                      'Close the plot without selecting to reuse your last guess.')
            while self.picks != 0:
                if self.interactive:
                    guess, x_previous, y_previous = vis.pick_plot(guess, x_previous, y_previous)
                else:
                    guess = input('Choose an angle (integer between -180 and 180) [previous]: ') or guess
                force = int(input('Choose the force applied (1-5): '))
                guess = int(guess)
                
                if abs(correct_guess - guess) < 3:
                    angle = 'correct'
                elif abs(correct_guess - guess) < 15 and abs(correct_guess - guess) >= 3:
                    angle = 'close'
                elif abs(correct_guess - guess) < 30 and abs(correct_guess - guess) >= 15:
                    angle = 'nearlyclose'
                elif abs(correct_guess - guess) < 60 and abs(correct_guess - guess) >= 30:
                    angle = 'far'
                else:
                    angle = 'realfar'
                    
                if angle == 'correct':
                    if force == 5:
                        print('*Click*')
                        print('The lock falls to the floor and the chest opens to reveal gold strewn with shining sapphires and rubies.')
                        super().alter_inv_count('gold', random.randint(10,20))
                        super().alter_inv_count('sapphires', random.randint(1,2))
                        super().alter_inv_count('rubies', random.randint(1,2))
                        vis.treasure_plot()
                        break
                    elif force < 5:
                        print('The pick is pushed with no resistance.')
                        
                elif angle == 'close':
                    if force == 5:
                        self._pick_breaks()
                    elif force == 4:
                        self.pick_strain += 1
                        if self.pick_strain == 3:
                            self._pick_breaks(from_repeat=True)
                        else:
                            print('The pick feels resistance.')
                    else:
                        print('The pick is pushed with no resistance.')
                elif angle == 'nearlyclose':
                    if force >= 4:
                        self._pick_breaks()
                    elif force == 3:
                        self.pick_strain += 1
                        if self.pick_strain == 3:
                            self._pick_breaks(from_repeat=True)
                        else:
                            print('The pick feels resistance.')
                    else:
                        print('The pick is pushed with no resistance.')
                        
                elif angle == 'far':
                    if force >= 3:
                        self._pick_breaks()
                    elif force == 2:
                        self.pick_strain += 1
                        if self.pick_strain == 3:
                            self._pick_breaks(from_repeat=True)
                        else:
                            print('The pick feels resistance.')
                    else:
                        print('The pick is pushed with no resistance.')
                            
                elif angle == 'realfar':
                    if force >= 2:
                        self._pick_breaks()
                    else:
                        self.pick_strain += 1
                        if self.pick_strain == 3:
                            self._pick_breaks(from_repeat=True)
                        else:
                            print('The pick feels resistance.')
        return
                    
if __name__ == '__main__':
    LockPicking().lockpicking_sequence()