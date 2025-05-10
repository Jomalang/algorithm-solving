import sys
from collections import deque

# 입력 받기
N, M, V = map(int, sys.stdin.readline().split())

# 그래프 초기화 (인접 리스트)
graph = [[] for _ in range(N + 1)]  # 1-base

# 간선 정보 입력
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 각 정점의 인접 리스트 정렬 (작은 번호부터 방문)
for i in range(1, N + 1):
    graph[i].sort()


# DFS 구현
def solution_dfs(start):
    visited_arr = [False] * (N + 1)
    result = []

    def dfs(v: int):
        # 방문 체크
        visited_arr[v] = True
        result.append(v)

        for next_v in graph[v]:
            if not visited_arr[next_v]:
                dfs(next_v)

    dfs(start)
    return result


# BFS 구현
def solution_bfs(start):
    visited_arr = [False] * (N + 1)
    result = []

    queue = deque([start])
    visited_arr[start] = True

    while queue:
        cur_v = queue.popleft()
        result.append(cur_v)

        for next_v in graph[cur_v]:
            if not visited_arr[next_v]:
                visited_arr[next_v] = True
                queue.append(next_v)
    return result


# 결과 출력
print(" ".join(map(str, solution_dfs(V))))
print(" ".join(map(str, solution_bfs(V))))
