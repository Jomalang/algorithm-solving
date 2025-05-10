a = int(input())

arr = [int(input()) for _ in range(a)]


def selectionSort(arr: list, n: int):
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


selectionSort(arr, a)

for num in arr:
    print(num)
