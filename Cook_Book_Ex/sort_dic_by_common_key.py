# Problem
# You have a list of dictionaries and you would like to sort the entries according to one
# or more of the dictionary values.
# Solution
# Sorting this type of structure is easy using the operator module’s itemgetter function.
# Let’s say you’ve queried a database table to get a listing of the members on your website,
# and you receive the following data structure in return:

rows = [
{'fname':'Brian', 'lname': 'Jones', 'uid': 1003},
{'fname':'David', 'lname': 'Beazley', 'uid': 1002},
{'fname':'John', 'lname': 'Cleese', 'uid': 1001},
{'fname':'Big', 'lname': 'Jones', 'uid': 1004}
]

from operator import itemgetter
import heapq
print(sorted(rows,key=itemgetter('fname')))
print(sorted(rows,key=itemgetter('uid')))

print(sorted(rows,key=itemgetter('uid','fname')))

print(sorted(rows, key=lambda r: r['fname']))
print(sorted(rows, key=lambda r: (r['lname'],r['fname'])))

#find min
print(min(rows,key=itemgetter('uid')))
print(heapq.nsmallest(1,rows,key=lambda x:x['uid']))
print(heapq.nsmallest(1,rows,key=itemgetter('uid')))

#find max
print(max(rows,key=itemgetter('uid')))
print(heapq.nlargest(1,rows,key=lambda x:x['uid']))
print(heapq.nlargest(1,rows,key=itemgetter('uid')))
