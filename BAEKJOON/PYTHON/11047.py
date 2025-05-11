import sys

N, K = map(int, sys.stdin.readline().split(" "))

coins = []
for _ in range(N):
    coins.append(int(input()))

len = N - 1
count = 0
while K > 0:
    if K // coins[len] <= 0:
        len -= 1
    else:
        count += K // coins[len]
        K = K % coins[len]
        len -= 1

print(count)
