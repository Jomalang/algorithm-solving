n = int(input())
k = 0
strArr = []


def hanoi(_from: int, _to: int, _mid: int, n: int):
    global k
    if n == 1:
        strArr.append(f"{_from} {_to}")
        k += 1
        return

    hanoi(_from, _mid, _to, n - 1)
    strArr.append(f"{_from} {_to}")
    k += 1
    hanoi(_mid, _to, _from, n - 1)


hanoi(1, 3, 2, n)
print(k)

print(str.join("\n", strArr))
