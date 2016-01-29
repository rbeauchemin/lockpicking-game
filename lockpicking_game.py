from random import randint

print 'You come across a dark cellar room and spot a chest with a lock in the corner'
yorn = raw_input('Will you attempt to pick the lock? [y]/n: ') or 'y'
if yorn == 'y':
    correct_guess = randint(-180,180)
    print 'You bash the key hole and are able to turn it 180 degrees to the left and right.'
    print 'You know that if you can apply leverage at the correct degree, the lock will free.'
    lockpicks = 5
    print 'You have {0} lockpicks, and one will break if you force it too hard into the wrong angle.'.format(lockpicks)
    damage = 0
    guess = 0
    finished = 'n'
    while lockpicks != 0 and finished == 'n':
        guess = raw_input('Choose an angle (integer between -180 and 180) [previous]: ') or guess
        force = int(raw_input('Choose the force applied (1-5): '))
        guess = int(guess)
        
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
                print '*Click*'
                print 'The lock falls to the floor and the chest opens to reveal gold strewn with shining sapphires and rubies.'
                finished = 'y'
            elif force < 5:
                print 'The pick is pushed with no resistance.'
                
        elif angle == 'close':
            if force == 5:
                lockpicks -= 1
                print 'The pick breaks. You now have {0} lockpicks.'.format(lockpicks)
                damage = 0
            elif force == 4:
                damage += 1
                if damage == 3:
                    lockpicks -= 1
                    print 'The pick feels resistance and snaps from repeated stress. You now have {0} lockpicks.'.format(lockpicks)
                else:
                    print 'The pick feels resistance.'
            else:
                print 'The pick is pushed with no resistance.'
        elif angle == 'nearlyclose':
            if force >= 4:
                lockpicks -= 1
                print 'The pick breaks. You now have {0} lockpicks.'.format(lockpicks)
                damage = 0
            elif force == 3:
                damage += 1
                if damage == 3:
                    lockpicks -= 1
                    print 'The pick feels resistance and snaps from repeated stress. You now have {0} lockpicks.'.format(lockpicks)
                else:
                    print 'The pick feels resistance.'
            else:
                print 'The pick is pushed with no resistance.'
                
        elif angle == 'far':
            if force >= 3:
                lockpicks -= 1
                print 'The pick breaks. You now have {0} lockpicks.'.format(lockpicks)
                damage = 0
            elif force == 2:
                damage += 1
                if damage == 3:
                    lockpicks -= 1
                    print 'The pick feels resistance and snaps from repeated stress. You now have {0} lockpicks.'.format(lockpicks)
                else:
                    print 'The pick feels resistance.'
            else:
                print 'The pick is pushed with no resistance.'
                    
        elif angle == 'realfar':
            if force >= 2:
                lockpicks -= 1
                print 'The pick breaks. You now have {0} lockpicks.'.format(lockpicks)
                damage = 0
            else:
                damage += 1
                if damage == 3:
                    lockpicks -= 1
                    print 'The pick feels resistance and snaps from repeated stress. You now have {0} lockpicks.'.format(lockpicks)
                else:
                    print 'The pick feels resistance.'
    if lockpicks == 0:
        print 'You\'re all out of picks. You\'ll have to leave this treasure for a more skilled treasure hunter.'

                    
                    
                    