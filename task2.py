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


if __name__ == "__main__":
    print(is_pal('12nr1 2'))
    print(is_pal('12nn 21'))
    print(is_pal('Minim'))
    print(is_pal('12nr12'))
    print(is_pal('А роза упала на лапу Азора'))
