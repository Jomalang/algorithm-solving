avg = 0
midList = []


def bubbleSort(arr: list, n: int):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


for _ in range(5):
    newNum = int(input())
    avg += newNum
    midList.append(newNum)

print(int(avg / 5))

bubbleSort(midList, 5)
print(midList[3])
