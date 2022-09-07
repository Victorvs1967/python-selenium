# Yield Python

def test():
  # for i in range(3):
  #   yield i
  # yield from [1, 2, 3, 4]
  yield from [x for x in range(20)]
  
def test_send():
  print('started')
  
  while True:
    x = yield
    print('recv:', x)
    

def main():
  a = test()
  b = iter('test')
  c = test_send()
  [print(i) for i in test()]
  [print(next(a)) for _ in range(4)]
  [print(next(b)) for _ in 'test']
  # [next(c) for _ in range(5)]
  next(c)
  c.send('test')

if __name__ == '__main__':
  main()
