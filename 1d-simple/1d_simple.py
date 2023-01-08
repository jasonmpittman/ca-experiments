

""" 1d-simple.py: A simple 1d cellular automata experiment """

# standard library imports

# external library imports
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

__author__ = "Jason M. Pittman"
__copyright__ = "Copyright 2023"
__credits__ = ["Jason M. Pittman"]
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Jason M. Pittman"
__email__ = "jason@jasonmpittman.com"
__status__ = "Experimental"


# utility functions
def decimal_to_binary(n):
    return bin(n).replace("0b", "").zfill(8)

def binary_to_decimal(b):
    return int(b,2)

def evolve_cell(left_neighbor, cell, right_neighbor, rule):
    index = int(left_neighbor + cell + right_neighbor)
    
    return rule[index]
    
#get the rule from the user
rule_input = int(input("Enter a rule as a three digit integer: ")) #over 255 grows the row
rule = decimal_to_binary(rule_input)

row = np.fromiter(rule, dtype=int)

# reverse the array because binary reads right to left and the ca will read left to right
row = row[::-1]

#print(row)

# initialize the first row per Wolfram
grid = np.array([0,0,0,1,0,0,0,0])
print(grid)

# compute cell changes for the neighborhoods
old_grid = grid
for cell in range(grid[1], len(grid) - 1):

    left_neighbor = old_grid[cell - 1]
    right_neighbor = old_grid[cell + 1]

    new_cell = evolve_cell(left_neighbor, cell, right_neighbor, rule)
    grid[cell] = new_cell
    print(grid)

# step forward in T

# animate the step T



