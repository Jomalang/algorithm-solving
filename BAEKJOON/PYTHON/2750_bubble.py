a = int(input())

arr = [int(input()) for _ in range(a)]


def bubbleSort(arr: list, n: int):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]


bubbleSort(arr, a)

for num in arr:
    print(num)
