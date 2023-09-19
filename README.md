# ProgrammersAlgorithms

#2023.09.15(화)

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
 
