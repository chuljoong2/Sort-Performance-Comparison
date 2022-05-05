# 퀵 정렬 (Quick Sort)

**`퀵 정렬`은 입력이 2개의 부분 문제로 분할되고, 부분 문제의 크기가 일정하지 않은 형태의 분할 정복 알고리즘을 사용하는 정렬 방법**이다.

퀵 정렬의 아이디어는 피봇(pivot)이라 일컫는 배열의 원소를 기준으로 피봇보다 작은 숫자들은 왼쪽으로 큰 숫자들은 오른쪽으로 위치하도록 분할하고 피봇을 그사이에 놓는 것이다.

다음은 퀵 정렬을 통하여 정렬한 하나의 예시이다.

![https://user-images.githubusercontent.com/63987872/166850777-8a195594-3946-4803-8f92-7d8d11064c81.png](https://user-images.githubusercontent.com/63987872/166850777-8a195594-3946-4803-8f92-7d8d11064c81.png)

## 퀵 정렬 알고리즘

```
def quick_sort(A, left, right):
	# 입력: 배열 A[left]~A[right]
	# 출력: 정렬된 배열 A[left]~A[right]
	if left < right:
		피봇 A[left]~A[right] 선택
		피봇을 A[left]와 자리 바꿈. 만약 A[left]가 피봇이라면 내버려둠
		피봇보다 작은 숫자들은 A[left]~A[p-1]에 위치
		피봇보다 큰 숫자들은 A[p+1]~A[right]에 위치
		피봇은 A[p]에 위치
		quick_sort(A, left, p-1)
		quick_sort(A, p+1, right)
```

이와 같은 수도코드를 위 이미지의 배열을 적용하여 수행 동작을 살펴보면 다음과 같다.

초기 상태의 배열에서 left는 0이고 right는 8이다. 피봇을 A[0]인 5를 선택한다. 피봇을 A[left]와 자리를 바꾸는데 이 경우에는 피봇과 A[left]가 일치하는 경우이므로 내버려 둔다. 피봇과 배열의 각 원소와 비교를 하여 자리를 옮긴 뒤 피봇의 위치를 A[p]로 옮긴다.

피봇을 기준으로 자리를 옮기는 과정은 아래와 같다.

![https://user-images.githubusercontent.com/63987872/166850771-1befac6c-c9bc-477d-adfa-9e3093f629d6.png](https://user-images.githubusercontent.com/63987872/166850771-1befac6c-c9bc-477d-adfa-9e3093f629d6.png)

2개의 인덱스가 A[left+1], A[right]에서 각각 출발하여 비교를 진행한다.

왼쪽에서 출발하는 인덱스는 가리키는 숫자가 피봇보다 작으면 정지하고, 오른쪽에서 출발하는 인덱스는 가리키는 숫자가 피봇보다 크면 정지한다. 양쪽 인덱스가 모두 정지하면 교환한다. 교환하고 난 뒤, 인덱스는 다시 오른쪽에서 왼쪽으로 왼쪽에서 오른쪽으로 이동하면서 반복한다.

이 작업은 두 인덱스가 엇갈려서 지나면 STOP한다. STOP하고 나서 피봇의 위치를 가운데로 옮긴다.

위 작업을 시행하고 나면 피봇을 기준으로 왼쪽 부분 배열과 오른쪽 부분 배열이 생긴다. 각 배열에 대해서도 이 작업을 반복하고 배열의 원소가 하나 남을 때까지 계속한다.

![https://user-images.githubusercontent.com/63987872/166850776-b3795c70-df83-46e8-ab2f-e4085254098b.png](https://user-images.githubusercontent.com/63987872/166850776-b3795c70-df83-46e8-ab2f-e4085254098b.png)

## 구현

[퀵 정렬](quick_sort.py)
