# ProgrammersAlgorithms

#2023.09.18(금)


<br>
문제를 입력하세요
```python

```
<br>

<br>
수열과 구간 쿼리1
```python
def solution(arr, queries):
    for i in range(len(queries)):
        s, e = queries[i][0], queries[i][1]
        for j in range(s, e+1):
            arr[j] += 1
    return arr
```
<br>


#2023.09.17(목)
<br>
왼쪽 오른쪽
```python
def solution(str_list):
    for index, value in enumerate(str_list):
        if value == 'l':
            
            return str_list[:index]
        elif value == 'r':
            return str_list[index+1:]
    return []
```
<br>

배열조각하기
```python
def solution(arr, query):
    answer = []
    for i in range(len(query)):
        if i%2 == 0:
            arr = arr[:query[i]+1]
        else:
            arr = arr[query[i]:]
    return arr
```
=> index와 각 요소들을 for문을 통해서 꺼낼때 파이썬의 내장함수 enumerate()를 사용하면 편하다.
for i, item in enumerate(arr):
    print(i, item)
의 형태로 사용할 수 있다.
<br>

<br>
2의 영역
```python
def solution(arr):
    arr2 = list(reversed(arr))
    leng = len(arr)
    si = 0;
    ei = leng
    
    if not(2 in arr):
        return [-1]
    for i in range(leng):
        if arr[i] == 2:
            si = i
            break    
    for i in range(leng):      
        if arr2[i] == 2:
            ei = leng - i
            break
    return arr[si:ei]
```
<br>


#2023.09.16(수)
<br>
조건에 맞게 수열 변환하기3
```python
def solution(arr, k):
    if k%2:
        for i in range(len(arr)):
            arr[i] *= k
    else:
        for i in range(len(arr)):
            arr[i] += k
    return arr
```
<br>

<br>
n번째 원소부터
```python
def solution(num_list, n):
    return num_list[n-1:]
```
<br>


#2023.09.15(화)
<br>
길이에 따른 연산
```python
def solution(num_list):
    answer = 0
    n = len(num_list)
    if n >= 11:
        for i in num_list:
            answer += i
    elif n <= 10:
        answer = 1
        for i in num_list:
            answer *= i
    return answer
```
=> 누적합이나 누적곱을 구할때는 sum(), prod()를 사용하면 편하다.
prod() 는 math 모듈을 임포트해야한다.
<br>

<br>
첫 번째로 나오는 음수
```python
def solution(num_list):
    for i in range(len(num_list)):
        if num_list[i] < 0:
            return i
    return -1
```
<br>

<br>
리스트 자르기
```python
def solution(n, slicer, num_list):
    answer = []
    a, b, c = slicer[0], slicer[1], slicer[2]

    if n==1:
        answer = num_list[:b+1]
    elif n==2:
        answer = num_list[a:]
    elif n==3:
        answer = num_list[a:b+1]
    elif n==4:
        answer = num_list[a:b+1:c]
    return answer
```
=> 파이썬에서 배열에 있는 값(ITERABLE)을 변수에 담을 때는 편하게 a, b, c = slicer(배열) 이렇게 넣어줄 수 있다는걸 몰랐다.
자바스크립트 스프레드문법이랑 비슷한 것 같다.  
<br>


#2023.09.09(토)
1일 1알고리즘 16일차, 하루에 쉬운문제 하나라도 풀어보자. 일단은 가장 익숙한 Python으로 풀어보기

#2023.09.10(일)
매일매일 조금씩!


#2023.09.11(월)
아직까지는 쉬운 문제들 위주이지만 확실히 알고리즘적 사고방식이 프로그래밍에 장기적으로 큰 도움이 될 것 같다는 생각이 든다.

#2023.09.12(화)
문제 푸는 시간도 조금씩 단축된다. 언제 고난이도 문제를 풀 수 있게 될까?

#2023.09.13(수)
 string문제 그만 풀고싶다.

#2023.09.14(목)
기초가 많이 부족하다.. cs 공부 및 자료구조 공부 더 해야겠다.
 
