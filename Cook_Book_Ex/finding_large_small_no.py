import heapq
nums=[1,3,5,0,-9,0,48]
print(heapq.nlargest(3,nums))
print(heapq.nsmallest(2,nums))

portfolio =[
    {'name':'IBM', 'shares': 100, 'price': 91.1},
    {'name':'AAPL', 'shares': 50, 'price': 543.22},
    {'name':'FB', 'shares': 200, 'price': 21.09},
    {'name':'PQ', 'shares': 35, 'price': 31.75},
    {'name':'YHOO', 'shares': 45, 'price': 16.35},
    {'name':'ACME', 'shares': 75, 'price': 115.65}]

cheap = heapq.nsmallest(2,portfolio,key=lambda t:t['price'])
expensive = heapq.nlargest(2,portfolio, key=lambda t:  t['price'])
print(cheap)
print(expensive)

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
import heapq
heap = list(nums)
print(heap)
heapq.heapify(heap)
print(heap)