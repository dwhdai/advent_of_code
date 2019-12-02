import numpy as np
import math
import pandas as pd

modules = pd.read_csv('C:/Users/David/Documents/advent_of_code/2019/day1_input.txt')

def calculate_fuel(mass):
    """This function takes an input array of module masses and
    returns the necessary fuel.
    
    Arguments:
        modules {numpy array} -- array of module masses 
    """    
    
    fuel = (mass//3) - 2
    return(fuel)

module_fuel = calculate_fuel(modules['weight'])

#module_fuel = np.array([100756,1969])
extra_fuel = calculate_fuel(module_fuel)
total_fuel = module_fuel + extra_fuel

for i in range(0, len(module_fuel)):
    while extra_fuel[i] > 0:
        if calculate_fuel(extra_fuel[i])<=0:
            i += 1
            break
        total_fuel[i] = total_fuel[i] + calculate_fuel(extra_fuel[i])
        extra_fuel[i] = calculate_fuel(extra_fuel[i])
    
print(total_fuel.sum())

