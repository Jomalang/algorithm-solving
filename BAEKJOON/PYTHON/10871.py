import sys


N, X = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

# 방법 1: 리스트 컴프리헨션
result = [str(num) for num in arr if num < X]
print(" ".join(result))
