# creating our first import

import math

print(math.sin(math.pi/2))

# importing just a entities of module

# from math import pi

# print(round(pi * 25, 2))

# if you wanna import a lot of modules use:

# from module ... import *

# if you wanna import a module using other name use:

# import math as matematica

# if you wanna import a entities of module using other name use>:

# from math import pi as PI, sin as sine

# name all entities in math module:

for name in dir(math):
    print(name, end='\n')
