# def extendList(val, list=[]):
#     list.append(val)
#     return list
#
# list1 = extendList(10)
# list2 = extendList(123,[])
# list3 = extendList('a',[])
#
# print ("list1 = %s" % list1)
# print ("list2 = %s" % list2)
# print ("list3 = %s" % list3)

def multipliers():
    return [lambda x: i * x for i in range(4)]


def multipliers():
  for i in range(4): yield lambda x : i * x

def multipliers():
  return [lambda x, i=i : i * x for i in range(4)]

from functools import partial
from operator import mul

def multipliers():
  return [partial(mul, i) for i in range(4)]

print([m(2)for m in multipliers()])