# Solar System💖

from math import pi
from random import choice as ch
planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn'
]

random_planet = ch(planets)
if random_planet == 'Mercury':
  print('The area of Mercury is ', 4*pi*(2440 **2))
elif random_planet == 'Venus':
  print('The area of Venus is ', 4*pi*(6052 **2))
elif random_planet == 'Earth':
  print('The area of Earth is ', 4*pi*(6371 **2))
elif random_planet == 'Mars':
  print('The area of Mars is ', 4*pi*(3390 **2))
elif random_planet == 'Saturn':
  print('The area of Saturn is ', 4*pi*(58232 **2))
else:
  print('Oops! An error has occured')
