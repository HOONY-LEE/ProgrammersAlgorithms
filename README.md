# ProgrammersAlgorithms

## 2023.09.27(수)

<br>
문자열 잘라서 정렬하기

```python
def solution(myString):
    answer = []
    tmp = myString.split('x')
    for i in tmp:
        if i != '':
            answer.append(i)
    answer.sort()
    return answer
```

<br>
문자열이 몇 번 등장하는지 세기

```python
def solution(myString, pat):
    answer = 0
    length = len(pat)
    for i in range(len(myString)):
        if myString[i:i+length] == pat:
            answer += 1
    return answer
```

## 2023.09.26(화)

<br>
빈 배열에 추가, 삭제하기

```python
def solution(arr, flag):
    answer = []
    for i in range(len(arr)):
        if flag[i]:
            for j in range(arr[i]*2):
                answer.append(arr[i])
        else:
            for j in range(arr[i]):
                answer.pop()
    return answer
```


## 2023.09.25(월)

<br>
조건에 맞게 수열 변환하기2

```python
def solution(arr):
    answer = 0
    while True:
        before = arr.copy()
        for i,value in enumerate(arr):
            if value>=50 and value%2==0:
                arr[i] = arr[i]/2
            elif value<50 and value%2==1:
                arr[i] = (arr[i]*2)+1    
        if before == arr:
            break
        answer += 1 
    return answer
```

## 2023.09.24(일)

<br>
A 강조하기

```python
def solution(myString):
    return myString.lower().replace('a','A')
```

<br>
배열에서 문자열 대소문자 변환하기

```python
def solution(strArr):
    answer = []
    for i, value in enumerate(strArr):
        if i%2==0:
            answer.append(value.lower())
        else:
            answer.append(value.upper())
    return answer
```


## 2023.09.23(토)

<br>
수열과 구간 쿼리1

```python
def solution(num_list):
    answer = 0
    for i in num_list:
        num = i
        while num!=1:
            if num%2==0:
                num = num/2
            else:
                num = (num-1)/2
            answer += 1
    return answer
```




## 2023.09.22(금)




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



## 2023.09.21(목)

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




## 2023.09.20(수)
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
n번째 원소부터
```python
def solution(num_list, n):
    return num_list[n-1:]
```


## 2023.09.19(화)
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


첫 번째로 나오는 음수
```python
def solution(num_list):
    for i in range(len(num_list)):
        if num_list[i] < 0:
            return i
    return -1
```
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


## 2023.09.09(토)
1일 1알고리즘 16일차, 하루에 쉬운문제 하나라도 풀어보자. 일단은 가장 익숙한 Python으로 풀어보기

## 2023.09.10(일)
매일매일 조금씩!


## 2023.09.11(월)
아직까지는 쉬운 문제들 위주이지만 확실히 알고리즘적 사고방식이 프로그래밍에 장기적으로 큰 도움이 될 것 같다는 생각이 든다.

## 2023.09.12(화)
문제 푸는 시간도 조금씩 단축된다. 언제 고난이도 문제를 풀 수 있게 될까?

## 2023.09.13(수)
 string문제 그만 풀고싶다.

## 2023.09.14(목)
기초가 많이 부족하다.. cs 공부 및 자료구조 공부 더 해야겠다.
 
