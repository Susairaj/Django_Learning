# Problem
# You have data inside of a sequence, and need to extract values or reduce the sequence
# using some criteria.
# Solution
# The easiest way to filter sequence data is often to use a list comprehension. For example:

sample_list = [1,2,3,4,-1,-2,-9]

print([n for n in sample_list if n > 0])
print([n for n in sample_list if n < 0])

pos = (n for n in sample_list if n > 0)
print(pos)
for s in pos:
    print(s)


values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False
ivals = list(filter(is_int, values))
print(ivals)

import math
print([math.sqrt(n) for n in sample_list if n > 0])



addresses = [
    'north street',
    'north street1',
    'north street2',
    'north street3',
    'north street4',
    'north street5',
]

counts = [ 0, 3, 10, 4, 1, 7, 6, 1]
from itertools import compress
more5 = [n > 5 for n in counts]
print(more5)
print(list(compress(addresses,more5)))
