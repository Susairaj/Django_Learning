# Problem
# You have a sequence of items, and you’d like to determine the most frequently occurring
# items in the sequence.
# Solution
# The collections.Counter class is designed for just such a problem. It even comes with
# a handy most_common() method that will give you the answer.
# To illustrate, let’s say you have a list of words and you want to find out which words
# occur most often. Here’s how you would do it:

words = [
'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
'my', 'eyes', "you're", 'under'
]

from collections import Counter

words_count = Counter(words)
print(words_count)
top_three = words_count.most_common(3)
print(top_three)

morewords = ['why','are','you','not','looking','in','my','eyes']
for word in morewords:
    words_count[word] += 1
print(words_count)

a = Counter(words)
b = Counter(morewords)
print(a),print(b)
print(a + b)
print(a-b)