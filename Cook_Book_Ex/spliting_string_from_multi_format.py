# Problem
# You need to split a string into fields, but the delimiters (and spacing around them) aren’t
# consistent throughout the string.
# Solution
# The split() method of string objects is really meant for very simple cases, and does
# not allow for multiple delimiters or account for possible whitespace around the delim‐
# iters. In cases when you need a bit more flexibility, use the re.split() method:
import re

line = 'asdf fjdk; afed, fjek,asdf,    foo'
print(re.split(r'[;,\s]\s*', line))
print(re.split(r'(;|,|\s)\s*', line))