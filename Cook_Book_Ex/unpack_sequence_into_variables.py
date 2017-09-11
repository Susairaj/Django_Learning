# Problem
# You have an N-element tuple or sequence that you would like to unpack into a collection
# of N variables.
# Solution
# Any sequence (or iterable) can be unpacked into variables using a simple assignment
# operation. The only requirement is that the number of variables and structure match
# the sequence. For example:


m =(1,2,3)
a,b,c = m
print(a)
print(b)
print(c)
data = ('susai','25',(1991,3,15))
name,age,dob=data
print(name)
print(age)
print (dob)
name,age,(year,month,day)=data
print(month)
print (year)
s='hello'
first,second,third,fourth,fifth = s
print (first)