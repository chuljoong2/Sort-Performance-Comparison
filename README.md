# 6개 정렬 알고리즘 비교 (퀵, 버블, 선택, 삽입, 쉘, 힙)

## 개요

**`정렬`이란 데이터를 특정한 기준에 따라서 순서대로 나열하는 것을 말한다.** 프로그램에서 데이터를 가공할 때 오름차순이나 내림차순 등 대부분 어떤 식으로든 정렬해서 사용하는 경우가 많기에 정렬 알고리즘은 프로그램을 작성할 때 가장 많이 사용하는 알고리즘 중 하나다.

정렬 알고리즘은 굉장히 다양한데 이 중에서 자주 등장하는 **선택, 삽입, 퀵,** **버블, 쉘, 힙 정렬**에 대해서만 비교하려 한다.

[노션 정리 링크](https://marred-starburst-a3c.notion.site/6-5879fb6dfc9f4b8280ac152ef91db555)

## 코드

### 퀵 정렬 (Quick Sort)

**pivot은 중앙값으로 선택**한다.

**함수가 처음 호출될 때 인자는 하나만 받는다.** 이유는 **파이썬 라이브러리 bigO를 사용할 때 배열 인자 하나만 받는 함수만 측정할 수 있기 때문**이다. 라이브러리 bigO에 대한 설명은 아래서 설명한다.

```python
def quick_sort(A, left=0, right=None):
  if right is None:
    right = len(A) - 1

  if left < right:
    p = partition(A, left, right)

    quick_sort(A, left, p)

    quick_sort(A, p + 1, right)

def partition(A, left, right):
  pivot = A[left + right // 2]

  low = left - 1

  high = right + 1

  while True:
    low += 1

    while A[low] < pivot:
      low += 1

    high -= 1

    while A[high] > pivot:
      high -= 1

    if low >= high:
      return high

    A[low], A[high] = A[high], A[low]

A = [5, 8, 3, 1, 2, 7, 6, 4]

quick_sort(A)

print(A)
```

### 버블 정렬 (Bubble Sort)

```python
def bubble_sort(A):
  n = len(A)

  for p in range(1, n):
    for i in range(1, n - p + 1):
      if A[i - 1] > A[i]:
        A[i - 1], A[i] = A[i], A[i - 1]

A = [5, 8, 3, 1, 2, 7, 6, 4]

bubble_sort(A)

print(A)
```

### 선택 **정렬 (Selection Sort)**

```python
def selection_sort(A):
  n = len(A)

  for i in range(0, n - 1):
    min = i

    for j in range(i + 1, n):
      if A[j] < A[min]:
        min = j

    A[i], A[min] = A[min], A[i]

A = [5, 8, 3, 1, 2, 7, 6, 4]

selection_sort(A)

print(A)
```

### 삽입 정렬 (Insertion Sort)

```python
def insertion_sort(A):
  n = len(A)

  for i in range(1, n):
    current_element = A[i]

    j = i - 1

    while j >= 0 and A[j] > current_element:
      A[j + 1] = A[j]

      j -= 1

    A[j + 1] = current_element

A = [5, 8, 3, 1, 2, 7, 6, 4]

insertion_sort(A)

print(A)
```

### 쉘 정렬 (Shell Sort)

gap은 1부터 3의배수씩 커지며 n보다 작게 선택한다.

```python
def shell_sort(A):
  n = len(A)

  m = n // 3 + 1

  gap = []

  while True:
    gap.append(m)

    if m == 1:
      break

    m = m // 3 + 1

  for h in gap:
    for i in range(h, n):
      CurrentElement = A[i]

      j = i

      while j >= h and A[j - h] > CurrentElement:
        A[j] = A[j - h]

        j -= h

      A[j] = CurrentElement

A = [5, 8, 3, 1, 2, 7, 6, 4]

shell_sort(A)

print(A)
```

### 힙 정렬 (Heap Sort)

**파이썬 라이브러리 heapq를 사용하여 힙 정렬을 구현한 방법**과 **heap 자료구조를 먼저 구현하여 힙 정렬을 구현한 방법**, 두 가지 방법을 이용하여 힙 정렬을 구현하였다.

- **heap 자료구조을 사용한 힙 정렬**

```python
def insert(l, item):
  l.append(item)

  i = len(l) - 1

  while i > 1:
    if l[i] > l[i // 2]:
      l[i], l[i // 2] = l[i // 2], l[i]

    i //= 2

def downheap(i, H, size):
  left = i * 2

  right = i * 2 + 1

  smallest = i

  if left <= size and H[left] > H[smallest]:
    smallest = left

  if right <= size and H[right] > H[smallest]:
    smallest = right

  if smallest != i:
    H[smallest], H[i] = H[i], H[smallest]

    downheap(smallest, H, size)

def heap_sort(A):
  H = [None]

  for item in A:
    insert(H, item)

  n = len(A)

  heapsize = n

  for _ in range(n):
    H[1], H[heapsize] = H[heapsize], H[1]

    heapsize -= 1

    downheap(1, H, heapsize)

  return H[1]

A = [5, 8, 3, 1, 2, 7, 6, 4]

H = heap_sort(A)

print(H)
```

- **파이썬 라이브러리 heapq를 사용한 힙 정렬**

```python
import heapq

def heap_sort(A):
  heap = []

  H = []

  for item in A:
    heapq.heappush(heap, item)

  while len(heap):
    H.append(heapq.heappop(heap))

  return H

A = [5, 8, 3, 1, 2, 7, 6, 4]

H = heap_sort(A)

print(H)
```

**정확한 비교를 위해 최적화가 되어있는 heapq 라이브러리를 사용한 힙 정렬을 사용할 것**이다.

## 비교

6개의 정렬을 다음과 같은 경우에 대해서 성능 분석 및 비교를 하려한다.

- Input Size: **[32, 64, 128, 256, ..., 1048576]**
- Data Case: **정렬된 데이터**인 경우, **역 정렬된 데이터**인 경우, **랜덤 데이터**인 경우
- Exception: **수행시간이 2시간(7200sec) 이상 걸리는 경우 예상치로 측정**한다.

**파이썬 라이브러리 BigO를 사용하여 수행시간을 측정**하였다.

- 라이브러리 설명: [big-O-calculator](https://github.com/Alfex4936/python-bigO-calculator)

### 설치

```bash
pip install big-o-calculator
```

### 사용

```python
from bigO import BigO

lib = BigO()

print("📌 ____ Sort Test Start")

print()

for e in range(5, 21):
  size = 2 ** e

  print(f"►► input size: 2^{e} (= {size})")

  lib.runtime(function, "sorted", size)

  lib.runtime(function, "reversed", size)

  lib.runtime(function, "random", size)

  print()

print("____ Sort Test Finish")
```

## 결과

아래는 **수행결과 출력 예시**입니다.

```bash
►► input size: 2^5 (= 32)
Running function(len 32 sorted array)
Took 0.00058s to sort function(sorted)
Running function(len 32 reversed array)
Took 0.00015s to sort function(reversed)
Running function(len 32 random array)
Took 0.00023s to sort function(random)
```

순서대로 **정렬된 데이터**인 경우, **역 정렬된 데이터**인 경우, **랜덤 데이터**인 경우의 수행시간을 출력한다.

- 정렬된 데이터인 경우: 0.00058s
- 역 정렬된 데이터인 경우: 0.00015s
- 랜덤 데이터인 경우: 0.00023s

### 퀵 정렬 (Quick Sort)

```bash
/Users/chuljoong/PycharmProjects/pythonProject/venv/bin/python /Users/chuljoong/PycharmProjects/pythonProject/main.py

📌 Quick Sort Test Start

►► input size: 2^5 (= 32)
Running quick_sort(len 32 sorted array)
Took 0.00003s to sort quick_sort(sorted)
Running quick_sort(len 32 reversed array)
Took 0.00003s to sort quick_sort(reversed)
Running quick_sort(len 32 random array)
Took 0.00004s to sort quick_sort(random)

►► input size: 2^6 (= 64)
Running quick_sort(len 64 sorted array)
Took 0.00006s to sort quick_sort(sorted)
Running quick_sort(len 64 reversed array)
Took 0.00006s to sort quick_sort(reversed)
Running quick_sort(len 64 random array)
Took 0.00008s to sort quick_sort(random)

►► input size: 2^7 (= 128)
Running quick_sort(len 128 sorted array)
Took 0.00013s to sort quick_sort(sorted)
Running quick_sort(len 128 reversed array)
Took 0.00014s to sort quick_sort(reversed)
Running quick_sort(len 128 random array)
Took 0.00021s to sort quick_sort(random)

►► input size: 2^8 (= 256)
Running quick_sort(len 256 sorted array)
Took 0.00029s to sort quick_sort(sorted)
Running quick_sort(len 256 reversed array)
Took 0.00029s to sort quick_sort(reversed)
Running quick_sort(len 256 random array)
Took 0.00039s to sort quick_sort(random)

►► input size: 2^9 (= 512)
Running quick_sort(len 512 sorted array)
Took 0.00064s to sort quick_sort(sorted)
Running quick_sort(len 512 reversed array)
Took 0.00067s to sort quick_sort(reversed)
Running quick_sort(len 512 random array)
Took 0.00092s to sort quick_sort(random)

►► input size: 2^10 (= 1024)
Running quick_sort(len 1024 sorted array)
Took 0.00173s to sort quick_sort(sorted)
Running quick_sort(len 1024 reversed array)
Took 0.00146s to sort quick_sort(reversed)
Running quick_sort(len 1024 random array)
Took 0.00211s to sort quick_sort(random)

►► input size: 2^11 (= 2048)
Running quick_sort(len 2048 sorted array)
Took 0.00338s to sort quick_sort(sorted)
Running quick_sort(len 2048 reversed array)
Took 0.00330s to sort quick_sort(reversed)
Running quick_sort(len 2048 random array)
Took 0.00554s to sort quick_sort(random)

►► input size: 2^12 (= 4096)
Running quick_sort(len 4096 sorted array)
Took 0.00808s to sort quick_sort(sorted)
Running quick_sort(len 4096 reversed array)
Took 0.00816s to sort quick_sort(reversed)
Running quick_sort(len 4096 random array)
Took 0.00907s to sort quick_sort(random)

►► input size: 2^13 (= 8192)
Running quick_sort(len 8192 sorted array)
Took 0.01289s to sort quick_sort(sorted)
Running quick_sort(len 8192 reversed array)
Took 0.01315s to sort quick_sort(reversed)
Running quick_sort(len 8192 random array)
Took 0.01993s to sort quick_sort(random)

►► input size: 2^14 (= 16384)
Running quick_sort(len 16384 sorted array)
Took 0.02724s to sort quick_sort(sorted)
Running quick_sort(len 16384 reversed array)
Took 0.02815s to sort quick_sort(reversed)
Running quick_sort(len 16384 random array)
Took 0.04318s to sort quick_sort(random)

►► input size: 2^15 (= 32768)
Running quick_sort(len 32768 sorted array)
Took 0.05966s to sort quick_sort(sorted)
Running quick_sort(len 32768 reversed array)
Took 0.05916s to sort quick_sort(reversed)
Running quick_sort(len 32768 random array)
Took 0.09279s to sort quick_sort(random)

►► input size: 2^16 (= 65536)
Running quick_sort(len 65536 sorted array)
Took 0.11759s to sort quick_sort(sorted)
Running quick_sort(len 65536 reversed array)
Took 0.12053s to sort quick_sort(reversed)
Running quick_sort(len 65536 random array)
Took 0.18408s to sort quick_sort(random)

►► input size: 2^17 (= 131072)
Running quick_sort(len 131072 sorted array)
Took 0.24330s to sort quick_sort(sorted)
Running quick_sort(len 131072 reversed array)
Took 0.25335s to sort quick_sort(reversed)
Running quick_sort(len 131072 random array)
Took 0.40444s to sort quick_sort(random)

►► input size: 2^18 (= 262144)
Running quick_sort(len 262144 sorted array)
Took 0.49905s to sort quick_sort(sorted)
Running quick_sort(len 262144 reversed array)
Took 0.51253s to sort quick_sort(reversed)
Running quick_sort(len 262144 random array)
Took 0.88383s to sort quick_sort(random)

►► input size: 2^19 (= 524288)
Running quick_sort(len 524288 sorted array)
Took 1.07091s to sort quick_sort(sorted)
Running quick_sort(len 524288 reversed array)
Took 1.04978s to sort quick_sort(reversed)
Running quick_sort(len 524288 random array)
Took 1.76576s to sort quick_sort(random)

►► input size: 2^20 (= 1048576)
Running quick_sort(len 1048576 sorted array)
Took 2.09934s to sort quick_sort(sorted)
Running quick_sort(len 1048576 reversed array)
Took 2.16671s to sort quick_sort(reversed)
Running quick_sort(len 1048576 random array)
Took 3.92065s to sort quick_sort(random)

Quick Sort Test Finish
```

### 버블 정렬 (Bubble Sort)

```bash
/Users/chuljoong/PycharmProjects/pythonProject/venv/bin/python /Users/chuljoong/PycharmProjects/pythonProject/main.py

📌 Bubble Sort Test Start

►► input size: 2^5 (= 32)
Running bubble_sort(len 32 sorted array)
Took 0.00005s to sort bubble_sort(sorted)
Running bubble_sort(len 32 reversed array)
Took 0.00014s to sort bubble_sort(reversed)
Running bubble_sort(len 32 random array)
Took 0.00008s to sort bubble_sort(random)

►► input size: 2^6 (= 64)
Running bubble_sort(len 64 sorted array)
Took 0.00017s to sort bubble_sort(sorted)
Running bubble_sort(len 64 reversed array)
Took 0.00044s to sort bubble_sort(reversed)
Running bubble_sort(len 64 random array)
Took 0.00029s to sort bubble_sort(random)

►► input size: 2^7 (= 128)
Running bubble_sort(len 128 sorted array)
Took 0.00064s to sort bubble_sort(sorted)
Running bubble_sort(len 128 reversed array)
Took 0.00178s to sort bubble_sort(reversed)
Running bubble_sort(len 128 random array)
Took 0.00119s to sort bubble_sort(random)

►► input size: 2^8 (= 256)
Running bubble_sort(len 256 sorted array)
Took 0.00251s to sort bubble_sort(sorted)
Running bubble_sort(len 256 reversed array)
Took 0.00776s to sort bubble_sort(reversed)
Running bubble_sort(len 256 random array)
Took 0.00527s to sort bubble_sort(random)

►► input size: 2^9 (= 512)
Running bubble_sort(len 512 sorted array)
Took 0.01086s to sort bubble_sort(sorted)
Running bubble_sort(len 512 reversed array)
Took 0.02908s to sort bubble_sort(reversed)
Running bubble_sort(len 512 random array)
Took 0.01945s to sort bubble_sort(random)

►► input size: 2^10 (= 1024)
Running bubble_sort(len 1024 sorted array)
Took 0.04556s to sort bubble_sort(sorted)
Running bubble_sort(len 1024 reversed array)
Took 0.12038s to sort bubble_sort(reversed)
Running bubble_sort(len 1024 random array)
Took 0.08513s to sort bubble_sort(random)

►► input size: 2^11 (= 2048)
Running bubble_sort(len 2048 sorted array)
Took 0.19054s to sort bubble_sort(sorted)
Running bubble_sort(len 2048 reversed array)
Took 0.48302s to sort bubble_sort(reversed)
Running bubble_sort(len 2048 random array)
Took 0.34266s to sort bubble_sort(random)

►► input size: 2^12 (= 4096)
Running bubble_sort(len 4096 sorted array)
Took 0.75421s to sort bubble_sort(sorted)
Running bubble_sort(len 4096 reversed array)
Took 1.94754s to sort bubble_sort(reversed)
Running bubble_sort(len 4096 random array)
Took 1.39076s to sort bubble_sort(random)

►► input size: 2^13 (= 8192)
Running bubble_sort(len 8192 sorted array)
Took 3.05692s to sort bubble_sort(sorted)
Running bubble_sort(len 8192 reversed array)
Took 7.82705s to sort bubble_sort(reversed)
Running bubble_sort(len 8192 random array)
Took 5.61281s to sort bubble_sort(random)

►► input size: 2^14 (= 16384)
Running bubble_sort(len 16384 sorted array)
Took 12.32393s to sort bubble_sort(sorted)
Running bubble_sort(len 16384 reversed array)
Took 31.45901s to sort bubble_sort(reversed)
Running bubble_sort(len 16384 random array)
Took 22.83863s to sort bubble_sort(random)

►► input size: 2^15 (= 32768)
Running bubble_sort(len 32768 sorted array)
Took 49.74195s to sort bubble_sort(sorted)
Running bubble_sort(len 32768 reversed array)
Took 126.99276s to sort bubble_sort(reversed)
Running bubble_sort(len 32768 random array)
Took 93.48883s to sort bubble_sort(random)

►► input size: 2^16 (= 65536)
Running bubble_sort(len 65536 sorted array)
Took 207.16958s to sort bubble_sort(sorted)
Running bubble_sort(len 65536 reversed array)
Took 519.16955s to sort bubble_sort(reversed)
Running bubble_sort(len 65536 random array)
Took 397.89080s to sort bubble_sort(random)

►► input size: 2^17 (= 131072)
Running bubble_sort(len 131072 sorted array)
Took 833.26096s to sort bubble_sort(sorted)
Running bubble_sort(len 131072 reversed array)
Took 2037.94290s to sort bubble_sort(reversed)
Running bubble_sort(len 131072 random array)
Took 1630.22294s to sort bubble_sort(random)

►► input size: 2^18 (= 262144)
Running bubble_sort(len 262144 sorted array)
Took 3209.41249s to sort bubble_sort(sorted)
Running bubble_sort(len 262144 reversed array)
Took 8098.36853s to sort bubble_sort(reversed)
Running bubble_sort(len 262144 random array)
Took 6709.39463s to sort bubble_sort(random)
```

### 선택 **정렬 (Selection Sort)**

```bash
/Users/chuljoong/PycharmProjects/pythonProject/venv/bin/python /Users/chuljoong/PycharmProjects/pythonProject/main.py

📌 Selection Sort Test Start

►► input size: 2^5 (= 32)
Running selection_sort(len 32 sorted array)
Took 0.00006s to sort selection_sort(sorted)
Running selection_sort(len 32 reversed array)
Took 0.00004s to sort selection_sort(reversed)
Running selection_sort(len 32 random array)
Took 0.00004s to sort selection_sort(random)

►► input size: 2^6 (= 64)
Running selection_sort(len 64 sorted array)
Took 0.00014s to sort selection_sort(sorted)
Running selection_sort(len 64 reversed array)
Took 0.00016s to sort selection_sort(reversed)
Running selection_sort(len 64 random array)
Took 0.00015s to sort selection_sort(random)

►► input size: 2^7 (= 128)
Running selection_sort(len 128 sorted array)
Took 0.00052s to sort selection_sort(sorted)
Running selection_sort(len 128 reversed array)
Took 0.00055s to sort selection_sort(reversed)
Running selection_sort(len 128 random array)
Took 0.00056s to sort selection_sort(random)

►► input size: 2^8 (= 256)
Running selection_sort(len 256 sorted array)
Took 0.00206s to sort selection_sort(sorted)
Running selection_sort(len 256 reversed array)
Took 0.00216s to sort selection_sort(reversed)
Running selection_sort(len 256 random array)
Took 0.00377s to sort selection_sort(random)

►► input size: 2^9 (= 512)
Running selection_sort(len 512 sorted array)
Took 0.01075s to sort selection_sort(sorted)
Running selection_sort(len 512 reversed array)
Took 0.01276s to sort selection_sort(reversed)
Running selection_sort(len 512 random array)
Took 0.01294s to sort selection_sort(random)

►► input size: 2^10 (= 1024)
Running selection_sort(len 1024 sorted array)
Took 0.04264s to sort selection_sort(sorted)
Running selection_sort(len 1024 reversed array)
Took 0.03800s to sort selection_sort(reversed)
Running selection_sort(len 1024 random array)
Took 0.04078s to sort selection_sort(random)

►► input size: 2^11 (= 2048)
Running selection_sort(len 2048 sorted array)
Took 0.15170s to sort selection_sort(sorted)
Running selection_sort(len 2048 reversed array)
Took 0.14752s to sort selection_sort(reversed)
Running selection_sort(len 2048 random array)
Took 0.14987s to sort selection_sort(random)

►► input size: 2^12 (= 4096)
Running selection_sort(len 4096 sorted array)
Took 0.55985s to sort selection_sort(sorted)
Running selection_sort(len 4096 reversed array)
Took 0.57550s to sort selection_sort(reversed)
Running selection_sort(len 4096 random array)
Took 0.57766s to sort selection_sort(random)

►► input size: 2^13 (= 8192)
Running selection_sort(len 8192 sorted array)
Took 2.21906s to sort selection_sort(sorted)
Running selection_sort(len 8192 reversed array)
Took 2.29552s to sort selection_sort(reversed)
Running selection_sort(len 8192 random array)
Took 2.30779s to sort selection_sort(random)

►► input size: 2^14 (= 16384)
Running selection_sort(len 16384 sorted array)
Took 8.80106s to sort selection_sort(sorted)
Running selection_sort(len 16384 reversed array)
Took 9.11271s to sort selection_sort(reversed)
Running selection_sort(len 16384 random array)
Took 9.21375s to sort selection_sort(random)

►► input size: 2^15 (= 32768)
Running selection_sort(len 32768 sorted array)
Took 35.06142s to sort selection_sort(sorted)
Running selection_sort(len 32768 reversed array)
Took 36.45018s to sort selection_sort(reversed)
Running selection_sort(len 32768 random array)
Took 37.01337s to sort selection_sort(random)

►► input size: 2^16 (= 65536)
Running selection_sort(len 65536 sorted array)
Took 140.36979s to sort selection_sort(sorted)
Running selection_sort(len 65536 reversed array)
Took 145.85695s to sort selection_sort(reversed)
Running selection_sort(len 65536 random array)
Took 148.07334s to sort selection_sort(random)

►► input size: 2^17 (= 131072)
Running selection_sort(len 131072 sorted array)
Took 560.20774s to sort selection_sort(sorted)
Running selection_sort(len 131072 reversed array)
Took 584.56603s to sort selection_sort(reversed)
Running selection_sort(len 131072 random array)
Took 601.12296s to sort selection_sort(random)

►► input size: 2^18 (= 262144)
Running selection_sort(len 262144 sorted array)
Took 2258.11498s to sort selection_sort(sorted)
Running selection_sort(len 262144 reversed array)
Took 2434.19621s to sort selection_sort(reversed)
Running selection_sort(len 262144 random array)
Took 2592.42371s to sort selection_sort(random)
```

### 삽입 정렬 (Insertion Sort)

```bash
/Users/chuljoong/PycharmProjects/pythonProject/venv/bin/python /Users/chuljoong/PycharmProjects/pythonProject/main.py

📌 Insertion Sort Test Start

►► input size: 2^5 (= 32)
Running insertion_sort(len 32 sorted array)
Took 0.00001s to sort insertion_sort(sorted)
Running insertion_sort(len 32 reversed array)
Took 0.00014s to sort insertion_sort(reversed)
Running insertion_sort(len 32 random array)
Took 0.00008s to sort insertion_sort(random)

►► input size: 2^6 (= 64)
Running insertion_sort(len 64 sorted array)
Took 0.00002s to sort insertion_sort(sorted)
Running insertion_sort(len 64 reversed array)
Took 0.00053s to sort insertion_sort(reversed)
Running insertion_sort(len 64 random array)
Took 0.00024s to sort insertion_sort(random)

►► input size: 2^7 (= 128)
Running insertion_sort(len 128 sorted array)
Took 0.00004s to sort insertion_sort(sorted)
Running insertion_sort(len 128 reversed array)
Took 0.00325s to sort insertion_sort(reversed)
Running insertion_sort(len 128 random array)
Took 0.00096s to sort insertion_sort(random)

►► input size: 2^8 (= 256)
Running insertion_sort(len 256 sorted array)
Took 0.00008s to sort insertion_sort(sorted)
Running insertion_sort(len 256 reversed array)
Took 0.01432s to sort insertion_sort(reversed)
Running insertion_sort(len 256 random array)
Took 0.00248s to sort insertion_sort(random)

►► input size: 2^9 (= 512)
Running insertion_sort(len 512 sorted array)
Took 0.00008s to sort insertion_sort(sorted)
Running insertion_sort(len 512 reversed array)
Took 0.01749s to sort insertion_sort(reversed)
Running insertion_sort(len 512 random array)
Took 0.00941s to sort insertion_sort(random)

►► input size: 2^10 (= 1024)
Running insertion_sort(len 1024 sorted array)
Took 0.00019s to sort insertion_sort(sorted)
Running insertion_sort(len 1024 reversed array)
Took 0.07341s to sort insertion_sort(reversed)
Running insertion_sort(len 1024 random array)
Took 0.03759s to sort insertion_sort(random)

►► input size: 2^11 (= 2048)
Running insertion_sort(len 2048 sorted array)
Took 0.00034s to sort insertion_sort(sorted)
Running insertion_sort(len 2048 reversed array)
Took 0.29273s to sort insertion_sort(reversed)
Running insertion_sort(len 2048 random array)
Took 0.14667s to sort insertion_sort(random)

►► input size: 2^12 (= 4096)
Running insertion_sort(len 4096 sorted array)
Took 0.00078s to sort insertion_sort(sorted)
Running insertion_sort(len 4096 reversed array)
Took 1.15591s to sort insertion_sort(reversed)
Running insertion_sort(len 4096 random array)
Took 0.59982s to sort insertion_sort(random)

►► input size: 2^13 (= 8192)
Running insertion_sort(len 8192 sorted array)
Took 0.00142s to sort insertion_sort(sorted)
Running insertion_sort(len 8192 reversed array)
Took 4.66461s to sort insertion_sort(reversed)
Running insertion_sort(len 8192 random array)
Took 2.37967s to sort insertion_sort(random)

►► input size: 2^14 (= 16384)
Running insertion_sort(len 16384 sorted array)
Took 0.00288s to sort insertion_sort(sorted)
Running insertion_sort(len 16384 reversed array)
Took 18.69529s to sort insertion_sort(reversed)
Running insertion_sort(len 16384 random array)
Took 9.52613s to sort insertion_sort(random)

►► input size: 2^15 (= 32768)
Running insertion_sort(len 32768 sorted array)
Took 0.00569s to sort insertion_sort(sorted)
Running insertion_sort(len 32768 reversed array)
Took 75.74235s to sort insertion_sort(reversed)
Running insertion_sort(len 32768 random array)
Took 38.92274s to sort insertion_sort(random)

►► input size: 2^16 (= 65536)
Running insertion_sort(len 65536 sorted array)
Took 0.01112s to sort insertion_sort(sorted)
Running insertion_sort(len 65536 reversed array)
Took 302.15980s to sort insertion_sort(reversed)
Running insertion_sort(len 65536 random array)
Took 157.07141s to sort insertion_sort(random)

►► input size: 2^17 (= 131072)
Running insertion_sort(len 131072 sorted array)
Took 0.02263s to sort insertion_sort(sorted)
Running insertion_sort(len 131072 reversed array)
Took 1206.30613s to sort insertion_sort(reversed)
Running insertion_sort(len 131072 random array)
Took 635.86112s to sort insertion_sort(random)

►► input size: 2^18 (= 262144)
Running insertion_sort(len 262144 sorted array)
Took 0.04612s to sort insertion_sort(sorted)
Running insertion_sort(len 262144 reversed array)
Took 4823.57653s to sort insertion_sort(reversed)
Running insertion_sort(len 262144 random array)
Took 3213.57116s to sort insertion_sort(random)
```

### 쉘 정렬 (Shell Sort)

```bash
/Users/chuljoong/PycharmProjects/pythonProject/venv/bin/python /Users/chuljoong/PycharmProjects/pythonProject/main.py

📌 Shell Sort Test Start

►► input size: 2^5 (= 32)
Running shell_sort(len 32 sorted array)
Took 0.00002s to sort shell_sort(sorted)
Running shell_sort(len 32 reversed array)
Took 0.00003s to sort shell_sort(reversed)
Running shell_sort(len 32 random array)
Took 0.00003s to sort shell_sort(random)

►► input size: 2^6 (= 64)
Running shell_sort(len 64 sorted array)
Took 0.00004s to sort shell_sort(sorted)
Running shell_sort(len 64 reversed array)
Took 0.00006s to sort shell_sort(reversed)
Running shell_sort(len 64 random array)
Took 0.00007s to sort shell_sort(random)

►► input size: 2^7 (= 128)
Running shell_sort(len 128 sorted array)
Took 0.00009s to sort shell_sort(sorted)
Running shell_sort(len 128 reversed array)
Took 0.00015s to sort shell_sort(reversed)
Running shell_sort(len 128 random array)
Took 0.00017s to sort shell_sort(random)

►► input size: 2^8 (= 256)
Running shell_sort(len 256 sorted array)
Took 0.00020s to sort shell_sort(sorted)
Running shell_sort(len 256 reversed array)
Took 0.00031s to sort shell_sort(reversed)
Running shell_sort(len 256 random array)
Took 0.00043s to sort shell_sort(random)

►► input size: 2^9 (= 512)
Running shell_sort(len 512 sorted array)
Took 0.00047s to sort shell_sort(sorted)
Running shell_sort(len 512 reversed array)
Took 0.00081s to sort shell_sort(reversed)
Running shell_sort(len 512 random array)
Took 0.00127s to sort shell_sort(random)

►► input size: 2^10 (= 1024)
Running shell_sort(len 1024 sorted array)
Took 0.00098s to sort shell_sort(sorted)
Running shell_sort(len 1024 reversed array)
Took 0.00179s to sort shell_sort(reversed)
Running shell_sort(len 1024 random array)
Took 0.00264s to sort shell_sort(random)

►► input size: 2^11 (= 2048)
Running shell_sort(len 2048 sorted array)
Took 0.00240s to sort shell_sort(sorted)
Running shell_sort(len 2048 reversed array)
Took 0.00439s to sort shell_sort(reversed)
Running shell_sort(len 2048 random array)
Took 0.01013s to sort shell_sort(random)

►► input size: 2^12 (= 4096)
Running shell_sort(len 4096 sorted array)
Took 0.00795s to sort shell_sort(sorted)
Running shell_sort(len 4096 reversed array)
Took 0.01098s to sort shell_sort(reversed)
Running shell_sort(len 4096 random array)
Took 0.01373s to sort shell_sort(random)

►► input size: 2^13 (= 8192)
Running shell_sort(len 8192 sorted array)
Took 0.01245s to sort shell_sort(sorted)
Running shell_sort(len 8192 reversed array)
Took 0.02119s to sort shell_sort(reversed)
Running shell_sort(len 8192 random array)
Took 0.03224s to sort shell_sort(random)

►► input size: 2^14 (= 16384)
Running shell_sort(len 16384 sorted array)
Took 0.02393s to sort shell_sort(sorted)
Running shell_sort(len 16384 reversed array)
Took 0.06704s to sort shell_sort(reversed)
Running shell_sort(len 16384 random array)
Took 0.08195s to sort shell_sort(random)

►► input size: 2^15 (= 32768)
Running shell_sort(len 32768 sorted array)
Took 0.05102s to sort shell_sort(sorted)
Running shell_sort(len 32768 reversed array)
Took 0.09884s to sort shell_sort(reversed)
Running shell_sort(len 32768 random array)
Took 0.19273s to sort shell_sort(random)

►► input size: 2^16 (= 65536)
Running shell_sort(len 65536 sorted array)
Took 0.11283s to sort shell_sort(sorted)
Running shell_sort(len 65536 reversed array)
Took 0.20926s to sort shell_sort(reversed)
Running shell_sort(len 65536 random array)
Took 0.39693s to sort shell_sort(random)

►► input size: 2^17 (= 131072)
Running shell_sort(len 131072 sorted array)
Took 0.22413s to sort shell_sort(sorted)
Running shell_sort(len 131072 reversed array)
Took 0.43315s to sort shell_sort(reversed)
Running shell_sort(len 131072 random array)
Took 0.88374s to sort shell_sort(random)

►► input size: 2^18 (= 262144)
Running shell_sort(len 262144 sorted array)
Took 0.45248s to sort shell_sort(sorted)
Running shell_sort(len 262144 reversed array)
Took 0.88095s to sort shell_sort(reversed)
Running shell_sort(len 262144 random array)
Took 2.01296s to sort shell_sort(random)

►► input size: 2^19 (= 524288)
Running shell_sort(len 524288 sorted array)
Took 0.98223s to sort shell_sort(sorted)
Running shell_sort(len 524288 reversed array)
Took 1.91473s to sort shell_sort(reversed)
Running shell_sort(len 524288 random array)
Took 4.61948s to sort shell_sort(random)

►► input size: 2^20 (= 1048576)
Running shell_sort(len 1048576 sorted array)
Took 2.09553s to sort shell_sort(sorted)
Running shell_sort(len 1048576 reversed array)
Took 4.04297s to sort shell_sort(reversed)
Running shell_sort(len 1048576 random array)
Took 11.98816s to sort shell_sort(random)
```

### 힙 정렬 (Heap Sort)

```bash
/Users/chuljoong/PycharmProjects/pythonProject/venv/bin/python /Users/chuljoong/PycharmProjects/pythonProject/main.py

📌 Heap Sort Test Start

►► input size: 2^5 (= 32)
Running heap_sort(len 32 sorted array)
Took 0.00003s to sort heap_sort(sorted)
Running heap_sort(len 32 reversed array)
Took 0.00003s to sort heap_sort(reversed)
Running heap_sort(len 32 random array)
Took 0.00003s to sort heap_sort(random)

►► input size: 2^6 (= 64)
Running heap_sort(len 64 sorted array)
Took 0.00006s to sort heap_sort(sorted)
Running heap_sort(len 64 reversed array)
Took 0.00004s to sort heap_sort(reversed)
Running heap_sort(len 64 random array)
Took 0.00004s to sort heap_sort(random)

►► input size: 2^7 (= 128)
Running heap_sort(len 128 sorted array)
Took 0.00011s to sort heap_sort(sorted)
Running heap_sort(len 128 reversed array)
Took 0.00014s to sort heap_sort(reversed)
Running heap_sort(len 128 random array)
Took 0.00010s to sort heap_sort(random)

►► input size: 2^8 (= 256)
Running heap_sort(len 256 sorted array)
Took 0.00021s to sort heap_sort(sorted)
Running heap_sort(len 256 reversed array)
Took 0.00023s to sort heap_sort(reversed)
Running heap_sort(len 256 random array)
Took 0.00018s to sort heap_sort(random)

►► input size: 2^9 (= 512)
Running heap_sort(len 512 sorted array)
Took 0.00037s to sort heap_sort(sorted)
Running heap_sort(len 512 reversed array)
Took 0.00049s to sort heap_sort(reversed)
Running heap_sort(len 512 random array)
Took 0.00045s to sort heap_sort(random)

►► input size: 2^10 (= 1024)
Running heap_sort(len 1024 sorted array)
Took 0.00060s to sort heap_sort(sorted)
Running heap_sort(len 1024 reversed array)
Took 0.00066s to sort heap_sort(reversed)
Running heap_sort(len 1024 random array)
Took 0.00063s to sort heap_sort(random)

►► input size: 2^11 (= 2048)
Running heap_sort(len 2048 sorted array)
Took 0.00182s to sort heap_sort(sorted)
Running heap_sort(len 2048 reversed array)
Took 0.00180s to sort heap_sort(reversed)
Running heap_sort(len 2048 random array)
Took 0.00424s to sort heap_sort(random)

►► input size: 2^12 (= 4096)
Running heap_sort(len 4096 sorted array)
Took 0.00685s to sort heap_sort(sorted)
Running heap_sort(len 4096 reversed array)
Took 0.00617s to sort heap_sort(reversed)
Running heap_sort(len 4096 random array)
Took 0.00326s to sort heap_sort(random)

►► input size: 2^13 (= 8192)
Running heap_sort(len 8192 sorted array)
Took 0.00561s to sort heap_sort(sorted)
Running heap_sort(len 8192 reversed array)
Took 0.00657s to sort heap_sort(reversed)
Running heap_sort(len 8192 random array)
Took 0.00519s to sort heap_sort(random)

►► input size: 2^14 (= 16384)
Running heap_sort(len 16384 sorted array)
Took 0.00865s to sort heap_sort(sorted)
Running heap_sort(len 16384 reversed array)
Took 0.01057s to sort heap_sort(reversed)
Running heap_sort(len 16384 random array)
Took 0.01048s to sort heap_sort(random)

►► input size: 2^15 (= 32768)
Running heap_sort(len 32768 sorted array)
Took 0.01740s to sort heap_sort(sorted)
Running heap_sort(len 32768 reversed array)
Took 0.02167s to sort heap_sort(reversed)
Running heap_sort(len 32768 random array)
Took 0.03561s to sort heap_sort(random)

►► input size: 2^16 (= 65536)
Running heap_sort(len 65536 sorted array)
Took 0.04045s to sort heap_sort(sorted)
Running heap_sort(len 65536 reversed array)
Took 0.04657s to sort heap_sort(reversed)
Running heap_sort(len 65536 random array)
Took 0.05159s to sort heap_sort(random)

►► input size: 2^17 (= 131072)
Running heap_sort(len 131072 sorted array)
Took 0.07931s to sort heap_sort(sorted)
Running heap_sort(len 131072 reversed array)
Took 0.10046s to sort heap_sort(reversed)
Running heap_sort(len 131072 random array)
Took 0.11422s to sort heap_sort(random)

►► input size: 2^18 (= 262144)
Running heap_sort(len 262144 sorted array)
Took 0.16545s to sort heap_sort(sorted)
Running heap_sort(len 262144 reversed array)
Took 0.20271s to sort heap_sort(reversed)
Running heap_sort(len 262144 random array)
Took 0.30696s to sort heap_sort(random)

►► input size: 2^19 (= 524288)
Running heap_sort(len 524288 sorted array)
Took 0.34730s to sort heap_sort(sorted)
Running heap_sort(len 524288 reversed array)
Took 0.42148s to sort heap_sort(reversed)
Running heap_sort(len 524288 random array)
Took 0.73782s to sort heap_sort(random)

►► input size: 2^20 (= 1048576)
Running heap_sort(len 1048576 sorted array)
Took 0.70225s to sort heap_sort(sorted)
Running heap_sort(len 1048576 reversed array)
Took 0.85943s to sort heap_sort(reversed)
Running heap_sort(len 1048576 random array)
Took 1.70861s to sort heap_sort(random)
```

## 정리

### 정렬된 데이터인 경우

|         | 퀵 정렬 | 버블 정렬  | 선택 정렬  | 삽입 정렬 | 쉘 정렬 | 힙 정렬 |
| ------- | ------- | ---------- | ---------- | --------- | ------- | ------- |
| 32      | 0.00003 | 0.00005    | 0.00006    | 0.00001   | 0.00002 | 0.00003 |
| 64      | 0.00006 | 0.00017    | 0.00014    | 0.00002   | 0.00004 | 0.00006 |
| 128     | 0.00013 | 0.00064    | 0.00052    | 0.00004   | 0.00009 | 0.00011 |
| 256     | 0.00029 | 0.00251    | 0.00206    | 0.00008   | 0.00020 | 0.00021 |
| 512     | 0.00064 | 0.01086    | 0.01075    | 0.00019   | 0.00047 | 0.00037 |
| 1024    | 0.00173 | 0.04556    | 0.04264    | 0.00034   | 0.00098 | 0.00060 |
| 2048    | 0.00338 | 0.19054    | 0.15170    | 0.00078   | 0.00240 | 0.00182 |
| 4096    | 0.00808 | 0.75421    | 0.55985    | 0.00142   | 0.00795 | 0.00685 |
| 8192    | 0.01289 | 3.05692    | 2.21906    | 0.00288   | 0.01245 | 0.00561 |
| 16384   | 0.02724 | 12.32393   | 8.80106    | 0.00569   | 0.02393 | 0.00865 |
| 32768   | 0.05966 | 49.74195   | 35.06142   | 0.01112   | 0.05102 | 0.01740 |
| 65536   | 0.11759 | 207.16958  | 140.36979  | 0.02263   | 0.11283 | 0.04045 |
| 131072  | 0.24330 | 833.26096  | 560.20774  | 0.04612   | 0.22413 | 0.07931 |
| 262144  | 0.49905 | 3209.41249 | 2258.11498 | 0.09311   | 0.45248 | 0.16545 |
| 524288  | 1.07091 | 약 12000   | 약 9000    | 0.15439   | 0.98223 | 0.34730 |
| 1048576 | 2.09934 | 약 50000   | 약 36000   | 0.32311   | 2.09553 | 0.70225 |

![https://user-images.githubusercontent.com/63987872/167281577-c7096274-d728-4a69-8ea6-2b0be3f247f6.png](https://user-images.githubusercontent.com/63987872/167281577-c7096274-d728-4a69-8ea6-2b0be3f247f6.png)

![정렬된-데이터 (2).png](https://user-images.githubusercontent.com/63987872/167281580-7afb330c-2480-4adf-b1bb-d857d5b4a5e9.png)

### 역 정렬된 데이터인 경우

|         | 퀵 정렬 | 버블 정렬  | 선택 정렬  | 삽입 정렬  | 쉘 정렬 | 힙 정렬 |
| ------- | ------- | ---------- | ---------- | ---------- | ------- | ------- |
| 32      | 0.00003 | 0.00014    | 0.00004    | 0.00014    | 0.00003 | 0.00003 |
| 64      | 0.00006 | 0.00044    | 0.00016    | 0.00053    | 0.00006 | 0.00004 |
| 128     | 0.00014 | 0.00178    | 0.00055    | 0.00325    | 0.00015 | 0.00014 |
| 256     | 0.00029 | 0.00776    | 0.00216    | 0.01432    | 0.00031 | 0.00023 |
| 512     | 0.00067 | 0.02908    | 0.01276    | 0.01749    | 0.00081 | 0.00049 |
| 1024    | 0.00146 | 0.12038    | 0.03800    | 0.07341    | 0.00179 | 0.00066 |
| 2048    | 0.00330 | 0.48302    | 0.14752    | 0.29273    | 0.00439 | 0.00180 |
| 4096    | 0.00816 | 1.94754    | 0.57550    | 1.15591    | 0.01098 | 0.00617 |
| 8192    | 0.01315 | 7.82705    | 2.29552    | 4.66461    | 0.02119 | 0.00657 |
| 16384   | 0.02815 | 31.45901   | 9.11271    | 18.69529   | 0.06704 | 0.01057 |
| 32768   | 0.05916 | 126.99276  | 36.45018   | 75.74235   | 0.09884 | 0.02167 |
| 65536   | 0.12053 | 519.16955  | 145.85695  | 302.15980  | 0.20926 | 0.04657 |
| 131072  | 0.25335 | 2037.94290 | 584.56603  | 1206.30613 | 0.43315 | 0.10046 |
| 262144  | 0.51253 | 8098.36853 | 2434.19621 | 4823.57653 | 0.88095 | 0.20271 |
| 524288  | 1.04978 | 약 32000   | 약 9500    | 약 20000   | 1.91473 | 0.42148 |
| 1048576 | 2.16671 | 약 130000  | 약 38000   | 약 80000   | 4.04297 | 0.85943 |

![역-정렬된-데이터.png](https://user-images.githubusercontent.com/63987872/167281571-7d5280c4-12c2-492a-b5c8-2b575e1fd4cc.png)

![역-정렬된-데이터 (1).png](https://user-images.githubusercontent.com/63987872/167281569-0f13bb72-0f0e-4195-8203-c3cf7abbd187.png)

### 랜덤 데이터인 경우

|         | 퀵 정렬 | 버블 정렬  | 선택 정렬  | 삽입 정렬  | 쉘 정렬  | 힙 정렬 |
| ------- | ------- | ---------- | ---------- | ---------- | -------- | ------- |
| 32      | 0.00004 | 0.00008    | 0.00004    | 0.00008    | 0.00003  | 0.00003 |
| 64      | 0.00006 | 0.00029    | 0.00015    | 0.00024    | 0.00007  | 0.00004 |
| 128     | 0.00021 | 0.00119    | 0.00056    | 0.00096    | 0.00017  | 0.00010 |
| 256     | 0.00039 | 0.00527    | 0.00377    | 0.00248    | 0.00043  | 0.00018 |
| 512     | 0.00092 | 0.01045    | 0.01294    | 0.00941    | 0.00127  | 0.00045 |
| 1024    | 0.00211 | 0.08513    | 0.04078    | 0.03759    | 0.00264  | 0.00063 |
| 2048    | 0.00554 | 0.34266    | 0.14987    | 0.14667    | 0.01013  | 0.00424 |
| 4096    | 0.00907 | 1.39076    | 0.57766    | 0.59982    | 0.01373  | 0.00326 |
| 8192    | 0.01993 | 5.61281    | 2.30779    | 2.37967    | 0.03224  | 0.00519 |
| 16384   | 0.04318 | 22.83863   | 9.21375    | 9.52613    | 0.08195  | 0.01048 |
| 32768   | 0.09279 | 93.48883   | 37.01337   | 38.92274   | 0.19273  | 0.03561 |
| 65536   | 0.18308 | 397.89080  | 148.07334  | 157.07141  | 0.39693  | 0.05159 |
| 131072  | 0.40444 | 1630.22294 | 601.12296  | 635.86112  | 0.88374  | 0.11422 |
| 262144  | 0.88383 | 6709.39463 | 2592.42371 | 3213.57116 | 2.01296  | 0.30696 |
| 524288  | 1.76576 | 약 25000   | 약 10000   | 약 13000   | 4.61948  | 0.73782 |
| 1048576 | 3.92065 | 약 100000  | 약 40000   | 약 53000   | 11.98816 | 1.70861 |

![랜덤-데이터 (1).png](https://user-images.githubusercontent.com/63987872/167281567-a344b91c-1ff6-4fa6-8d03-fb20ffd8d8ca.png)

![랜덤-데이터.png](https://user-images.githubusercontent.com/63987872/167281563-00adb355-9774-455c-b6b1-d52c9894aacf.png)

## 분석

### 순위

- Small Input Size & 정렬된 데이터인 경우

**버블 정렬 > 선택 정렬 >> 퀵 정렬 > 쉘 정렬 > 힙 정렬 > 삽입 정렬**

- Medium Input Size & 정렬된 데이터인 경우

**버블 정렬 >> 선택 정렬 >>>>>> 퀵 정렬 > 쉘 정렬 > 힙 정렬 > 삽입 정렬**

- Large Input Size & 정렬된 데이터인 경우

**버블 정렬 >> 선택 정렬 >>> ... >>> 퀵 정렬 > 쉘 정렬 >> 힙 정렬 > 삽입 정렬**

- Small Input Size & 역 정렬된 데이터인 경우

**버블 정렬 > 삽입 정렬 > 선택 정렬 >> 쉘 정렬 > 퀵 정렬 > 힙 정렬**

- Medium Input Size & 역 정렬된 데이터인 경우

**버블 정렬 >> 삽입 정렬 >> 선택 정렬 >>>>>> 쉘 정렬 > 퀵 정렬 > 힙 정렬**

- Large Input Size & 역 정렬된 데이터인 경우

**버블 정렬 >> 삽입 정렬 >> 선택 정렬 >>> ... >>> 쉘 정렬 >> 퀵 정렬 >> 힙 정렬**

- Small Input Size & 랜덤 데이터인 경우

**버블 정렬 > 삽입 정렬 > 선택 정렬 >> 쉘 정렬 > 퀵 정렬 > 힙 정렬**

- Medium Input Size & 랜덤 데이터인 경

**버블 정렬 >> 삽입 정렬 > 선택 정렬 >>>>>> 쉘 정렬 > 퀵 정렬 > 힙 정렬**

- Large Input Size & 랜덤 데이터인 경우

**버블 정렬 >> 삽입 정렬 > 선택 정렬 >>> ... >>> 쉘 정렬 >>> 퀵 정렬 >> 힙 정렬**

### 정렬 별 평가

- 퀵 정렬: 어떠한 경우에서든 4초이내에 수행이 가능하며 평균적으로 준수한 수행시간을 가진다. 하지만 설정하는 피봇방법에 따라 성능 차이가 발생할 수 있다.
- 버블 정렬: 어떠한 경우에서든 성능이 가장 안좋으며 데이터 사이즈가 20000을 넘기면 분단위로 넘어간다.
- 선택 정렬: 버블 정렬보다는 성능이 좋지만 전체적으로 성능이 안좋은 편에 속하며 데이터 사이즈가 50000을 넘기면 분단위로 넘어간다.
- 삽입 정렬: 정렬이 되어있는 데이터인 경우 데이터 사이즈가 크건 작건 거의 0.00001초 단위를 가진다. 하지만 정렬이 되어 있지 않다면 성능이 안좋은 편에 속하며 선택 정렬과 성능이 비슷하다.
- 쉘 정렬: 어떠한 경우에서든 10초이내에 수행이 가능하며 평균적으로 준수한 수행시간을 가진다. 하지만 설정하는 간격에 따라 성능 차이가 발생할 수 있다.
- 힙 정렬: 대부분의 경우와 평균적으로 가장 성능이 좋으며 어떠한 경우에도 1초대안에 수행이 가능하다.

### 시간 복잡도

|           | 최선      | 평균      | 최악      |
| --------- | --------- | --------- | --------- |
| 퀵 정렬   | O(nlog₂n) | O(nlog₂n) | O(nlog₂n) |
| 버블 정렬 | O(n²)     | O(n²)     | O(n²)     |
| 선택 장렬 | O(n²)     | O(n²)     | O(n²)     |
| 삽입 정렬 | O(n)      | O(n²)     | O(n²)     |
| 쉘 정렬   | O(n)      | O(n^1.5)  | O(n²)     |
| 힙 정렬   | O(nlog₂n) | O(nlog₂n) | O(nlog₂n) |
