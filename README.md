                                                                                                                                                                                                                                                    
# ProgrammersAlgorithms                                                     
##2026.04.17(금)

<br>.
**유일한 원소 찾기**
정수 배열에서 딱 한 번만 등장하는 원소를 반환하시오. 나머지 원소는 모두 두 번씩 등장합니다.
XOR 비트 연산을 활용하면 O(n) 시간, O(1) 공간으로 풀 수 있습니다.
입력: nums = [4,1,2,1,2] → 출력: 4
<br>.

```python
def single_number(nums):
    result = 0
    for n in nums:
        result ^= n
    return result
```

##2026.04.16(목)

<br>.
**배열 회전**
정수 배열 nums를 오른쪽으로 k번 회전시키시오. in-place로 구현해야 합니다.
뒤집기(reverse) 세 번으로 O(n) 시간, O(1) 공간에 해결할 수 있습니다.
입력: nums = [1,2,3,4,5,6,7], k = 3 → 출력: [5,6,7,1,2,3,4]
<br>.

```python
def rotate(nums, k):
    n = len(nums)
    k %= n
    nums.reverse()
    nums[:k] = nums[:k][::-1]
    nums[k:] = nums[k:][::-1]
```

##2026.04.15(수)

<br>.
**행렬 나선형 순회**
m×n 행렬이 주어질 때, 나선형(spiral) 순서로 모든 원소를 반환하시오.
경계를 좁혀가며 순회하는 방식으로 구현합니다.
입력: [[1,2,3],[4,5,6],[7,8,9]] → 출력: [1,2,3,6,9,8,7,4,5]
<br>.

```python
def spiral_order(matrix):
    result = []
    while matrix:
        result += matrix.pop(0)
        matrix = list(zip(*matrix))[::-1]
    return result
```

##2026.04.14(화)

<br>.
**중복 없는 가장 긴 부분 문자열**
문자열 s가 주어질 때, 중복 문자가 없는 가장 긴 부분 문자열의 길이를 구하시오.
슬라이딩 윈도우 기법을 활용하면 효율적으로 풀 수 있습니다.
입력: s = 'abcabcbb' → 출력: 3 ('abc')
<br>.

```python
def length_of_longest_substring(s):
    char_set = set()
    left = 0
    max_len = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len
```

##2026.04.13(월)

<br>.
**이진 탐색**
오름차순으로 정렬된 정수 배열 nums에서 target의 인덱스를 반환하시오. 없으면 -1을 반환합니다.
반드시 O(log n) 시간복잡도로 구현하시오.
입력: nums = [-1,0,3,5,9,12], target = 9 → 출력: 4
<br>.

```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

##2026.04.12(일)

<br>.
**행렬 90도 회전**
n×n 정수 행렬이 주어질 때, in-place로 시계 방향 90도 회전시키시오.
전치(transpose) 후 각 행을 뒤집는 방식으로 구현할 수 있습니다.
입력: [[1,2,3],[4,5,6],[7,8,9]] → 출력: [[7,4,1],[8,5,2],[9,6,3]]
<br>.

```python
def rotate(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
```

##2026.04.11(토)

<br>.
**배열 회전**
정수 배열 nums를 오른쪽으로 k번 회전시키시오. in-place로 구현해야 합니다.
뒤집기(reverse) 세 번으로 O(n) 시간, O(1) 공간에 해결할 수 있습니다.
입력: nums = [1,2,3,4,5,6,7], k = 3 → 출력: [5,6,7,1,2,3,4]
<br>.

```python
def rotate(nums, k):
    n = len(nums)
    k %= n
    nums.reverse()
    nums[:k] = nums[:k][::-1]
    nums[k:] = nums[k:][::-1]
```

##2026.04.10(금)

<br>.
**소수 판별**
주어진 정수 n이 소수인지 판별하는 함수를 작성하시오.
에라토스테네스의 체 원리를 응용하여 O(√n) 시간 내에 풀 수 있습니다.
입력: n = 17 → 출력: True
<br>.

```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

##2026.04.09(목)

<br>.
**아나그램 그룹화**
문자열 배열이 주어질 때, 아나그램끼리 같은 그룹으로 묶어 반환하시오.
아나그램이란 문자의 순서를 바꿔 다른 단어를 만들 수 있는 단어들의 관계입니다.
입력: strs = ['eat','tea','tan','ate','nat','bat'] → 출력: [['eat','tea','ate'],['tan','nat'],['bat']]
<br>.

```python
from collections import defaultdict
def group_anagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        groups[tuple(sorted(s))].append(s)
    return list(groups.values())
```

##2026.04.08(수)

<br>.
**연속 부분 배열의 최대 합 (카데인 알고리즘)**
정수 배열에서 연속된 부분 배열의 합이 최대가 되는 값을 반환하시오.
카데인(Kadane) 알고리즘을 사용하면 O(n)에 해결할 수 있습니다.
입력: nums = [-2,1,-3,4,-1,2,1,-5,4] → 출력: 6
<br>.

```python
def max_subarray(nums):
    max_sum = curr = nums[0]
    for n in nums[1:]:
        curr = max(n, curr + n)
        max_sum = max(max_sum, curr)
    return max_sum
```

##2026.04.07(화)

<br>.
**주식 최대 이익**
주가 배열 prices가 주어질 때, 한 번 사고 팔아서 얻을 수 있는 최대 이익을 반환하시오.
이익이 없으면 0을 반환합니다. 반드시 사는 날이 파는 날보다 앞서야 합니다.
입력: prices = [7,1,5,3,6,4] → 출력: 5
<br>.

```python
def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    for p in prices:
        min_price = min(min_price, p)
        max_profit = max(max_profit, p - min_price)
    return max_profit
```

##2026.04.06(월)

<br>.
**배열의 최댓값 인덱스**
정수 배열에서 최댓값이 처음 등장하는 인덱스를 반환하시오.
배열은 비어있지 않으며 정수로만 구성됩니다.
입력: nums = [3, 1, 4, 1, 5, 9, 2, 6] → 출력: 5
<br>.

```python
def max_index(nums):
    return nums.index(max(nums))
```

##2026.04.05(일)

<br>.
**문자열 압축**
문자열에서 연속된 같은 문자를 '문자+개수' 형태로 압축하시오. 압축 결과가 원본보다 길면 원본을 반환합니다.
입력: s = 'aabcccccaaa' → 출력: 'a2b1c5a3'
입력: s = 'abcde' → 출력: 'abcde' (압축이 더 길어서)
<br>.

```python
def compress(s):
    result = ''
    i = 0
    while i < len(s):
        count = 1
        while i + count < len(s) and s[i + count] == s[i]:
            count += 1
        result += s[i] + str(count)
        i += count
    return result if len(result) < len(s) else s
```

##2026.04.04(토)

<br>.
**문자열 뒤집기**
문자 배열 s가 주어질 때, 배열을 in-place로 뒤집으시오. 추가 메모리를 O(1)만 사용해야 합니다.
투 포인터 방식으로 구현하시오.
입력: s = ['h','e','l','l','o'] → 출력: ['o','l','l','e','h']
<br>.

```python
def reverse_string(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s
```

##2026.04.03(금)

<br>.
**문자열 압축**
문자열에서 연속된 같은 문자를 '문자+개수' 형태로 압축하시오. 압축 결과가 원본보다 길면 원본을 반환합니다.
입력: s = 'aabcccccaaa' → 출력: 'a2b1c5a3'
입력: s = 'abcde' → 출력: 'abcde' (압축이 더 길어서)
<br>.

```python
def compress(s):
    result = ''
    i = 0
    while i < len(s):
        count = 1
        while i + count < len(s) and s[i + count] == s[i]:
            count += 1
        result += s[i] + str(count)
        i += count
    return result if len(result) < len(s) else s
```

##2026.04.02(목)

<br>.
**배열의 최댓값 인덱스**
정수 배열에서 최댓값이 처음 등장하는 인덱스를 반환하시오.
배열은 비어있지 않으며 정수로만 구성됩니다.
입력: nums = [3, 1, 4, 1, 5, 9, 2, 6] → 출력: 5
<br>.

```python
def max_index(nums):
    return nums.index(max(nums))
```

##2026.04.01(수)

<br>.
**행렬 90도 회전**
n×n 정수 행렬이 주어질 때, in-place로 시계 방향 90도 회전시키시오.
전치(transpose) 후 각 행을 뒤집는 방식으로 구현할 수 있습니다.
입력: [[1,2,3],[4,5,6],[7,8,9]] → 출력: [[7,4,1],[8,5,2],[9,6,3]]
<br>.

```python
def rotate(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
```

##2026.03.31(화)

<br>.
**단어 빈도 카운트**
문자열 배열 words가 주어질 때, 각 단어의 등장 횟수를 딕셔너리로 반환하시오.
대소문자를 구분하지 않으며, 결과는 빈도 내림차순으로 정렬하시오.
입력: words = ['apple','banana','apple','cherry','banana','apple'] → 출력: {'apple':3,'banana':2,'cherry':1}
<br>.

```python
from collections import Counter
def word_count(words):
    return dict(Counter(w.lower() for w in words).most_common())
```

##2026.03.30(월)

<br>.
**배열 회전**
정수 배열 nums를 오른쪽으로 k번 회전시키시오. in-place로 구현해야 합니다.
뒤집기(reverse) 세 번으로 O(n) 시간, O(1) 공간에 해결할 수 있습니다.
입력: nums = [1,2,3,4,5,6,7], k = 3 → 출력: [5,6,7,1,2,3,4]
<br>.

```python
def rotate(nums, k):
    n = len(nums)
    k %= n
    nums.reverse()
    nums[:k] = nums[:k][::-1]
    nums[k:] = nums[k:][::-1]
```

##2026.03.29(일)

<br>.
**숫자 뒤집기**
32비트 부호 있는 정수 x를 뒤집으시오. 뒤집은 결과가 32비트 범위를 벗어나면 0을 반환합니다.
문자열 변환 없이 수학적으로 구현하는 방법도 있습니다.
입력: x = 123 → 출력: 321 / x = -123 → 출력: -321
<br>.

```python
def reverse_int(x):
    sign = -1 if x < 0 else 1
    x = int(str(abs(x))[::-1]) * sign
    return x if -(2**31) <= x <= 2**31 - 1 else 0
```

##2026.03.28(토)

<br>.
**오름차순 정렬된 배열에서 중복 제거**
오름차순 정렬된 배열에서 중복을 in-place로 제거하고, 고유한 원소의 개수를 반환하시오.
추가 메모리를 사용하지 않고 투 포인터로 구현하시오.
입력: nums = [0,0,1,1,1,2,2,3,3,4] → 출력: 5 (nums = [0,1,2,3,4,...])
<br>.

```python
def remove_duplicates(nums):
    if not nums:
        return 0
    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[k] = nums[i]
            k += 1
    return k
```

##2026.03.27(금)

<br>.
**유효한 스도쿠**
9×9 스도쿠 보드가 주어질 때, 현재 채워진 숫자들이 규칙에 유효한지 판별하시오.
각 행, 열, 3×3 박스에 1~9가 중복 없이 있어야 합니다. '.'은 빈 칸입니다.
같은 행/열/박스에 같은 숫자가 있으면 False를 반환하시오.
<br>.

```python
def is_valid_sudoku(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    for i in range(9):
        for j in range(9):
            val = board[i][j]
            if val == '.':
                continue
            box_idx = (i // 3) * 3 + j // 3
            if val in rows[i] or val in cols[j] or val in boxes[box_idx]:
                return False
            rows[i].add(val)
            cols[j].add(val)
            boxes[box_idx].add(val)
    return True
```

##2026.03.26(목)

<br>.
**숫자를 로마 숫자로 변환**
1~3999 사이의 정수를 로마 숫자 문자열로 변환하는 함수를 작성하시오.
로마 숫자: I=1, V=5, X=10, L=50, C=100, D=500, M=1000
입력: num = 1994 → 출력: 'MCMXCIV'
<br>.

```python
def int_to_roman(num):
    vals = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    syms = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
    result = ''
    for v, s in zip(vals, syms):
        while num >= v:
            result += s
            num -= v
    return result
```

##2026.03.25(수)

<br>.
**주식 최대 이익**
주가 배열 prices가 주어질 때, 한 번 사고 팔아서 얻을 수 있는 최대 이익을 반환하시오.
이익이 없으면 0을 반환합니다. 반드시 사는 날이 파는 날보다 앞서야 합니다.
입력: prices = [7,1,5,3,6,4] → 출력: 5
<br>.

```python
def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    for p in prices:
        min_price = min(min_price, p)
        max_profit = max(max_profit, p - min_price)
    return max_profit
```

##2026.03.25(수)

<br>.
**주식 최대 이익**
주가 배열 prices가 주어질 때, 한 번 사고 팔아서 얻을 수 있는 최대 이익을 반환하시오.
이익이 없으면 0을 반환합니다. 반드시 사는 날이 파는 날보다 앞서야 합니다.
입력: prices = [7,1,5,3,6,4] → 출력: 5
<br>.

```python
def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    for p in prices:
        min_price = min(min_price, p)
        max_profit = max(max_profit, p - min_price)
    return max_profit
```

##2026.03.24(화)

<br>.
**배열 회전**
정수 배열 nums를 오른쪽으로 k번 회전시키시오. in-place로 구현해야 합니다.
뒤집기(reverse) 세 번으로 O(n) 시간, O(1) 공간에 해결할 수 있습니다.
입력: nums = [1,2,3,4,5,6,7], k = 3 → 출력: [5,6,7,1,2,3,4]
<br>.

```python
def rotate(nums, k):
    n = len(nums)
    k %= n
    nums.reverse()
    nums[:k] = nums[:k][::-1]
    nums[k:] = nums[k:][::-1]
```

##2026.03.23(월)

<br>.
**숫자를 로마 숫자로 변환**
1~3999 사이의 정수를 로마 숫자 문자열로 변환하는 함수를 작성하시오.
로마 숫자: I=1, V=5, X=10, L=50, C=100, D=500, M=1000
입력: num = 1994 → 출력: 'MCMXCIV'
<br>.

```python
def int_to_roman(num):
    vals = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    syms = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
    result = ''
    for v, s in zip(vals, syms):
        while num >= v:
            result += s
            num -= v
    return result
```

##2026.03.22(일)

<br>.
**배열 회전**
정수 배열 nums를 오른쪽으로 k번 회전시키시오. in-place로 구현해야 합니다.
뒤집기(reverse) 세 번으로 O(n) 시간, O(1) 공간에 해결할 수 있습니다.
입력: nums = [1,2,3,4,5,6,7], k = 3 → 출력: [5,6,7,1,2,3,4]
<br>.

```python
def rotate(nums, k):
    n = len(nums)
    k %= n
    nums.reverse()
    nums[:k] = nums[:k][::-1]
    nums[k:] = nums[k:][::-1]
```

##2026.03.22(일)

<br>.
**배열 회전**
정수 배열 nums를 오른쪽으로 k번 회전시키시오. in-place로 구현해야 합니다.
뒤집기(reverse) 세 번으로 O(n) 시간, O(1) 공간에 해결할 수 있습니다.
입력: nums = [1,2,3,4,5,6,7], k = 3 → 출력: [5,6,7,1,2,3,4]
<br>.

```python
def rotate(nums, k):
    n = len(nums)
    k %= n
    nums.reverse()
    nums[:k] = nums[:k][::-1]
    nums[k:] = nums[k:][::-1]
```

##2026.03.21(토)

<br>.
**두 수의 합**
정수 배열 nums와 목표값 target이 주어질 때, 합이 target이 되는 두 원소의 인덱스를 반환하시오.
각 입력에는 정확히 하나의 답이 존재하며, 같은 원소를 두 번 사용할 수 없습니다.
입력: nums = [2, 7, 11, 15], target = 9 → 출력: [0, 1]
<br>.

```python
def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        if target - n in seen:
            return [seen[target - n], i]
        seen[n] = i
```

                                                                                                                                                                                                     
                                                        
##2025.06.25(수)                                                                                                   
                                                                                                                    
<br>.                                          
문자열 s가 주어질 때, 중복 문자가 없는 가장 긴 부분 문자열의 길이를 구하시오.               
<br>. 
                         
```python
def lengthOfLongestSubstring(s):        
    char_set = set()
    left = 0 
    max_len = 0. 
      
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)    
    
    return max_len
```
               
    
## 2025.06.11(수)       
             
<br>        
문자열 s가 주어질 때, 중복 문자가 없는 가장 긴 부분 문자열의 길이를 구하시오. 
<br>
     
```python
def lengthOfLongestSubstring(s):
    char_set = set()
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    
    return max_len
```

  
## 2025.06.09(월)     
         
<br>      
델타 순회
<br>
     
```python
def solution(grid):
    def dfs(x, y):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == '0':
            return
        grid[x][y] = '0'
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            dfs(x+dx, y+dy)
    
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1
    return count
```


               
## 2025.05.25(일)       
                   
<br>  
n개의 컴퓨터가 있고 computers[i][j] == 1이면 i번 컴퓨터와 j번 컴퓨터가 직접 연결되어 있다. 네트워크(서로 연결된 컴퓨터들)의 개수를 구하시오.
<br>
     
```python
def solution(n, computers):
    visited = [False] * n  
    
    def dfs(x):
        visited[x] = True
        for i in range(n):
            if computers[x][i] == 1 and not visited[i]:
                dfs(i)
    
    count = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            count += 1
    return count


```
    
                
## 2025.05.14(수)       
         
<br>
주식을 사고팔기 가장 좋은 시점** 정수 배열 `prices`가 주어질 때, 하루에 한 주씩 사고팔 수 있다고 했을 때, 가장 큰 이익을 반환하세요. (단, 반드시 사고 나서 팔아야 함)
<br>
     
```python   
def solution(prices):
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    
    return max_profit

```

       
## 2025.04.28(월)             
                     
<br>          
문자열 s가 주어질 때, 중복 문자가 없는 가장 긴 부분 문자열의 길이를 구하시오. 
<br>
            
```python
def lengthOfLongestSubstring(s):
    char_set = set()
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    
    return max_len
```   
  

## 2025.04.26(토)   
 
<br>
섬의 개수 (DFS/BFS)
2차원 배열 grid가 주어질 때, 1은 육지, 0은 바다를 의미한다. 상하좌우로 연결된 육지 덩어리의 개수를 구하시오.
<br>
     
```python
def numIslands(grid):
    if not grid:
        return 0
    
    n, m = len(grid), len(grid[0])
    visited = [[False]*m for _ in range(n)]
    
    def dfs(x, y):
        if x < 0 or x >= n or y < 0 or y >= m or visited[x][y] or grid[x][y] == '0':
            return
        visited[x][y] = True
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            dfs(x + dx, y + dy)
    
    count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '1' and not visited[i][j]:
                dfs(i, j)
                count += 1
    return count

```




## 2025.04.25(금) 
 
<br>
가장 긴 팰린드롬 부분 문자열** 문자열 `s`가 주어졌을 때, `s`의 부분 문자열 중 가장 긴 팰린드롬을 구하세요. 예시 입력: `"babad"` → 출력: `"bab"` 또는 `"aba"`
<br>
     
```python
def solution(s):
    n = len(s)
    result = ""
    
    for i in range(n):
        for j in range(i, n):
            substr = s[i:j+1]
            if substr == substr[::-1] and len(substr) > len(result):
                result = substr
    return result

```


## 2025.04.23(수)

<br>
두 배열의 합** 정수 배열 `A`, `B`가 주어질 때, `A`에서 하나, `B`에서 하나를 골라 만들 수 있는 두 수의 합 중에서 특정 정수 `X`를 만들 수 있는 경우의 수를 구하세요. (각 배열의 길이는 최대 1,000)
<br>
     
```python
from collections import Counter

def solution(A, B, X):
    count = 0
    counter_B = Counter(B)
    
    for a in A:
        if (X - a) in counter_B:
            count += counter_B[X - a]
    
    return count
```


## 2025.04.22(화)

<br>
섬의 개수** 2차원 배열 `grid`가 주어질 때, '1'은 땅, '0'은 물입니다. 섬은 상하좌우로 연결된 땅들로 이루어져 있습니다. 섬의 개수를 구하세요.
<br>
     
```python
def solution(grid):
    def dfs(x, y):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == '0':
            return
        grid[x][y] = '0'
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            dfs(x+dx, y+dy)
    
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1
    return count

```


## 2025.04.20(일)

<br>
주식을 사고팔기 가장 좋은 시점** 정수 배열 `prices`가 주어질 때, 하루에 한 주씩 사고팔 수 있다고 했을 때, 가장 큰 이익을 반환하세요. (단, 반드시 사고 나서 팔아야 함)
<br>
     
```python
def solution(prices):
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    
    return max_profit

```

## 2025.04.19(토)

<br>
이진 트리의 최대 깊이** 이진 트리를 나타내는 `TreeNode`가 주어졌을 때, 그 트리의 최대 깊이를 반환하세요.
<br>
     
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solution(root):
    if not root:
        return 0
    return 1 + max(solution(root.left), solution(root.right))

```



## 2025.04.16(수)

<br>
두 배열의 합** 정수 배열 `A`, `B`가 주어질 때, `A`에서 하나, `B`에서 하나를 골라 만들 수 있는 두 수의 합 중에서 특정 정수 `X`를 만들 수 있는 경우의 수를 구하세요. (각 배열의 길이는 최대 1,000)
<br>
     
```python
from collections import Counter

def solution(A, B, X):
    count = 0
    counter_B = Counter(B)
    
    for a in A:
        if (X - a) in counter_B:
            count += counter_B[X - a]
    
    return count
```
  
   
## 2025.04.15(화)     
             
<br>        
빈 배열 추가하기    
<br>       

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

        
## 2025.04.14(월)     
             
<br>
두 배열의 합** 정수 배열 `A`, `B`가 주어질 때, `A`에서 하나, `B`에서 하나를 골라 만들 수 있는 두 수의 합 중에서 특정 정수 `X`를 만들 수 있는 경우의 수를 구하세요. (각 배열의 길이는 최대 1,000)
<br>
     
```python
from collections import Counter

def solution(A, B, X):
    count = 0
    counter_B = Counter(B)
    
    for a in A:
        if (X - a) in counter_B:
            count += counter_B[X - a]
    
    return count
```

          
        
## 2025.04.13(금)     
             
<br>
이진 트리의 최대 깊이** 이진 트리를 나타내는 `TreeNode`가 주어졌을 때, 그 트리의 최대 깊이를 반환하세요.
<br>
     
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solution(root):
    if not root:
        return 0
    return 1 + max(solution(root.left), solution(root.right))

```
  
     
## 2025.04.11(금)     
             
<br>        
카페 자동화 키오스크   
<br>

```python
def solution(order):
    answer = 0
    # 1. 차가운것 뜨거운것 상관 없이 아메리카노인지 카페라떼인지 중요
    # 2. anything -> 아메리카노
    #    americano in -> 아메리카노
    #    cafelatte in -> 라떼

    for item in order:
        if 'americano' in item:
            answer += 4500
        elif 'cafelatte' in item:
            answer += 5000
        elif 'anything' in item:
            answer += 4500
    return answer
```
                   
           
## 2025.03.25(화)     
             
<br>
n개의 컴퓨터가 있고 computers[i][j] == 1이면 i번 컴퓨터와 j번 컴퓨터가 직접 연결되어 있다. 네트워크(서로 연결된 컴퓨터들)의 개수를 구하시오.
<br>
     
```python
def solution(n, computers):
    visited = [False] * n
    
    def dfs(x):
        visited[x] = True
        for i in range(n):
            if computers[x][i] == 1 and not visited[i]:
                dfs(i)
    
    count = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            count += 1
    return count


```
   
      
        
     
## 2025.03.22(토)     
         
<br>      
날짜 비교하기

<br>    

```python
def solution(date1, date2):
    
    if date1[0] > date2[0]:
        return 0
    elif date1[0] < date2[0]:
        return 1
    elif date1[0] == date2[0]:
        if date1[1] > date2[1]:
            return 0
        elif date1[1] < date2[1]:
            return 1
        elif date1[1] == date2[1]:
            if date1[2] > date2[2]:
                return 0
            elif date1[2] < date2[2]:
                return 1
            elif date1[2] == date2[2]:
                return 0
```

    
        
     
## 2025.03.13(목)     
         
<br>
섬의 개수** 2차원 배열 `grid`가 주어질 때, '1'은 땅, '0'은 물입니다. 섬은 상하좌우로 연결된 땅들로 이루어져 있습니다. 섬의 개수를 구하세요.
<br>
     
```python
def solution(grid):
    def dfs(x, y):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == '0':
            return
        grid[x][y] = '0'
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            dfs(x+dx, y+dy)
    
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1
    return count

```

      
     
## 2025.03.12(수)     
         
<br>
주식을 사고팔기 가장 좋은 시점** 정수 배열 `prices`가 주어질 때, 하루에 한 주씩 사고팔 수 있다고 했을 때, 가장 큰 이익을 반환하세요. (단, 반드시 사고 나서 팔아야 함)
<br>
     
```python
def solution(prices):
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    
    return max_profit

```


   
## 2025.03.09(화)     
         
<br>      
노드 개수 n, 간선 리스트 edges, 시작 노드 start가 주어질 때, 각 노드까지의 최단 거리를 리스트로 반환하시오.
<br>

     
```python
import heapq

def dijkstra(n, edges, start):
    graph = [[] for _ in range(n + 1)]
    for u, v, w in edges:
        graph[u].append((v, w))
    
    distance = [float('inf')] * (n + 1)
    distance[start] = 0
    heap = [(0, start)]
    
    while heap:
        dist, now = heapq.heappop(heap)
        if dist > distance[now]:
            continue
        for neighbor, cost in graph[now]:
            if distance[neighbor] > dist + cost:
                distance[neighbor] = dist + cost
                heapq.heappush(heap, (dist + cost, neighbor))
    
    return distance[1:]  # 0번 노드는 무시

```


  
## 2025.03.09(일)     
         
<br>      
문자열 s가 주어질 때, 중복 문자가 없는 가장 긴 부분 문자열의 길이를 구하시오. 
<br>
     
```python
def lengthOfLongestSubstring(s):
    char_set = set()
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    
    return max_len
```

  
## 2025.03.08(토)     
         
<br>      
델타 순회
<br>
     
```python
def solution(grid):
    def dfs(x, y):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == '0':
            return
        grid[x][y] = '0'
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            dfs(x+dx, y+dy)
    
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1
    return count
```

  
## 2025.03.06(금)     
         
<br>      
짝짓기  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```

  
## 2025.03.04(수)     
         
<br>      
Date 함수  
     
```python
def solution(date1, date2):
    
    if date1[0] > date2[0]:
        return 0
    elif date1[0] < date2[0]:
        return 1
    elif date1[0] == date2[0]:
        if date1[1] > date2[1]:
            return 0
        elif date1[1] < date2[1]:
            return 1
        elif date1[1] == date2[1]:
            if date1[2] > date2[2]:
                return 0
            elif date1[2] < date2[2]:
                return 1
            elif date1[2] == date2[2]:
                return 0
```



## 2025.03.03(화)     
         
<br>      
무작위로 K개 수 추첨 
     
```python
def solution(arr, k):
    answer = []
    leng = len(arr)

    for i in range(leng):
        if i == 0:
            answer.append(arr[i])
        else:
            flag = True
            for j in range(len(answer)):
                if arr[i] == answer[j]:
                    print('같은값 : ', arr[i])
                    flag = False
                    break
            if flag:
                answer.append(arr[i])
        if len(answer) == k:
            break
    if len(answer) < k:
        for i in range(k-len(answer)):
            answer.append(-1)
    return answer
```


## 2025.03.03(월)     
         
<br>      
그리드1  
     
```python
def solution(grid):
    def dfs(x, y):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == '0':
            return
        grid[x][y] = '0'
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            dfs(x+dx, y+dy)
    
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1
    return count
```

 


## 2025.03.02(일)     
         
<br>      
범위 찾기 
     
```python
def solution(grid):
    def dfs(x, y):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == '0':
            return
        grid[x][y] = '0'
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            dfs(x+dx, y+dy)
    
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1
    return count
```



## 2025.03.01(토)     
         
<br>      
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```


## 2025.02.28(금)     
         
<br>      
순서쌍2  
     
```python
def solution(s):
    n = len(s)
    result = ""
    
    for i in range(n):
        for j in range(i, n):
            substr = s[i:j+1]
            if substr == substr[::-1] and len(substr) > len(result):
                result = substr
    return result
```




## 2025.02.27(목)     
         
<br>      
순서쌍2  
     
```python
def solution(grid):
    def dfs(x, y):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == '0':
            return
        grid[x][y] = '0'
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            dfs(x+dx, y+dy)
    
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1
    return count
```

 

## 2025.02.26(수)     
         
<br>      
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```



## 2025.02.25(화)     
         
<br>      
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```



## 2025.02.24(월)     
         
<br>      
순서쌍2  
     
```python
def solution(n):
    arr = [[0 for _ in range(n)] for _ in range(n)]
    x = 0
    y = 0
    num = 1
    delta = 0
    direction = [[0,1],[1,0],[0,-1],[-1,0]]
    print(arr[x][y])
    for _ in range(n*n):
        arr[x][y] = num
        nextX = x + direction[delta][0]
        nextY = y + direction[delta][1]
        if nextX >= n or nextY >= n or nextX < 0 or nextY < 0 or arr[nextX][nextY]:
            delta = (delta+1)%4
            nextX = x + direction[delta][0]
            nextY = y + direction[delta][1]
        x = nextX
        y = nextY
        num += 1
    return arr
```




## 2025.02.23(일)     
         
<br>      
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```



## 2025.02.22(토)     
         
<br>      
순서쌍2  
     
```python
def solution(grid):
    def dfs(x, y):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == '0':
            return
        grid[x][y] = '0'
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            dfs(x+dx, y+dy)
    
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1
    return count
```




## 2025.02.21(금)     
         
<br>      
순서쌍2  
     
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solution(root):
    if not root:
        return 0
    return 1 + max(solution(root.left), solution(root.right))
```


 
## 2025.02.20(목)     
         
<br>      
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```

 
## 2025.02.19(수)     
         
<br>      
순서쌍2  
     
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solution(root):
    if not root:
        return 0
    return 1 + max(solution(root.left), solution(root.right))
```


## 2025.02.18(화)     
         
<br>     
순서쌍2  
     
```python
def solution(grid):
    def dfs(x, y):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == '0':
            return
        grid[x][y] = '0'
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            dfs(x+dx, y+dy)
    
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1
    return count
```



## 2025.02.17(월)     
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```


## 2025.02.16(일)     
         
<br>     
순서쌍2  
     
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solution(root):
    if not root:
        return 0
    return 1 + max(solution(root.left), solution(root.right))
```




## 2025.02.15(토)     
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```


## 2025.02.14(금)     
         
<br>     
순서쌍2  
     
```python
def solution(grid):
    def dfs(x, y):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == '0':
            return
        grid[x][y] = '0'
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            dfs(x+dx, y+dy)
    
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1
    return count
```



## 2025.02.13(목)     
         
<br>     
순서쌍2  
     
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solution(root):
    if not root:
        return 0
    return 1 + max(solution(root.left), solution(root.right))
```



## 2025.02.12(수)     
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```




## 2025.02.11(화)     
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```

## 2025.02.10(월)     
         
<br>     
순서쌍2  
     
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solution(root):
    if not root:
        return 0
    return 1 + max(solution(root.left), solution(root.right))
```




## 2025.02.09(일)     
         
<br>     
순서쌍2  
     
```python
def solution(n):
    arr = [[0 for _ in range(n)] for _ in range(n)]
    x = 0
    y = 0
    num = 1
    delta = 0
    direction = [[0,1],[1,0],[0,-1],[-1,0]]
    print(arr[x][y])
    for _ in range(n*n):
        arr[x][y] = num
        nextX = x + direction[delta][0]
        nextY = y + direction[delta][1]
        if nextX >= n or nextY >= n or nextX < 0 or nextY < 0 or arr[nextX][nextY]:
            delta = (delta+1)%4
            nextX = x + direction[delta][0]
            nextY = y + direction[delta][1]
        x = nextX
        y = nextY
        num += 1
    return arr
```




## 2025.02.07(토)     
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```


## 2025.02.06(금)     
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```



## 2025.02.05(목)     
         
<br>     
순서쌍2  
     
```python
def solution(n):
    arr = [[0 for _ in range(n)] for _ in range(n)]
    x = 0
    y = 0
    num = 1
    delta = 0
    direction = [[0,1],[1,0],[0,-1],[-1,0]]
    print(arr[x][y])
    for _ in range(n*n):
        arr[x][y] = num
        nextX = x + direction[delta][0]
        nextY = y + direction[delta][1]
        if nextX >= n or nextY >= n or nextX < 0 or nextY < 0 or arr[nextX][nextY]:
            delta = (delta+1)%4
            nextX = x + direction[delta][0]
            nextY = y + direction[delta][1]
        x = nextX
        y = nextY
        num += 1
    return arr
```


 
## 2025.02.05(수)     
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```



 
## 2025.02.04(수)     
         
<br>     
순서쌍2  
     
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solution(root):
    if not root:
        return 0
    return 1 + max(solution(root.left), solution(root.right))
```



 
## 2025.02.03(화)     
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```



 
## 2025.02.02(일)     
         
<br>     
순서쌍2  
     
```python
def solution(n):
    arr = [[0 for _ in range(n)] for _ in range(n)]
    x = 0
    y = 0
    num = 1
    delta = 0
    direction = [[0,1],[1,0],[0,-1],[-1,0]]
    print(arr[x][y])
    for _ in range(n*n):
        arr[x][y] = num
        nextX = x + direction[delta][0]
        nextY = y + direction[delta][1]
        if nextX >= n or nextY >= n or nextX < 0 or nextY < 0 or arr[nextX][nextY]:
            delta = (delta+1)%4
            nextX = x + direction[delta][0]
            nextY = y + direction[delta][1]
        x = nextX
        y = nextY
        num += 1
    return arr
```


  
 
## 2025.01.27(수)     
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```
  
 
## 2025.01.27(수)     
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```

  
 
## 2025.01.26(화)     
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```


## 2025.01.25(월)     
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```

## 2025.01.25(일)     
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```


## 2025.01.24(금)     
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```




## 2025.01.23(목)     
         
<br>     
순서쌍2  
     
```python
def solution(n):
    arr = [[0 for _ in range(n)] for _ in range(n)]
    x = 0
    y = 0
    num = 1
    delta = 0
    direction = [[0,1],[1,0],[0,-1],[-1,0]]
    print(arr[x][y])
    for _ in range(n*n):
        arr[x][y] = num
        nextX = x + direction[delta][0]
        nextY = y + direction[delta][1]
        if nextX >= n or nextY >= n or nextX < 0 or nextY < 0 or arr[nextX][nextY]:
            delta = (delta+1)%4
            nextX = x + direction[delta][0]
            nextY = y + direction[delta][1]
        x = nextX
        y = nextY
        num += 1
    return arr
```


## 2025.01.22(수)     
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```



## 2025.01.21(화)     
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```




## 2025.01.20(월)     
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```


## 2025.01.19(일)     
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```


## 2025.01.17(금)     
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```



## 2025.01.16(금)     
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```

## 2025.01.15(목)     
         
<br>     
나선형 계단1 
     
```python
def solution(n):
    arr = [[0 for _ in range(n)] for _ in range(n)]
    x = 0
    y = 0
    num = 1
    delta = 0
    direction = [[0,1],[1,0],[0,-1],[-1,0]]
    print(arr[x][y])
    for _ in range(n*n):
        arr[x][y] = num
        nextX = x + direction[delta][0]
        nextY = y + direction[delta][1]
        if nextX >= n or nextY >= n or nextX < 0 or nextY < 0 or arr[nextX][nextY]:
            delta = (delta+1)%4
            nextX = x + direction[delta][0]
            nextY = y + direction[delta][1]
        x = nextX
        y = nextY
        num += 1
    return arr
```

  
## 2025.01.15(수)     
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```
    
  
## 2025.01.11(토)     
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```


## 2025.01.10(금)     
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```

  
  
## 2025.01.05(일)     
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```




## 2025.01.03(토)     
         
<br>     
2차원 메트릭스  
     
```python
def solution(n):
    arr = [[0 for _ in range(n)] for _ in range(n)]
    x = 0
    y = 0
    num = 1
    delta = 0
    direction = [[0,1],[1,0],[0,-1],[-1,0]]
    print(arr[x][y])
    for _ in range(n*n):
        arr[x][y] = num
        nextX = x + direction[delta][0]
        nextY = y + direction[delta][1]
        if nextX >= n or nextY >= n or nextX < 0 or nextY < 0 or arr[nextX][nextY]:
            delta = (delta+1)%4
            nextX = x + direction[delta][0]
            nextY = y + direction[delta][1]
        x = nextX
        y = nextY
        num += 1
    return arr
```

 
## 2025.01.03(금)     
         
<br>     
최적해3  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```


## 2025.01.01(수)     
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```


## 2024.12.31(수)     
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```

 
## 2024.12.27(금)     
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```



## 2024.12.26(목)   
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```

 
## 2024.12.24(화)   
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```


    
## 2024.12.23(월)   
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```


    
## 2024.12.19(목)   
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```



## 2024.12.18(수)   
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```


## 2024.12.17(화)   
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```


## 2024.12.16(월)   
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```



## 2024.12.14(토)   
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```



## 2024.12.13(금)   
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```




## 2024.12.12(목)   
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```


## 2024.12.11(수)   
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```


## 2024.12.10(화)   
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```



## 2024.12.09(월)   
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```


## 2024.12.08(일)   
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```


## 2024.12.06(금)   
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```


## 2024.12.05(목)  
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```





## 2024.12.04(수)  
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```


  
## 2024.12.01(월)  
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```


## 2024.11.31(일)  
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```


## 2024.11.30(토)  
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```


## 2024.11.29(금)  
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```


## 2024.11.28(목)  
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```


## 2024.11.27(수)  
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```


## 2024.11.26(화)  
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```



## 2024.11.25(월)  
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```


## 2024.11.23(토)  
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```


## 2024.11.22(금)  
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```



## 2024.11.21(목)  
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```



## 2024.11.18(화)  
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```


## 2024.11.17(월)  
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```
 


## 2024.11.17(일)  
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```
 

## 2024.11.14(금)  
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```



## 2024.11.13(목)  
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```

  
## 2024.11.13(수)  
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```

  
## 2024.11.12(화)  
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```


  
## 2024.11.10(일)  
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```


## 2024.11.08(금)  
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```


## 2024.11.07(목) 
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```




## 2024.11.05(화) 
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```



  
## 2024.11.04(월) 
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```

  
## 2024.11.02(토) 
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```


## 2024.11.01(금) 
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```


## 2024.10.31(목) 
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```


## 2024.10.30(수) 
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```



## 2024.10.29(화) 
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```


## 2024.10.28(월) 
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```


## 2024.10.25(금) 
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```
 

## 2024.10.23(수)
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```


## 2024.10.22(화)
         
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```




## 2024.10.21(월)
        
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```


## 2024.10.20(일)
        
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```

## 2024.10.18(금)
        
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```


## 2024.10.17(목)
        
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```


## 2024.10.16(수)
        
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```



## 2024.10.14(월)
        
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```


## 2024.10.13(일)
        
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```



## 2024.10.10(금)
        
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```

## 2024.10.10(금)
        
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```

## 2024.10.09(수)
        
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```



## 2024.10.08(화)
        
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```


## 2024.10.07(화)
        
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```


## 2024.10.06(일)
        
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```



## 2024.10.05(토)
        
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```



## 2024.10.04(금)
        
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```


## 2024.10.03(목)
        
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```


## 2024.10.02(수)
        
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```


## 2024.09.30(화)
        
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```



## 2024.09.30(월)
        
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```


## 2024.09.27(금)
        
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```



## 2024.09.26(목)
        
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```


## 2024.09.25(수)
        
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```




## 2024.09.24(화)
        
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```



## 2024.09.23(월)
        
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```


## 2024.09.22(일)
        
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```
  

## 2024.09.20(금)
        
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```


## 2024.09.19(목)
        
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```

  
## 2024.09.18(수)
        
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```
 
   
## 2024.09.10(화)
        
<br>     
순서쌍2  
     
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1. 
    return answer
```
 

## 2024.09.08(일)
        
<br>     
순서쌍2  
   
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1
    return answer
```


## 2024.09.07(토)
        
<br>     
순서쌍2  
   
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1
    return answer
```



## 2024.09.06(금)
        
<br>     
순서쌍2  
   
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1
    return answer
```


## 2024.09.05(목)
        
<br>     
순서쌍2  
   
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1
    return answer
```


## 2024.09.04(수)
        
<br>     
순서쌍2  
   
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1
    return answer
```


## 2024.09.03(화)
        
<br>     
순서쌍2  
   
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1
    return answer
```


## 2024.09.01(일)
        
<br>     
순서쌍2  
   
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1
    return answer
```

 
## 2024.08.29(금)
        
<br>     
순서쌍2  
   
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1
    return answer
```



## 2024.08.28(목)
        
<br>     
순서쌍2  
   
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1
    return answer
```



## 2024.08.27(수)
        
<br>     
순서쌍2  
   
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1
    return answer
```


## 2024.08.26(월)
        
<br>     
순서쌍2  
   
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1
    return answer
```


 
## 2024.08.22(금)
        
<br>     
순서쌍2  
   
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:  
            answer += 1
    return answer
```



## 2024.08.23(목)
        
<br>     
순서쌍2  
   
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2024.08.22(수)
        
<br>     
순서쌍2  
   
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.08.21(화)
        
<br>     
순서쌍2  
   
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2024.08.20(월)
        
<br>     
순서쌍2  
   
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2024.08.19(월)
        
<br>     
순서쌍2  
   
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```





## 2024.08.14(수)
        
<br>     
순서쌍2  
   
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2024.08.13(화)
       
<br>     
순서쌍2  
   
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2024.08.12(일)
       
<br>     
순서쌍2  
   
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```

 
 
## 2024.08.08(금)
       
<br>     
순서쌍2  
   
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2024.08.07(목)
       
<br>     
순서쌍2  
   
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2024.08.06(수)
       
<br>     
순서쌍2  
   
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2024.08.05(화)
       
<br>     
순서쌍2  
   
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2024.08.04(일)
       
<br>     
순서쌍2  
   
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2024.08.03(토)
       
<br>     
순서쌍2  
   
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.08.02(금)
       
<br>     
순서쌍2  
   
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2024.08.01(목)
       
<br>     
순서쌍2  
   
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2024.07.31(수)
       
<br>     
순서쌍2  
   
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2024.07.30(화)
       
<br>     
순서쌍2  
   
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.07.28(월)
       
<br>     
순서쌍2  
   
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.07.25(토)
       
<br>     
순서쌍2  
   
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.07.24(금)
       
<br>     
순서쌍2  
   
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```




## 2024.07.23(목)
       
<br>     
순서쌍2  
   
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.07.23(수)
       
<br>     
순서쌍2  
   
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.07.23(화)
       
<br>     
순서쌍2  
   
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.07.22(월)
       
<br>     
순서쌍2  
   
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.07.21(일)
       
<br>     
순서쌍2  
   
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```

## 2024.07.20(금)
       
<br>     
순서쌍2  
   
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2024.07.18(목)
     
<br>     
순서쌍2  
   
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.07.17(수)
     
<br>     
순서쌍2  
   
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.07.16(화)
     
<br>     
순서쌍2  
   
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```




## 2024.07.15(월)
     
<br>     
순서쌍2  
   
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2024.07.14(일)
     
<br>     
순서쌍2  
   
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```

## 2024.07.12(토)
     
<br>     
순서쌍2  
  
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```

## 2024.07.12(금)
     
<br>     
순서쌍2  
  
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.07.11(목)
     
<br>     
순서쌍2  
  
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.07.10(화)
     
<br>     
순서쌍2  
  
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2024.07.09(월)
     
<br>     
순서쌍2  
  
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2024.07.09(월)
     
<br>     
순서쌍2  
  
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.07.08(일)
     
<br>     
순서쌍2  
  
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.07.02(토)
     
<br>     
순서쌍2  
  
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.07.02(금)
     
<br>     
순서쌍2  
  
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.07.02(목)
     
<br>     
순서쌍2  
  
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.07.01(수)
     
<br>     
순서쌍2  
  
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.07.01(화)
     
<br>     
순서쌍2  
  
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```

 
## 2024.06.31(월)
     
<br>     
순서쌍2  
  
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


 
## 2024.06.28(금)
     
<br>     
순서쌍2  
  
```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2024.06.27(목)
     
<br>     
순서쌍2  

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.06.26(수)
     
<br>     
순서쌍2  

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2024.06.25(화)
     
<br>     
순서쌍2  

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.06.24(월)
     
<br>     
순서쌍2  

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.06.23(일)
     
<br>     
순서쌍2  

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```

## 2024.06.21(금)
     
<br>     
순서쌍2  

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```

## 2024.06.20(목)
     
<br>     
순서쌍2  

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.06.19(수)
     
<br>     
순서쌍2  

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.06.18(화)
     
<br>     
순서쌍2  

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


# ProgrammersAlgorithms

## 2024.06.17(월)
     
<br>     
순서쌍2  

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.06.16(일)
     
<br>     
순서쌍2  

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2024.06.15(토)
     
<br>     
순서쌍2  

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.06.14(금)
     
<br>     
순서쌍2  

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.06.13(목)
     
<br>     
순서쌍2  

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.06.12(수)
     
<br>     
순서쌍2  

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.06.11(화)
     
<br>     
순서쌍2  

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.06.10(월)
     
<br>     
순서쌍2  

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.06.09(일)
     
<br>     
순서쌍2  

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.06.07(토)
     
<br>     
순서쌍2  

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.06.07(토)
     
<br>     
순서쌍2  

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```

## 2024.06.06(금)
     
<br>     
순서쌍2  

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.06.04(수)
     
<br>     
순서쌍2  

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```
 

## 2024.06.03(화)
     
<br>     
순서쌍2  

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```

## 2024.06.03(월)
     
<br>     
순서쌍2  

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.06.01(토)
     
<br>     
순서쌍2  

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```

## 2024.06.01(토)
     
<br>     
순서쌍2  

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2024.05.29(금)
     
<br>     
순서쌍2  

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.05.29(목)
     
<br>     
순서쌍2  

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.05.29(수)
     
<br>     
순서쌍2  

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.05.28(화)
     
<br>     
순서쌍2  

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.05.27(월)
     
<br>     
순서쌍2  

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
``` 


## 2024.05.24(금)
     
<br>     
순서쌍2  

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
``` 


## 2024.05.24(목)
     
<br>     
순서쌍2  

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
``` 


## 2024.05.23(수)
     
<br>     
순서쌍2  

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.05.22(화)
     
<br>     
순서쌍2  

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.05.21(월)
     
<br>     
순서쌍2  

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.05.20(일)
     
<br>     
순서쌍2  

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.05.19(토)
     
<br>     
순서쌍2  

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2024.05.18(토)
     
<br>     
순서쌍2  

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```

## 2024.05.17(금)
     
<br>     
순서쌍2  

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.05.16(목)
     
<br>     
순서쌍2  

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.05.15(수)
     
<br>     
순서쌍2  

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```

## 2024.05.14(화)
     
<br>     
순서쌍2  

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```

## 2024.05.13(월)
     
<br>     
순서쌍2  

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```

## 2024.05.10(금)
     
<br>     
순서쌍2  

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```

 
## 2024.05.09(목)
     
<br>     
순서쌍2  

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.05.08(수)
     
<br>     
순서쌍2  

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```

## 2024.05.07(화)
     
<br>     
순서쌍2  

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.04.30(수)
     
<br>     
순서쌍2  

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```
 
 
## 2024.04.30(화)
     
<br>     
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.04.29(월)
     
<br>     
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.04.28(일)
     
<br>     
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.04.27(토)
     
<br>     
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.04.26(금)
     
<br>     
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.04.25(목)
     
<br>     
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.04.23(수)
     
<br>     
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.04.23(화)
     
<br>     
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```

## 2024.04.22(월)
     
<br>     
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.04.21(일)
     
<br>     
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.04.20(토)
     
<br>     
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```

## 2024.04.19(금)
     
<br>     
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.04.18(목)
     
<br>     
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.04.17(수)
     
<br>     
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.04.16(화)
     
<br>     
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.04.15(월)
     
<br>     
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.04.14(일)
     
<br>     
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.04.13(토)
     
<br>     
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```

## 2024.04.12(금)
     
<br>     
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.04.11(목)
     
<br>     
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.04.10(수)
     
<br>     
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.04.09(화)
     
<br>     
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.04.08(월)
     
<br>     
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.04.07(일)
     
<br>     
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.04.04(금)
     
<br>     
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.04.03(목)
     
<br>     
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```

## 2024.04.03(수)
     
<br>     
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```




## 2024.04.02(화)
     
<br>     
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2024.04.01(월)
     
<br>     
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.03.31(일)
     
<br>     
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.03.29(금)
     
<br>     
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.03.28(목)
     
<br>     
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2024.03.27(수)
     
<br>     
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2024.03.26(화)
     
<br>     
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2024.03.25(월)
     
<br>     
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```

## 2024.03.24(일)
     
<br>     
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```

## 2024.03.23(토)
     
<br>     
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.03.22(금)
     
<br>     
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```

## 2024.03.22(금)
     
<br>     
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.03.21(목)
     
<br>     
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.03.20(수)
     
<br>     
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2024.03.19(화)
     
<br>     
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.03.18(월)
     
<br>     
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```

## 2024.03.17(일)
     
<br>     
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.03.16(토)
     
<br>     
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2024.03.15(금)
     
<br>     
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.03.14(목)
     
<br>     
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.03.13(수)
     
<br>     
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.03.12(화)
     
<br>     
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.03.11(월)
     
<br>     
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.03.10(일)
     
<br>     
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.03.09(토)
     
<br>     
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.03.08(금)
     
<br>     
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2024.03.07(목)
     
<br>   
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.03.06(수)
     
<br>   
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2024.03.05(화)
     
<br>   
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.03.04(화)
     
<br>   
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.03.03(일)
     
<br>   
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.03.02(토)
     
<br>   
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.03.01(금)
     
<br>   
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.02.29(목)
     
<br>   
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.02.28(목)
   
<br>   
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.02.28(목)
   
<br>   
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.02.28(수)
   
<br>   
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.02.27(화)
   
<br>   
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.02.26(월)
   
<br>   
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.02.25(일)
   
<br>   
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2024.02.24(토)
   
<br>   
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.02.23(금)
   
<br>   
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2024.02.22(목)
   
<br>   
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2024.02.21(수)
   
<br>   
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2024.02.20(화)
   
<br>   
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2024.02.19(월)

   
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.02.18(일)
   
<br>   
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2024.02.17(토)
   
<br>   
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```

## 2024.02.16(금)
   
<br>   
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2024.02.15(목)
   
<br>   
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.02.14(수)
   
<br>   
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.02.09(화)
   
<br>   
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.02.08(월)
   
<br>   
순서쌍2 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.02.06(토)
   
<br>   
순서쌍 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```
## 2024.02.06(토)
   
<br> 
순서쌍 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```
## 2024.02.06(금)
   
<br> 
순서쌍 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```

## 2024.02.06(목)
   
<br> 
순서쌍 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2024.02.06(수)
   
<br> 
순서쌍 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.02.05(화)
   
<br> 
순서쌍 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.02.05(월)
   
<br> 
순서쌍 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.02.04(일)
   
<br> 
순서쌍 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.02.03(토)
   
<br> 
순서쌍 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.02.03(금)
   
<br> 
순서쌍 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2024.02.02(목)
   
<br> 
순서쌍 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.02.01(수)
   
<br> 
순서쌍 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.01.30(화)
   
<br> 
순서쌍 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.01.29(월)
   
<br> 
순서쌍 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.01.28(일)
   
<br> 
순서쌍 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```

## 2024.01.26(금)
   
<br> 
순서쌍 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```

## 2024.01.20(목)
   
<br> 
순서쌍 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.01.19(수)
   
<br> 
순서쌍 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2024.01.19(화)
   
<br> 
순서쌍 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.01.19(월)
   
<br> 
순서쌍 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```

## 2024.01.18(일)
   
<br> 
순서쌍 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```

## 2024.01.16(금)
   
<br> 
순서쌍 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.01.16(목)
   
<br> 
순서쌍 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.01.16(수)
   
<br> 
순서쌍 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.01.16(화)
   
<br> 
순서쌍 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.01.15(월)
   
<br> 
순서쌍 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```
 
## 2024.01.12(금)
   
<br> 
순서쌍 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```

## 2024.01.11(목)
   
<br> 
순서쌍 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```

## 2024.01.10(수)
   
<br> 
순서쌍 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.01.09(화)
   
<br> 
순서쌍 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```

## 2024.01.08(월)
   
<br> 
순서쌍 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.01.07(일)
   
<br> 
순서쌍 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.01.05(금)
   
<br> 
순서쌍 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.01.04(목)
   
<br>
순서쌍 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.01.03(수)
   
<br>
순서쌍 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.01.02(화)
   
<br>
순서쌍 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2024.01.01(월)
   
<br>
순서쌍 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```

## 2023.12.31(일)
   
<br>
순서쌍 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2023.12.30(토)
 
<br>
순서쌍 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2023.12.29(금)
 
<br>
순서쌍 

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2023.12.28(목)
 
<br>
순서쌍

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```

  
## 2023.12.27(수)
 
<br>
순서쌍

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```
  
## 2023.12.20(수)
 
<br>
순서쌍

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2023.12.19(화)
 
<br>
순서쌍

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2023.12.18(월)
 
<br>
순서쌍

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2023.12.17(일)
 
<br>
순서쌍

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```

## 2023.12.16(토)
 
<br>
순서쌍

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2023.12.15(금)
 
<br>
순서쌍

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2023.12.14(목)
 
<br>
순서쌍

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2023.12.13(수)
 
<br>
순서쌍

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2023.12.12(화)
 
<br>
순서쌍

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```




## 2023.12.11(월)
 
<br>
순서쌍

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2023.12.06(토)
 
<br>
순서쌍

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2023.12.06(금)

<br>
순서쌍

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2023.12.06(목)

<br>
순서쌍

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2023.12.06(수)

<br>
순서쌍

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2023.12.05(화)

<br>
순서쌍

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2023.12.04(월)

<br>
순서쌍

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```

 
## 2023.12.03(일)

<br>
순서쌍

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```
  
## 2023.12.02(토)

<br>
순서쌍

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2023.12.01(금)

<br>
순서쌍

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2023.11.30(목)

   
<br>
순서쌍

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2023.11.29(수)

 
<br>
순서쌍

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2023.11.28(화)

 
<br>
순서쌍

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


 
## 2023.11.27(월)

 
<br>
순서쌍

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


 
## 2023.11.26(일)

 
<br>
순서쌍

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2023.11.25(토)

 
<br>
순서쌍

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2023.11.24(금)

 
<br>
순서쌍

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2023.11.23(목)

 
<br>
순서쌍

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2023.11.22(수)

 
<br>
순서쌍

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2023.11.21(화)

 
<br>
순서쌍

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2023.11.20(월)

 
<br>
순서쌍

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```




## 2023.11.19(일)

 
<br>
순서쌍

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2023.11.18(토)

 
<br>
순서쌍

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


  
## 2023.11.17(금)

 
<br>
순서쌍

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2023.11.16(목)

 
<br>
순서쌍

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2023.11.15(수)

 
<br>
순서쌍

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2023.11.14(화)

 
<br>
순서쌍

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2023.11.13(월)

 
<br>
순서쌍

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2023.11.12(일)

 
<br>
순서쌍

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



  
## 2023.11.11(토)

 
<br>
순서쌍

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2023.11.10(금)


<br>
순서쌍

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2023.11.09(목)


<br>
순서쌍의 개수

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2023.11.08(수)


<br>
모스부호(1)

```python
def solution(letter):
    letters = letter.split(' ')
    answer = ''
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
    }
    for i in letters:
        answer += morse[i]
    return answer
```



## 2023.11.07(화)


<br>
가위 바위 보

```python
def solution(rsp):
    answer = ''
    for i in rsp:
        if i=='2':
            answer += '0'
        elif i=='0':
            answer += '5'
        elif i=='5':
            answer += '2'
    return answer
```




## 2023.11.06(월)


<br>
순서쌍의 개수

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```



## 2023.11.05(일)


<br>
순서쌍의 개수

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```


## 2023.11.04(토)


<br>
개미 군단

```python
def solution(hp):
    answer = 0    
    answer += hp//5
    hp = hp%5
    answer += hp//3
    hp = hp%3
    answer += hp
    return answer
```




## 2023.11.03(금)


<br>
순서쌍의 개수

```python
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += 1
    return answer
```
=> 순서쌍의 개수는 결국 약수의 개수를 구하는 것



## 2023.11.02(목)


<br>
진료순서 정하기

```python
def solution(emergency):
    size = len(emergency)
    answer = [0 for _ in range(size)]
    tmp = emergency.copy()
    tmp.sort(reverse=True)

    for i in range(size):
        for j in range(size):
            if emergency[i] == tmp[j]:
                answer[i] = j+1

    return answer
```


<br>
외계행성의 나이

```python
def solution(age):
    answer = ''
    ageList = ['a','b','c','d','e','f','g','h','i','j']
    strAge = str(age)
    for i in strAge:
        answer += ageList[int(i)]
    return answer
```


## 2023.11.01(수)

<br>
짝수 홀수 개수

```python
def solution(num_list):
    answer = [0,0]
    for i in num_list:
        if i%2:
            answer[1] += 1
        else:
            answer[0] += 1
    return answer
```


<br>
문자열 뒤집기

```python
def solution(my_string):
    return my_string[::-1]
```


## 2023.10.31(화)


<br>
옷가게 할인 받기

```python
def solution(price):
    answer = 0
    if price >= 500000:
        answer = price*0.8
    elif price >= 300000:
        answer = price*0.9
    elif price >= 100000:
        answer = price*0.95
    else:
        answer = price
    return int(answer)
```



<br>
배열의 평균값

```python
def solution(numbers):
    return sum(numbers)/len(numbers)
```
  
<br>
피자 나눠먹기(3)

```python
def solution(slice, n):
    answer = 1
    while True:
        if (slice * answer) / n >= 1:
            return answer
        answer += 1
```


## 2023.10.30(월)
  
<br>
짝수는 싫어요

```python
def solution(n):
    answer = []
    for i in range(n+1):
        if i%2:
            answer.append(i)
    return answer
```


## 2023.10.29(일)
  

<br>
최빈값 구하기

```python
def solution(array):
    size = max(array)
    cnt = 0
    idx = 0
    arr = [0 for _ in range(size + 1)]
    for i in array:
        arr[i] += 1
    maxV = max(arr)    

    for i, value in enumerate(arr):
        if value == maxV:
            cnt += 1
            idx = i
    if cnt == 1:
        return idx
    else:
        return -1
```


## 2023.10.28(토)
  

<br>
피자 나눠먹기(1)

```python
def solution(n):
    # 1,2,3,4,5,6,7   => 1
    # 8,9,10,11,12,13,14 => 2
    # 15,16,17,18,19,20,21 => 3
    # ...
    return ((n-1)//7)+1 
```



## 2023.10.27(금)
  

<br>
피자 나눠먹기(2)

```python
def solution(n):
    answer = 1
    while True:
        if (answer*6)%n == 0:
            return answer
        answer += 1
```




## 2023.10.26(목)
  

<br>
최빈값 구하기

```python
def solution(array):
    size = max(array)
    cnt = 0
    idx = 0
    arr = [0 for _ in range(size + 1)]
    for i in array:
        arr[i] += 1
    maxV = max(arr)    

    for i, value in enumerate(arr):
        if value == maxV:
            cnt += 1
            idx = i
    if cnt == 1:
        return idx
    else:
        return -1
```



## 2023.10.25(수)


<br>
중앙값 구하기

```python
def solution(array):
    return sorted(array)[len(array)//2]
```




## 2023.10.24(화)


<br>
분수의 덧셈

```python
def solution(numer1, denom1, numer2, denom2):
    lcm = 0
    for i in range(max(denom1, denom2), denom1 * denom2 + 1):
        if i%denom1 == 0 and i%denom2 == 0:
            lcm = i
            break
    n, m = int(numer1*(lcm/denom1) + numer2*(lcm/denom2)) , lcm
    print(n, m)
    gcd = 1
    for i in range(1, min(n, m) + 1):
        if n%i == 0 and m%i == 0:
            gcd = i

    return [n/gcd, m/gcd]
```
최대공약수와 최소공배수를 직접 짜려고하니 생각보다 어려웠다. 파이썬의 익숙함에 속아 기본적인 함수들도
못만들게 된 것 같다는 반성이든다.



## 2023.10.23(월)


<br>
이차원 배열 대각선 순회하기

```python
def solution(board, k):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if i+j <= k:
                answer += board[i][j]
    return answer
```



## 2023.10.22(일)


<br>
종이 자르기

```python
def solution(M, N):
    return (M-1) + M*(N-1)
```
규칙과 패턴을 찾으면 생각보다 간단한 문제. 하지만 적기 귀찮음



## 2023.10.21(토)


<br>
정사각형으로 만들기

```python
def solution(arr):
    x = len(arr)
    y = len(arr[0])

    # 행의 수가 많을 때
    if x > y:
        for i in range(x):
            for _ in range(x-y):
                arr[i].append(0)
    # 열의 수가 많을 때
    elif x < y:
        for _ in range(y-x):
            arr.append([0 for _ in range(y)])   
    return arr
```
테스트 케이스가 점점 복잡해진다. 리팩토링보다는 깔끔한 예외처리를 먼저 생각하자.


## 2023.10.20(금)


<br>
배열 두배 만들기

```python
def solution(numbers):
    return [i*2 for i in numbers]
```
easy



## 2023.10.19(목)


<br>
정수를 나선형으로 배치하기

```python
def solution(n):
    arr = [[0 for _ in range(n)] for _ in range(n)]
    x = 0
    y = 0
    num = 1
    delta = 0
    direction = [[0,1],[1,0],[0,-1],[-1,0]]
    print(arr[x][y])
    for _ in range(n*n):
        arr[x][y] = num
        nextX = x + direction[delta][0]
        nextY = y + direction[delta][1]
        if nextX >= n or nextY >= n or nextX < 0 or nextY < 0 or arr[nextX][nextY]:
            delta = (delta+1)%4
            nextX = x + direction[delta][0]
            nextY = y + direction[delta][1]
        x = nextX
        y = nextY
        num += 1
    return arr
```
델타변수를 이용한 달팽이 2차원배열 오랜만에 풀어봐서 한참 고민했다.


## 2023.10.18(수)


<br>
특별한 이차원배열2

```python
def solution(arr):
    N = len(arr)
    for i in range(N):
        for j in range(N):
            if arr[i][j] != arr[j][i]:
                return 0
    return 1
```



## 2023.10.17(화)


<br>
제목

```python
def solution(order):
    answer = 0
    # 1. 차가운것 뜨거운것 상관 없이 아메리카노인지 카페라떼인지 중요
    # 2. anything -> 아메리카노
    #    americano in -> 아메리카노
    #    cafelatte in -> 라떼

    for item in order:
        if 'americano' in item:
            answer += 4500
        elif 'cafelatte' in item:
            answer += 5000
        elif 'anything' in item:
            answer += 4500
    return answer
```



## 2023.10.16(월)


<br>
제목

```python
def solution(order):
    answer = 0
    # 1. 차가운것 뜨거운것 상관 없이 아메리카노인지 카페라떼인지 중요
    # 2. anything -> 아메리카노
    #    americano in -> 아메리카노
    #    cafelatte in -> 라떼

    for item in order:
        if 'americano' in item:
            answer += 4500
        elif 'cafelatte' in item:
            answer += 5000
        elif 'anything' in item:
            answer += 4500
    return answer
```



## 2023.10.15(일)


<br>
제목

```python
def solution(order):
    answer = 0
    # 1. 차가운것 뜨거운것 상관 없이 아메리카노인지 카페라떼인지 중요
    # 2. anything -> 아메리카노
    #    americano in -> 아메리카노
    #    cafelatte in -> 라떼

    for item in order:
        if 'americano' in item:
            answer += 4500
        elif 'cafelatte' in item:
            answer += 5000
        elif 'anything' in item:
            answer += 4500
    return answer
```




## 2023.10.12(목)


<br>
제목

```python
def solution(order):
    answer = 0
    # 1. 차가운것 뜨거운것 상관 없이 아메리카노인지 카페라떼인지 중요
    # 2. anything -> 아메리카노
    #    americano in -> 아메리카노
    #    cafelatte in -> 라떼

    for item in order:
        if 'americano' in item:
            answer += 4500
        elif 'cafelatte' in item:
            answer += 5000
        elif 'anything' in item:
            answer += 4500
    return answer
```



## 2023.10.12(목)


<br>
커피 심부름

```python
def solution(order):
    answer = 0
    # 1. 차가운것 뜨거운것 상관 없이 아메리카노인지 카페라떼인지 중요
    # 2. anything -> 아메리카노
    #    americano in -> 아메리카노
    #    cafelatte in -> 라떼

    for item in order:
        if 'americano' in item:
            answer += 4500
        elif 'cafelatte' in item:
            answer += 5000
        elif 'anything' in item:
            answer += 4500
    return answer
```


## 2023.10.11(수)


<br>
날짜 비교하기

```python
def solution(date1, date2):
    
    if date1[0] > date2[0]:
        return 0
    elif date1[0] < date2[0]:
        return 1
    elif date1[0] == date2[0]:
        if date1[1] > date2[1]:
            return 0
        elif date1[1] < date2[1]:
            return 1
        elif date1[1] == date2[1]:
            if date1[2] > date2[2]:
                return 0
            elif date1[2] < date2[2]:
                return 1
            elif date1[2] == date2[2]:
                return 0
```
날짜 비교가 생각보다 까다로웠다. 반례 [10000, 12, 15], [0, 12, 17] 케이스를 염두에 두자.
하지만 파이썬에서는 더 단순하게 리스트의 크기 비교가 가능하다. 어떤 원리의 동작인지는 정확하게 모르겠다.
```python
def solution(date1, date2):
    return int(date1 < date2)
```
간단하게 이렇게 해결 가능하다.

## 2023.10.10(화)


<br>
배열의 원소 삭제하기

```python
def solution(arr, delete_list):
    answer = []
    for idx, item in enumerate(arr):
        if arr[idx] not in delete_list:
            answer.append(arr[idx])
    return answer
```





## 2023.10.6(금)


<br>
전국 대회 선발 고사

```python
def solution(rank, attendance):
    answer = 0
    # 1. arr 최소값 찾기
    # 2. 참석여부 검사
    # 3. 배열에 추가하고 해당 rank[i] 값 높게 변경
    arr = []
    while len(arr) < 3 :
        idx = rank.index(min(rank))
        if attendance[idx]:
            arr.append(idx)
            rank[idx] = 101
        else:
            rank[idx] = 101
    a, b, c = arr
    return 10000*a + 100*b + c
```
튜플 자료형을 활용하면 좀 더 쉽게 풀 수 있던 문제 같다.
다음은 튜플을 통한 리펙토링
```python
def solution(rank, attendance):
    arr = []
    for i, attend in enumerate(attendance):
        if attend:
            arr.append((rank[i], i))
    arr.sort()
    a, b , c = arr[:3]
    return 10000*a[1] + 100*b[1] + c[1]
```


<br>
문자열 묶기

```python
def solution(strArr):
    lengths = [0 for _ in range(30)]
    
    for i in strArr:
        lengths[len(i)-1] += 1
    answer = max(lengths)
    return answer
```

<br>
배열 비교하기

```python
def solution(arr1, arr2):
    l1, l2 = len(arr1), len(arr2)
    if l1 > l2:
        return 1
    elif l1 < l2:
        return -1
    elif l1 == l2:
        if sum(arr1) > sum(arr2):
            return 1
        elif sum(arr1) < sum(arr2):
            return -1
        elif sum(arr1) == sum(arr2):
            return 0
```



## 2023.10.5(목)

<br>
배열의 길이를 2의 거듭제곱으로 만들기

```python
import math

def solution(arr):
    n = int(math.pow(2,math.ceil(math.log2(len(arr)))))
    if len(arr) < n:
        for i in range(n - len(arr)):
            arr.append(0)
    return arr
```

<br>
무작위로 K개의 수 뽑기

```python
def solution(arr, k):
    answer = []
    leng = len(arr)

    for i in range(leng):
        if i == 0:
            answer.append(arr[i])
        else:
            flag = True
            for j in range(len(answer)):
                if arr[i] == answer[j]:
                    print('같은값 : ', arr[i])
                    flag = False
                    break
            if flag:
                answer.append(arr[i])
        if len(answer) == k:
            break
    if len(answer) < k:
        for i in range(k-len(answer)):
            answer.append(-1)
    return answer
```
쉬운문제를 쓸데없이 어렵게 생각했다.
변경후
```python
def solution(arr, k):
    answer = []
    for i in arr:
        if i not in answer:
            answer.append(i)
        if len(answer) == k:
            break
    if len(answer) < k:
        for i in range(k-len(answer)):
            answer.append(-1)
    return answer
```


<br>
배열의 길이에 따라 다른 연산하기

```python
def solution(arr, n):
    leng = len(arr)
    if leng%2==0:
        for i in range(1,leng,2):
            arr[i] += n
    else:
        for i in range(0,leng,2):
            arr[i] += n
    return arr
```


<br>
배열만들기 6

```python
def solution(arr):
    answer = []
    i = 0
    while i<len(arr):
        leng = len(answer)
        if leng == 0:
            answer.append(arr[i])
            i+=1
        elif answer[leng-1] == arr[i]:
            del answer[leng-1]
            i+=1
        else:
            answer.append(arr[i])
            i+=1
    if len(answer) == 0:
        return [-1]
    return answer
```


## 2023.10.4(수)

<br>
문자열 잘라서 정렬하기

```python
def solution(myStr):
    answer = myStr.replace('a',' ').replace('b', ' ').replace('c',' ').strip().split(' ')
    result = [i for i in answer if i != '']
    if result == []:
        result = ['EMPTY']
    return result
```


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


## 2023.09.13(수)
<br>
특이한 이차원배월

```python
def solution(n):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i==j:
                answer[i][j] = 1
    return answer
```


## 2023.09.12(화)
<br>
l로 만들기

```python
def solution(myString):
    answer = ''
    for i in myString:
        if i < 'l':
            answer += 'l'
        else:
            answer += i    
    return answer
```


## 2023.09.11(월)
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


## 2023.09.10(일)
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

## 2023.09.09(토)
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


## 2023.09.08(금)


<br>
문자열 반복 출력

```python
def solution(my_string, n):
    answer = ''
    for i in my_string:
        answer += i*n
    return answer
```


## 2023.09.07(목)


<br>
배열 뒤집기

```python
def solution(num_list):
    return num_list[::-1]
```



## 2023.09.06(수)


<br>
직각삼각형 출력하기

```python
n = int(input())

for i in range(1,n+1):
    print('*' * i)
```




## 2023.09.05(화)


<br>
문자열 뒤집기

```python
def solution(my_string):
    return my_string[::-1]
```


## 2023.09.04(월)


<br>
아이스아메리카노

```python
def solution(money):
    answer = [money//5500, money%5500]
    return answer
```



## 2023.09.03(일)


<br>
특정 문자 제거하기

```python
def solution(my_string, letter):
    answer = ''
    for i in my_string:
        if i!=letter:
            answer += i
    return answer
```

## 2023.09.02(토)


<br>
아이스아메리카노

```python
def solution(money):
    answer = [money//5500, money%5500]
    return answer
```

## 2023.09.01(금)


<br>
각도기

```python
def solution(angle):
    if 0 < angle < 90:
        return 1
    elif angle == 90:
        return 2
    elif 90 < angle < 180:
        return 3
    elif angle == 180:
        return 4
```

## 2023.08.31(목)


<br>
양꼬치

```python
def solution(n, k):
    answer = 12000*n + 2000*k - 2000*(n//10)
    return answer
```

## 2023.08.30(수)


<br>
짝수의 합

```python
def solution(n):
    answer = 0
    for i in range(2,n+1):
        if i%2 == 0:
            answer += i
    return answer
```

## 2023.08.29(화)


<br>
아이스아메리카노

```python
def solution(money):
    answer = [money//5500, money%5500]
    return answer
```

## 2023.08.28(월)


<br>
문자열 안의 문자열

```python
def solution(str1, str2):
    return 1 if str2 in str1 else 2 
```
=> 파이썬의 3항 연산자는 조금 특이하다. (참) if (조건) else (거짓)

## 2023.08.27(일)


<br>
배열 자르기

```python
def solution(numbers, num1, num2):
    return numbers[num1:num2+1]
```

## 2023.08.26(토)


<br>
배열 원소의 길이

```python
def solution(strlist):
    return [len(x) for x in strlist]
```

## 2023.08.25(금)


<br>
편지

```python
def solution(message):
    return len(message)*2
```
