from collections import deque

def is_palindrom(data:str):
  data = data.replace(" ", "")
  dq = deque(data.lower())
  for i in range(len(data)//2):
    a = dq.pop()
    b = dq.popleft()
    if a!= b:
      return False
  return True


if __name__ == 'main':
    print(is_palindrom('12nr12'))
    print(is_palindrom('12n1n21'))
    print(is_palindrom('Minim'))
    print(is_palindrom('12nr12'))