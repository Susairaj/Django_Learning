# Problem
# You have code that accesses list or tuple elements by position, but this makes the code
# somewhat difficult to read at times. You’d also like to be less dependent on position in
# the structure, by accessing the elements by name.


from collections import namedtuple

Subscriber = namedtuple('Subscriber',['addr','joined'])
sub = Subscriber('sub@gmail.com','2012-10-19')
print(sub)
print(sub.addr)

email,joined = sub
print(email)


Stock = namedtuple('Stock',['name','share','price'])
s = Stock('ACE','20','300')
print(s.name)
s = s._replace(share=90)
print(s.share)


Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
# Create a prototype instance
stock_prototype = Stock('', 0, 0.0, None, None)
# Function to convert a dictionary to a Stock
def dict_to_stock(s):
    return stock_prototype._replace(**s)
a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
print(dict_to_stock(a))