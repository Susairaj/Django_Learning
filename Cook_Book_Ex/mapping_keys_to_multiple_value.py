# Problem
# You want to make a dictionary that maps keys to more than one value (a so-called
# “multidict”).
# Solution
# A dictionary is a mapping where each key is mapped to a single value. If you want to
# map keys to multiple values, you need to store the multiple values in another container
# such as a list or set. For example, you might make dictionaries like this:

d = {

    'a':[1,2,3],
    'b':[1,2]
}
e = {

    'a':{1,2,3},
    'b':{1,2}
}
from collections import defaultdict
d = defaultdict(list)
print(d)
d['a'].append(1)
d['b'].append(2)
d['b'].append(3)
d = defaultdict(set)
d['a'].add(1)
print(d)