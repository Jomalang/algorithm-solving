a = int(input())


def fibonachi_recursive(level: int):
    if level == 0:
        return 0
    elif level == 1:
        return 1
    else:
        return fibonachi_recursive(level - 1) + fibonachi_recursive(level - 2)


def fibonachi_loop(level: int):
    a = 0
    b = 1
    c = 0
    for i in range(1, level):
        c = a + b
        a = b
        b = c
    return c


print(fibonachi_recursive(a))
print(fibonachi_loop(a))
