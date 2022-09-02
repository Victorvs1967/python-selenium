
from pip import main

def summ(x, y):
  return x + y
  
def main():
  res = summ(1, 2)
  print(f"test: {res} | __name__: {__name__}")


print(f"__name__: {__name__}")

if __name__ == '__main__':
  main()
