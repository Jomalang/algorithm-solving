import sys

T = int(input())
result = []

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    result.append(A + B)

for num in result:
    print(num)
