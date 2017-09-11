# Problem
# Your program has become an unreadable mess of hardcoded slice indices and you want
# to clean it up.
# Solution
# Suppose you have some code that is pulling specific data fields out of a record string
# with fixed fields (e.g., from a flat file or similar format):

record = '0123456789012345678901234567890123456789012345678901234567890'
cost = int(record[20:32]) * float(record[40:48])
print(cost)

SHARES = slice(20,32)
PRICE = slice(40,48)
cost = int(record[SHARES]) * float(record[PRICE])
print(cost)

items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
print(items[2:4])
print(items[a])
items[a] = [10,11]
print(items)
del items[a]
print(items)


a = slice(10, 50, 2)
print(a.start)
print(a.stop)
print(a.step)

s = 'HelloWorld'
a.indices(len(s))
print(a)
for i in range(*a.indices(len(s))):
    print(s[i])