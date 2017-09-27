import re
str = 'an example word:cat!!'
match = re.search(r'word:\w\w\w', str)
# If-statement after search() tests if it succeeded
if match:
    print ('found', match.group()) ## 'found word:cat'
else:
    print ('did not find')

match = re.search(r'pi+g', 'piiig')
print(match.group() == "piiig")
## Finds the first/leftmost solution, and within it drives the +
## as far as possible (aka 'leftmost and largest').
## In this example, note that it does not get to the second set of i's.
match = re.search(r'i+', 'piiiiii')
print(match.group() == "iiiiii")
## \s* = zero or more whitespace chars
## Here look for 3 digits, possibly separated by whitespace.
match = re.search(r'\d\s*\d\s*\d', 'xx1 2   3xx')
print(match.group() == "1 2   3")

match = re.search(r'\d\s*\d\s*\d', 'xx12  3xx')
print(match.group() == "12  3")

match = re.search(r'\d\s*\d\s*\d', 'xx123xx')
print(match.group() == "123")
## ^ = matches the start of string, so this fails:
match = re.search(r'^b\w+', 'foobar')
print(match == None)
## but without the ^ it succeeds:
match = re.search(r'b\w+', 'foobar')
print(match.group() == "bar")

#Emails Example
str = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'\w+@\w+', str)
print(match)
if match:
    print(match.group())
#Square Brackets
match = re.search(r'[\w.-]+@[\w.-]+', str)
if match:
    print (match.group())  ## 'alice-b@google.com'

#Group Extraction
str = 'purple alice-b@google.com monkey dishwasher'
match = re.search('([\w.-]+)@([\w.-]+)', str)
if match:
    print (match.group())   ## 'alice-b@google.com' (the whole match)
    print (match.group(1))  ## 'alice-b' (the username, group 1)
    print (match.group(2))  ## 'google.com' (the host, group 2)

## Suppose we have a text with many email addresses
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher j@gmil.com m@gmail.com d@gmail.com'

## Here re.findall() returns a list of all the found email strings
emails = re.findall(r'[\w\.-]+@[\w\.-]+', str) ## ['alice@google.com', 'bob@abc.com']
print(emails)
for email in emails:
    # do something with each found email string
    print (email)

# Open file
f = open('/home/susai/Documents/measuring-employee-performance.py', 'r')
# Feed the file text into findall(); it returns a list of all the found strings
strings = re.findall(r'—', f.read())
print(strings)

#findall and Groups
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
tuples = re.findall(r'([\w\.-]+)@([\w\.-]+)', str)
print(tuples)  ## [('alice', 'google.com'), ('bob', 'abc.com')]
for tuple in tuples:
    print('UserName:',tuple[0])  ## username
    print('Host:',tuple[1])  ## host

#Substitution (optional)
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
## re.sub(pat, replacement, str) -- returns new string with all replacements,
## \1 is group(1), \2 group(2) in the replacement
print(re.sub(r'([\w\.-]+)@([\w\.-]+)', r'\1@yo-yo-dyne.com', str))
## purple alice@yo-yo-dyne.com, blah monkey bob@yo-yo-dyne.com blah dishwasher