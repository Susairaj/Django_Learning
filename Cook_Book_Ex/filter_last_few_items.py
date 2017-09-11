from collections import deque
def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
    previous_lines.append(line)
# Example use on a file
if __name__ == '__main__':
    with open('/home/susai/Downloads/test1') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
        print(line, end='')
        print('-'*20)


#
q=deque()
q.append(1)
q.append(2)
print(q)
q.appendleft(5)
print(q)
q.pop()
print(q)
q.popleft()
print(q)