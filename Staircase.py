import math
import os
import random
import re
import sys

def staircase(n):
    num_stairs = n
    for stairs in range(1, n):
        print(' ' * (n-2), '#' * stairs)
        n -= 1
    print('#' * num_stairs)



n = 6
staircase(n)