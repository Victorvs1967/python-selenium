def test(*args):
  print(args)

def test1(*args, **kwargs):
  print(kwargs)

def main():
  a = [1, 2, 3]
  b = {'1': '1'}
  test(*a)
  test1(1, **b)

if __name__ == '__main__':
  main()