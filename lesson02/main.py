# Named function parameters

def test01(a, b, *, c=None):
  return (a, b, c)

def get_html(url, headers, *, proxy: str = None):
  if isinstance(proxy, str):
    print(f'proxy: {proxy}, {url}:{headers}')
  elif proxy is None:
    print(f'proxy: none, {url}:{headers}')
  
def main():
  print(test01(10, '20', c='str'))
  url = 'html://google.com'
  headers = 'authorization'
  get_html(url, headers, proxy='http://proxy.com')
  get_html(url, headers)


if __name__ == '__main__':
  main();