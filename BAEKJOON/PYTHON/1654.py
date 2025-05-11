import sys

# 랜선 K개를 갖고, N개의 랜선을 만들기 위한 최대 랜선 길이 구하기
K, N = map(int, sys.stdin.readline().split())

lans = []
max_len = 0

for _ in range(K):
    new_lan = int(input())
    if max_len < new_lan:
        max_len = new_lan
    lans.append(new_lan)


def calc_count(lans: list, target: int) -> int:
    count = 0
    for lan in lans:
        count += lan // target

    return count


def binary_search_loop(arr: list, _min: int, _max: int):
    ret = 0

    while _min <= _max:
        # 중간값 계산
        _mid = (_min + _max) // 2

        if _mid == 0:
            break

        count = calc_count(arr, _mid)
        if count >= N:
            ret = max(_mid, ret)
            _min = _mid + 1
        else:
            _max = _mid - 1

    return ret


result = binary_search_loop(lans, 1, max_len)
print(result)
