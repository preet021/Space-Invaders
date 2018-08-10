import SpaceInvaders
from GetInput import _getChUnix as getinp
import os

#creating an instance of the game engine
myEngine = SpaceInvaders.Engine()

#general instructions to play the game
os.system('tput reset')
print('                                 ----------------- Welcome to Space Invaders --------------\n')
print('Instructions:')
print('press "a" to move the spaceship to left')
print('press "d" to move the spaceship to right')
print('use "w" and "s" to shoot')
print('press any key to start the game')
print('press "q" to quit\n')

inp = getinp()
if inp() != 'q':
    myEngine.run()
else:
    print('Come back again!')
