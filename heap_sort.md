# 힙 **정렬 (Heap Sort)**

**힙은 힙 조건을 만족하는 완전 이진 트리다. 힙 조건이란 각 노드의 값이 자식 노드의 값보다 커야 한다는 것을 말한다. 노드의 값은 우선순위라고 일컫는다. 따라서 힙의 루트노드에는 가장 높은 우선순위 즉, 가장 큰 값이 저장**되어 있다. (루트노드에 가장 큰 값이 들어가는 경우: MaxHeap, 작은 값이 들어가는 경우: MinHeap)

다음은 힙 정렬을 통하여 정렬한 하나의 예시이다.

![https://user-images.githubusercontent.com/63987872/166850785-f5b7c22a-01e1-42b7-9221-ec3214ef0e80.png](https://user-images.githubusercontent.com/63987872/166850785-f5b7c22a-01e1-42b7-9221-ec3214ef0e80.png)

배열 A에 힙을 저장한다면 A[0]은 비워 두고 A[1]부터 A[n]까지에 힙 노드들을 트리의 층별로 좌우로 저장한다.

- A[i]의 부모 노드는 A[i/2]이다. 단, i가 홀수일 때는 i/2에서 정수 부분만을 취한다. ex. A[7]의 부모노드는 A[7/2] = A[3]이다.
- A[i]의 왼쪽 자식 노드는 A[2*i]이고, 오른쪽 자식 노드는 A[2*i+1]이다. ex. A[4]의 왼쪽 자식 노드는 A[2*4] = A[8]이고, 오른쪽 자식 노드는 A[2*4+1] = A[9]이다.

**`힙 정렬`은 힙 자료구조를 이용하는 정렬 알고리즘**이다.

정렬을 위해 최대힙을 만들고 루트노드에 저장된 가장 큰 수를 배열의 가장 끝으로 이동시킨다. 그리고 루트노드에 새로 저장된 숫자로 인해 위배된 힙 조건을 해결하여 힙조건을 만족시키고 힙 크기를 1개 줄인다. 그리고 이 과정을 반복하여 나머지 숫자를 정렬한다.

## 힙 **정렬** 알고리즘

```
def heap_sort(A):
	# 입력: 배열 A
	# 출력: 정렬된 배열 A
	배열 A를 힙 자료구조로 만든다.
	n = len(A)
	heapSize = n - 1
	for i = 1 to n - 1:
		A[1], A[heapSize] = A[heapSize], A[1]
		heapSize = heapSize - 1
		위배된 힙 조건을 만족시킨다.
	return A
```

아래와 같은 배열이 있다.

A = [None, 40, 60, 80, 50, 30, 70, 10, 20 ,90]

위 수도코드를 이 배열에 대해 힙 정렬이 수행되는 과정은 다음과 같다.

A[1] = 40과 A[heapSize] = 90을 swap하고 힙 크기를 1개 줄인다.

![https://user-images.githubusercontent.com/63987872/166850779-d45d56fe-1564-46ae-bdeb-73edf2d04165.png](https://user-images.githubusercontent.com/63987872/166850779-d45d56fe-1564-46ae-bdeb-73edf2d04165.png)

이 작업이 끝나면 최댓값은 80인데 루트노드에는 40이 올라가 있으므로 힙 조건이 위배된다. 위배되는 힙 조건을 만족시키기 위해 DownHeap를 수행한다.

![https://user-images.githubusercontent.com/63987872/166850780-0601283d-3ff5-4b0e-80f3-ea580a2fa28f.png](https://user-images.githubusercontent.com/63987872/166850780-0601283d-3ff5-4b0e-80f3-ea580a2fa28f.png)

DownHeap은 힙이 모두 만족할 때 까지 계속 수행한다.

![https://user-images.githubusercontent.com/63987872/166850783-2efdee86-27c2-4baa-9ba3-e89eb0e66faa.png](https://user-images.githubusercontent.com/63987872/166850783-2efdee86-27c2-4baa-9ba3-e89eb0e66faa.png)

힙 조건을 위배하지 않으므로 다시 이 전체 과정을 반복하여 큰 수를 오른쪽으로 옮기며 정렬을 수행한다.

힙의 크기가 1이 되면 힙 정렬을 마친다.

## 구현

[힙 정렬](heap_sort.py)
