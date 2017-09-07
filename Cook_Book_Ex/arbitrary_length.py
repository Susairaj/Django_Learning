# Problem
# You need to unpack N elements from an iterable, but the iterable may be longer than N
# elements, causing a “too many values to unpack” exception.
# Solution
# Python “star expressions” can be used to address this problem. For example, suppose
# you run a course and decide at the end of the semester that you’re going to drop the first
# and last homework grades, and only average the rest of them. If there are only four
# assignments, maybe you simply unpack all four, but what if there are 24? A star expres‐
# sion makes it easy:

def drop_first_last(*grades):
    first, *middle, last = grades
    print(first)
    print(middle)
    print(last)
    print(sum(grades))
    # return avg(middle)
drop_first_last(1,2,3)


records = ('david','a@gmail.com','123',456)
name,gmail,*phone = records
print(name)
print(phone)

*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(trailing)
print(current)


records = [
('foot', 1, 2),
('bar', 'hello'),
('foo', 3, 4),
]
def do_foo(x, y):
    print('foo', x, y)
def do_bar(s):
    print('bar', s)
for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)



line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname)
print(fields)
print(homedir)
print(sh)


record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *test,(*_,month,year)=record
print(name)
print(year)
print(_)
print(test)
print(month)


items = [1, 10, 7, 4, 5, 9]
def sum(itmes):
    head, *tail = items
    return head + sum(tail) if tail else head
sum(items)