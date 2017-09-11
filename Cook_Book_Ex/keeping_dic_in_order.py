# Problem
# You want to create a dictionary, and you also want to control the order of items when
# iterating or serializing.
# Solution
# To control the order of items in a dictionary, you can use an OrderedDict from the
# collections module. It exactly preserves the original insertion order of data when
# iterating. For example:

from collections import OrderedDict
import json
d=OrderedDict()
d['foo'] = 1
d['go'] = 2
print(d)
print(json.dumps(d))