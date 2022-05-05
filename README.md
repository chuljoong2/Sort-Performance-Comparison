# 6개 정렬 알고리즘 비교 (퀵, 버블, 선택, 삽입, 쉘, 힙)

## 개요

**`정렬`이란 데이터를 특정한 기준에 따라서 순서대로 나열하는 것을 말한다.** 프로그램에서 데이터를 가공할 때 오름차순이나 내림차순 등 대부분 어떤 식으로든 정렬해서 사용하는 경우가 많기에 정렬 알고리즘은 프로그램을 작성할 때 가장 많이 사용하는 알고리즘 중 하나다.

정렬 알고리즘은 굉장히 다양한데 이 중에서 많이 사용하는 **선택, 삽입, 퀵 정렬**과 그 외 추가로 **버블, 쉘, 힙 정렬**에 대해서만 알아보려 한다.

## 설명

[퀵 정렬 (Quick Sort)](quick_sort.md)

[버블 정렬 (Bubble Sort)](bubble_sort.md)

[선택 정렬 (Selection Sort)](selection_sort.md)

[삽입 정렬 (Insertion Sort)](insertion_sort.md)

[쉘 정렬 (Shell Sort)](shell_sort.md)

[힙 정렬 (Heap Sort)](heap_sort.md)

## 비교

또한 6개의 정렬을 다음과 같은 경우에 대해서 성능 분석 및 비교를 하려한다.

- 입력 데이터 수(n) : 32, 64, 128, 256, ..., 1048576
- 세 개의 그래프: 정렬된 데이터인 경우, 랜덤 데이터인 경우, 역 정렬된 데이터인 경우

시간 측정은 time 라이브러리를 활용하여 측정한다.

```python
import time

start = time.time()

end = time.time()

print(f"{end - start:.5f} sec")
```
