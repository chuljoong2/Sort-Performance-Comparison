# 삽입 **정렬 (Insertion Sort)**

**`삽입 정렬`은 배열을 정렬된 부분(앞부분)과 정렬이 안 된 부분(뒷부분)으로 나누고, 정렬이 안 된 부분의 가장 왼쪽 원소를 정렬된 부분에서 적절한 위치에 삽입하여 정렬되도록 하는 과정을 반복하는 정렬 알고리즘**이다.

정렬이 안 된 부분의 숫자 하나가 정렬된 부분에 삽입되기 때문에 정렬된 부분의 원소 개수는 하나 증가하고 정렬이 안 된 부분의 원소 개수는 하나 줄어든다. 이를 반복하면 결국 마지막에는 정렬이 안 된 부분에 원소는 0개가 된다.

## 삽입 **정렬** 알고리즘

```
def insertion_sort(A):
	# 입력: 배열 A
	# 출력: 정렬된 배열 A
	n = len(A)
	for i = 1 to n - 1:
		CurrentElement = A[i]
		j = i - 1 # 정렬이 된 부분의 가장 오른쪽 원소(왼쪽으로 이동)
		while j >= 0 and A[j] > CurrentElement:
			A[j+1] = A[j]
			j -= 1 # (왼쪽으로 이동)
		A[j+1] = CurrentElement
	return A
```

아래와 같은 배열이 있다.

A = [40, 10, 50, 90, 20, 80, 30, 60]

위 수도코드를 이 배열에 대해 삽입 정렬이 수행되는 과정은 다음과 같다.

**[i = 1]**

![https://user-images.githubusercontent.com/63987872/166850746-caed0077-944d-46db-ba4e-eb2fbb61ce06.png](https://user-images.githubusercontent.com/63987872/166850746-caed0077-944d-46db-ba4e-eb2fbb61ce06.png)

i = 1일 때, A[j] = A[0] > CurrentElement = A[i] = 10이므로 A[j+1] = A[-1+1] = A[0]에 CurrentElement를 저장한다.

![https://user-images.githubusercontent.com/63987872/166850747-98b28996-d38b-4ba2-a4f4-fc3e30e40f82.png](https://user-images.githubusercontent.com/63987872/166850747-98b28996-d38b-4ba2-a4f4-fc3e30e40f82.png)

**[i = 2]**

i = 2일 때, A[j] = A[1] < CurrentElement = A[i] = 50이므로 while문의 조건문을 만족하지 않는다. 따라서 자리 이동은 없다.

**[i = 3]**

i = 3일 때, A[j] = A[2] < CurrentElement = A[i] = 90이므로 while문의 조건문을 만족하지 않는다. 따라서 자리 이동은 없다.

**[i = 4]**

i = 4일 때, A[j] = A[3] > CurrentElement = A[i] = 20이므로 j를 왼쪽으로 이동하여 CurrentElement가 정렬된 위치로 이동하도록 한다. 따라서 j = 0까지 즉, A[j+1] = A[1]에 CurrentElement를 저장한다.

![https://user-images.githubusercontent.com/63987872/166850749-aedccd9b-1867-4eab-a172-f57eb82d2581.png](https://user-images.githubusercontent.com/63987872/166850749-aedccd9b-1867-4eab-a172-f57eb82d2581.png)

**[i = 5] ~ [i = 7]**

나머지도 위 작업을 반복하면 정렬할 수 있다.

![https://user-images.githubusercontent.com/63987872/166850751-77ec2ab5-3669-4881-a9ed-68ea6a2d8473.png](https://user-images.githubusercontent.com/63987872/166850751-77ec2ab5-3669-4881-a9ed-68ea6a2d8473.png)

![https://user-images.githubusercontent.com/63987872/166850753-141f5fa2-4214-4de2-871a-a59b120c6c2e.png](https://user-images.githubusercontent.com/63987872/166850753-141f5fa2-4214-4de2-871a-a59b120c6c2e.png)

![https://user-images.githubusercontent.com/63987872/166850754-adab7ad7-aa4a-4fc9-8cc9-6a36e6b6363a.png](https://user-images.githubusercontent.com/63987872/166850754-adab7ad7-aa4a-4fc9-8cc9-6a36e6b6363a.png)

## 구현

[삽입 정렬](insertion_sort.py)
