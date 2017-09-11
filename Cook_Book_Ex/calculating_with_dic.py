# Problem
# You want to perform various calculations (e.g., minimum value, maximum value, sort‐
# ing, etc.) on a dictionary of data.
# Solution
# Consider a dictionary that maps stock names to prices:
import heapq
prices = {
'ACME': 45.23,
'AAPL': 612.78,
'IBM': 205.55,
'HPQ': 37.20,
'FB': 10.75
}

print(heapq.nsmallest(2,zip(prices.values(),prices.keys())))
# in other way
print(min(zip(prices.values(),prices.keys())))
print(sorted(zip(prices.values(), prices.keys())))