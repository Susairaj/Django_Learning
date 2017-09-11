# Problem
# You have two dictionaries and want to find out what they might have in common (same
# keys, same values, etc.).
# Solution
# Consider two dictionaries:

a = {
'x' : 1,
'y' : 2,
'z' : 3
}
b = {
'w' : 10,
'x' : 11,
'y' : 2
}

print(a.keys() & b.keys())
print(a.keys() - b.keys())
print(a.items() & b.items())
print(a.items() - b.items())

c = {key:a[key] for key in a.keys() - {'z', 'w'}}
print(c)