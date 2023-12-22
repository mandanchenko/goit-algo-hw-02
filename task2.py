from collections import deque


def is_pal(data):
    data = data.replace(" ", "")
    dq = deque(data.lower())
    for i in range(len(data) // 2):
        a = dq.pop()
        b = dq.popleft()
        if a != b:
            return False
    return True



print(is_pal('12nr1 2'))
print(is_pal('12n1n 21'))
print(is_pal('Minim'))
print(is_pal('12nr12'))
