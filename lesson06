from array import array

def test():
  a = array('i', [1, 2, 3, 4])

  print(a)
  print(a[0])
  print(a[-1])
  print(a[1:])
  print(a[::-1])
  a.reverse()
  print(a)
  print(a.typecode)
  print(a * 2)
  print(a.itemsize)
  a.append(5)
  print(a)
  print(a.count(2))
  b = a.tolist()
  print(b)
  print(type(b))
  print(a.index(3))
  a.insert(2, 8)
  print(a)
  print(a.pop(2))
  print(a)

def test2():
  a = array('i', list(range(100)))
  
  for value in a:
    for value in a:
      if value % 2 == 0: a[a.index(value)] = 255
  
  print(a)

def main():
  test2()

if __name__ == "__main__":
  main()