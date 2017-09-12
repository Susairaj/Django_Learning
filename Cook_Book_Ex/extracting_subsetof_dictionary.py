# Problem
# You want to make a dictionary that is a subset of another dictionary.
# Solution
# This is easily accomplished using a dictionary comprehension. For example:

prices = {
'ACME': 45.23,
'AAPL': 612.78,
'IBM': 205.55,
'HPQ': 37.20,
'FB': 10.75
}

M = {key:value for key,value in prices.items() if value >200}
print(M)