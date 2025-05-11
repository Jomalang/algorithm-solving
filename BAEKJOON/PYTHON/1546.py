import sys

N = int(input())
scores = list(map(int, sys.stdin.readline().split(" ")))
max = 0

for i in range(N):
    if scores[i] > max:
        max = scores[i]

print((sum(scores) / N) * (100 / max))
