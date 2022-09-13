from collections import Counter, deque
from queue import LifoQueue, PriorityQueue


def test():
  words = [
    1, 1, 1, 2, 3, 4, 1,
    2, 3, 4, 1, 5, 7, 9,
    7, 4, 3, 2, 2, 7, 5
  ]  
  c = Counter(words)
  res = c.most_common()
  print(c, res)
  
def test2():
  a = deque(maxlen=3)
  a.append(1); a.append(2); a.append(3)
  print(a)
  a.append(4)
  print(a)
  print(a.pop())
  print(a)
  print(a.popleft())
  print(a)
  a.appendleft(11)
  print(a)
  
def test3():
  a = LifoQueue(maxsize=3)
  a.put(1); a.put(2); a.put(3)
  print(a.queue)
  print(a.get())
  print(a.queue)

def test4():
  a = PriorityQueue(maxsize=3)
  a.put((1, 'task1')); a.put((10, 'task2')); a.put((4, 'task3'))
  print(a.queue)
  print(a.get())
  print(a.queue)
  print(a.get())
  print(a.queue)
  
def main():
  test4()


if __name__ == '__main__':
  main()