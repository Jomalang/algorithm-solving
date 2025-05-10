a = int(input())

arr = [int(input()) for _ in range(a)]


def insertionSort(arr: list, n: int):
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


insertionSort(arr, a)

for num in arr:
    print(num)
