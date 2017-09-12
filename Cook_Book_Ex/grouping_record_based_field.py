# Problem
# You have a sequence of dictionaries or instances and you want to iterate over the data
# in groups based on the value of a particular field, such as date.
# Solution
# The itertools.groupby() function is particularly useful for grouping data together
# like this. To illustrate, suppose you have the following list of dictionaries:
rows = [
    {'address':'north street','date':'07/01/2012'},
    {'address':'north street','date':'07/01/2012'},
    {'address':'north street1','date':'07/01/2012'},
    {'address':'north street1','date':'08/01/2012'},
    {'address':'north street1','date':'08/01/2012'},
]

from operator import itemgetter
from itertools import groupby

print(sorted(rows,key=itemgetter('date')))

for date,items in groupby(rows,key=itemgetter('date')):
    print(date)
    for i in items:
        print('',i)


#OR

from collections import defaultdict

rows_by_date = defaultdict(list)
for row in rows:
    print(rows_by_date[row['date']].append(row))
for r in rows_by_date['08/01/2012']:
    print(r)
