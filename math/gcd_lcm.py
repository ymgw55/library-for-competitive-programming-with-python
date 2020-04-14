#from math import gcd #3.5以降
from fractions import gcd #3.4以前
from functools import reduce

def lcm(x, y):
    return (x*y)//gcd(x, y)

def gcd_list(num_list):
    return reduce(gcd, num_list)
