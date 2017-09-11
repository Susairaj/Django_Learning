# Problem
# You want to eliminate the duplicate values in a sequence, but preserve the order of the
# remaining items.
# Solution
# If the values in the sequence are hashable, the problem can be easily solved using a set
# and a generator. For example:

def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))
print(sorted(list(set(a))))

def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
print(list(dedupe(a, key=lambda d: (d['x'],d['y']))))
print(list(dedupe(a, key=lambda d: (d['x']))))
print(list(dedupe(a, key=lambda d: (d['y']))))
for b in a:
    print(sorted(list(set(b.values()))))