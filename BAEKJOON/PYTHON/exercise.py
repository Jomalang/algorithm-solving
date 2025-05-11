from collections import Counter
import heapq

freq = Counter(["a", "b", "c", "a"])
a = freq.most_common()
print(a)

# ==== 최소 힙 기반 우선순위 큐 ====

heap = []
heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)

# 최소값 반환
print(f"최소 값: {heapq.heappop(heap)}")

# 기존 리스트를 힙으로 만들기
arr = [5, 3, 8, 1]
heapq.heapify(arr)
print(f"힙으로 만든 리스트: {arr}")
print(heapq.heappop(arr))

# 최대 힙 기반으로 변경하고 싶다면? 음수 부호를 이용해서 만듦
heap = []
heapq.heappush(heap, -10)
heapq.heappush(heap, -3)
heapq.heappush(heap, -7)

print(f"최대 값: {-heapq.heappop(heap)}")

from array import array

# int형 배열
# 메모리 효율은 높지만 일반 list보다 사용하기 불편
a = array("i", [1, 2, 3])

# deque
from collections import deque

q = deque()
q.append(1)
q.append(2)
q.append(3)

print(f"deque: {q}")
print(f"왼쪽 pop: {q.popleft()}")
print(f"오른쪽 pop: {q.pop()}")


# 존재하지 않는 키에 접근해도 오류가 나지 않도록 기본값이 들어간 dict
from collections import defaultdict

freq = defaultdict(int)
freq["apple"] += 1
freq["banana"] += 3

print(f"defaultDict: {freq}")
print(freq["pineapple"])

# 리스트 실습
fruits = ["apple", "banana"]
fruits.append("grape")
# 리스트 인덱스에 덮어쓰기?
fruits[1] = "orange"

numbers = [10, 20, 30]
numbers.pop()

print(f"리스트: {fruits}")

# tuple - 순서가 있지만 불변한 리스트
point = (3, 4)
x, y = point
print(x + y)

student = ("Alice", 90)
name, score = student[0], student[1]
print(f"name: {name}, score: {score}")

# set - 순서 없고 중복 제거
s = set([1, 2, 3, 4])

s.add(4)
print(s)


# dict - 키(key):값(value)의 해시 테이블
person = {"name": "Bob", "age": 30}
person["job"] = "engineer"
print(f"name: {person["name"]}")
print(f"job: {person["job"]}")

student = {"id": 101, "score": 88}
student[score] = 90
student["name"] = "bob"

print(student)

print(student.get("nickname", "defaultNickname"))

print(f"items: {person.items()}")

for key, value in person.items():
    print(f"{key} -> {value}")

print(list(person.items()))
