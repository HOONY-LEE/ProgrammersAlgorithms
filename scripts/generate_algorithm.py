import random
import hashlib
from datetime import datetime
from zoneinfo import ZoneInfo

WEEKDAY_KR = ["월", "화", "수", "목", "금", "토", "일"]

PROBLEMS = [
    {
        "title": "두 수의 합",
        "problem": "정수 배열 nums와 목표값 target이 주어질 때, 합이 target이 되는 두 원소의 인덱스를 반환하시오.\n각 입력에는 정확히 하나의 답이 존재하며, 같은 원소를 두 번 사용할 수 없습니다.\n입력: nums = [2, 7, 11, 15], target = 9 → 출력: [0, 1]",
        "solution": """def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        if target - n in seen:
            return [seen[target - n], i]
        seen[n] = i"""
    },
    {
        "title": "유효한 괄호",
        "problem": "괄호 문자 '(', ')', '{', '}', '[', ']'로 이루어진 문자열 s가 주어질 때, 올바른 괄호 문자열인지 판별하시오.\n열린 괄호는 반드시 같은 종류의 닫힌 괄호로 닫혀야 하며, 올바른 순서로 닫혀야 합니다.\n입력: s = '()[]{}' → 출력: True",
        "solution": """def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for ch in s:
        if ch in mapping:
            if not stack or stack[-1] != mapping[ch]:
                return False
            stack.pop()
        else:
            stack.append(ch)
    return not stack"""
    },
    {
        "title": "중복 없는 가장 긴 부분 문자열",
        "problem": "문자열 s가 주어질 때, 중복 문자가 없는 가장 긴 부분 문자열의 길이를 구하시오.\n슬라이딩 윈도우 기법을 활용하면 효율적으로 풀 수 있습니다.\n입력: s = 'abcabcbb' → 출력: 3 ('abc')",
        "solution": """def length_of_longest_substring(s):
    char_set = set()
    left = 0
    max_len = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len"""
    },
    {
        "title": "피보나치 수열 (메모이제이션)",
        "problem": "n번째 피보나치 수를 반환하는 함수를 작성하시오. (0번째: 0, 1번째: 1)\n단순 재귀 대신 메모이제이션을 사용하여 시간복잡도를 O(n)으로 줄이시오.\n입력: n = 10 → 출력: 55",
        "solution": """def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]"""
    },
    {
        "title": "배열의 최댓값 인덱스",
        "problem": "정수 배열에서 최댓값이 처음 등장하는 인덱스를 반환하시오.\n배열은 비어있지 않으며 정수로만 구성됩니다.\n입력: nums = [3, 1, 4, 1, 5, 9, 2, 6] → 출력: 5",
        "solution": """def max_index(nums):
    return nums.index(max(nums))"""
    },
    {
        "title": "팰린드롬 판별",
        "problem": "문자열이 팰린드롬(앞뒤로 읽어도 같은 문자열)인지 판별하시오.\n영문 소문자만 포함되며 공백은 없습니다.\n입력: s = 'racecar' → 출력: True",
        "solution": """def is_palindrome(s):
    return s == s[::-1]"""
    },
    {
        "title": "소수 판별",
        "problem": "주어진 정수 n이 소수인지 판별하는 함수를 작성하시오.\n에라토스테네스의 체 원리를 응용하여 O(√n) 시간 내에 풀 수 있습니다.\n입력: n = 17 → 출력: True",
        "solution": """def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True"""
    },
    {
        "title": "아나그램 그룹화",
        "problem": "문자열 배열이 주어질 때, 아나그램끼리 같은 그룹으로 묶어 반환하시오.\n아나그램이란 문자의 순서를 바꿔 다른 단어를 만들 수 있는 단어들의 관계입니다.\n입력: strs = ['eat','tea','tan','ate','nat','bat'] → 출력: [['eat','tea','ate'],['tan','nat'],['bat']]",
        "solution": """from collections import defaultdict
def group_anagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        groups[tuple(sorted(s))].append(s)
    return list(groups.values())"""
    },
    {
        "title": "이진 탐색",
        "problem": "오름차순으로 정렬된 정수 배열 nums에서 target의 인덱스를 반환하시오. 없으면 -1을 반환합니다.\n반드시 O(log n) 시간복잡도로 구현하시오.\n입력: nums = [-1,0,3,5,9,12], target = 9 → 출력: 4",
        "solution": """def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1"""
    },
    {
        "title": "연속 부분 배열의 최대 합 (카데인 알고리즘)",
        "problem": "정수 배열에서 연속된 부분 배열의 합이 최대가 되는 값을 반환하시오.\n카데인(Kadane) 알고리즘을 사용하면 O(n)에 해결할 수 있습니다.\n입력: nums = [-2,1,-3,4,-1,2,1,-5,4] → 출력: 6",
        "solution": """def max_subarray(nums):
    max_sum = curr = nums[0]
    for n in nums[1:]:
        curr = max(n, curr + n)
        max_sum = max(max_sum, curr)
    return max_sum"""
    },
    {
        "title": "문자열 뒤집기",
        "problem": "문자 배열 s가 주어질 때, 배열을 in-place로 뒤집으시오. 추가 메모리를 O(1)만 사용해야 합니다.\n투 포인터 방식으로 구현하시오.\n입력: s = ['h','e','l','l','o'] → 출력: ['o','l','l','e','h']",
        "solution": """def reverse_string(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s"""
    },
    {
        "title": "유일한 원소 찾기",
        "problem": "정수 배열에서 딱 한 번만 등장하는 원소를 반환하시오. 나머지 원소는 모두 두 번씩 등장합니다.\nXOR 비트 연산을 활용하면 O(n) 시간, O(1) 공간으로 풀 수 있습니다.\n입력: nums = [4,1,2,1,2] → 출력: 4",
        "solution": """def single_number(nums):
    result = 0
    for n in nums:
        result ^= n
    return result"""
    },
    {
        "title": "숫자를 로마 숫자로 변환",
        "problem": "1~3999 사이의 정수를 로마 숫자 문자열로 변환하는 함수를 작성하시오.\n로마 숫자: I=1, V=5, X=10, L=50, C=100, D=500, M=1000\n입력: num = 1994 → 출력: 'MCMXCIV'",
        "solution": """def int_to_roman(num):
    vals = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    syms = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
    result = ''
    for v, s in zip(vals, syms):
        while num >= v:
            result += s
            num -= v
    return result"""
    },
    {
        "title": "오름차순 정렬된 배열에서 중복 제거",
        "problem": "오름차순 정렬된 배열에서 중복을 in-place로 제거하고, 고유한 원소의 개수를 반환하시오.\n추가 메모리를 사용하지 않고 투 포인터로 구현하시오.\n입력: nums = [0,0,1,1,1,2,2,3,3,4] → 출력: 5 (nums = [0,1,2,3,4,...])",
        "solution": """def remove_duplicates(nums):
    if not nums:
        return 0
    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[k] = nums[i]
            k += 1
    return k"""
    },
    {
        "title": "계단 오르기 (DP)",
        "problem": "n개의 계단을 오르는데, 한 번에 1칸 또는 2칸씩 오를 수 있습니다. n개의 계단을 오르는 방법의 수를 구하시오.\n동적 프로그래밍 또는 피보나치 패턴으로 풀 수 있습니다.\n입력: n = 5 → 출력: 8",
        "solution": """def climb_stairs(n):
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b"""
    },
    {
        "title": "가장 많이 등장한 원소 K개",
        "problem": "정수 배열 nums와 정수 k가 주어질 때, 가장 자주 등장하는 k개의 원소를 반환하시오.\n시간복잡도 O(n log n)보다 효율적으로 풀 수 있습니다.\n입력: nums = [1,1,1,2,2,3], k = 2 → 출력: [1, 2]",
        "solution": """from collections import Counter
def top_k_frequent(nums, k):
    return [x for x, _ in Counter(nums).most_common(k)]"""
    },
    {
        "title": "행렬 90도 회전",
        "problem": "n×n 정수 행렬이 주어질 때, in-place로 시계 방향 90도 회전시키시오.\n전치(transpose) 후 각 행을 뒤집는 방식으로 구현할 수 있습니다.\n입력: [[1,2,3],[4,5,6],[7,8,9]] → 출력: [[7,4,1],[8,5,2],[9,6,3]]",
        "solution": """def rotate(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()"""
    },
    {
        "title": "주식 최대 이익",
        "problem": "주가 배열 prices가 주어질 때, 한 번 사고 팔아서 얻을 수 있는 최대 이익을 반환하시오.\n이익이 없으면 0을 반환합니다. 반드시 사는 날이 파는 날보다 앞서야 합니다.\n입력: prices = [7,1,5,3,6,4] → 출력: 5",
        "solution": """def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    for p in prices:
        min_price = min(min_price, p)
        max_profit = max(max_profit, p - min_price)
    return max_profit"""
    },
    {
        "title": "빗물 트래핑",
        "problem": "지형의 높이를 나타내는 배열이 주어질 때, 비가 온 후 고이는 빗물의 총량을 구하시오.\n투 포인터 방식으로 O(n) 시간, O(1) 공간에 해결할 수 있습니다.\n입력: height = [0,1,0,2,1,0,1,3,2,1,2,1] → 출력: 6",
        "solution": """def trap(height):
    left, right = 0, len(height) - 1
    left_max = right_max = water = 0
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    return water"""
    },
    {
        "title": "단어 빈도 카운트",
        "problem": "문자열 배열 words가 주어질 때, 각 단어의 등장 횟수를 딕셔너리로 반환하시오.\n대소문자를 구분하지 않으며, 결과는 빈도 내림차순으로 정렬하시오.\n입력: words = ['apple','banana','apple','cherry','banana','apple'] → 출력: {'apple':3,'banana':2,'cherry':1}",
        "solution": """from collections import Counter
def word_count(words):
    return dict(Counter(w.lower() for w in words).most_common())"""
    },
    {
        "title": "연결 리스트 뒤집기",
        "problem": "단방향 연결 리스트의 헤드가 주어질 때, 리스트를 뒤집어서 새 헤드를 반환하시오.\nin-place로 O(n) 시간, O(1) 공간에 구현하시오.\n입력: 1->2->3->4->5 → 출력: 5->4->3->2->1",
        "solution": """class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev"""
    },
    {
        "title": "최장 공통 접두사",
        "problem": "문자열 배열에서 모든 문자열의 공통 접두사(prefix) 중 가장 긴 것을 반환하시오.\n공통 접두사가 없으면 빈 문자열을 반환합니다.\n입력: strs = ['flower','flow','flight'] → 출력: 'fl'",
        "solution": """def longest_common_prefix(strs):
    if not strs:
        return ''
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ''
    return prefix"""
    },
    {
        "title": "배열 회전",
        "problem": "정수 배열 nums를 오른쪽으로 k번 회전시키시오. in-place로 구현해야 합니다.\n뒤집기(reverse) 세 번으로 O(n) 시간, O(1) 공간에 해결할 수 있습니다.\n입력: nums = [1,2,3,4,5,6,7], k = 3 → 출력: [5,6,7,1,2,3,4]",
        "solution": """def rotate(nums, k):
    n = len(nums)
    k %= n
    nums.reverse()
    nums[:k] = nums[:k][::-1]
    nums[k:] = nums[k:][::-1]"""
    },
    {
        "title": "유효한 스도쿠",
        "problem": "9×9 스도쿠 보드가 주어질 때, 현재 채워진 숫자들이 규칙에 유효한지 판별하시오.\n각 행, 열, 3×3 박스에 1~9가 중복 없이 있어야 합니다. '.'은 빈 칸입니다.\n같은 행/열/박스에 같은 숫자가 있으면 False를 반환하시오.",
        "solution": """def is_valid_sudoku(board):
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
    return True"""
    },
    {
        "title": "숫자 뒤집기",
        "problem": "32비트 부호 있는 정수 x를 뒤집으시오. 뒤집은 결과가 32비트 범위를 벗어나면 0을 반환합니다.\n문자열 변환 없이 수학적으로 구현하는 방법도 있습니다.\n입력: x = 123 → 출력: 321 / x = -123 → 출력: -321",
        "solution": """def reverse_int(x):
    sign = -1 if x < 0 else 1
    x = int(str(abs(x))[::-1]) * sign
    return x if -(2**31) <= x <= 2**31 - 1 else 0"""
    },
    {
        "title": "두 정렬 배열 병합",
        "problem": "오름차순으로 정렬된 두 배열 nums1(크기 m+n), nums2(크기 n)를 병합하여 nums1에 정렬된 상태로 저장하시오.\nnums1의 뒤쪽 n개 원소는 0으로 채워져 있습니다. in-place, 역방향 투 포인터로 풀 수 있습니다.\n입력: nums1=[1,2,3,0,0,0] m=3, nums2=[2,5,6] n=3 → 출력: [1,2,2,3,5,6]",
        "solution": """def merge(nums1, m, nums2, n):
    i, j, k = m - 1, n - 1, m + n - 1
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    nums1[:j+1] = nums2[:j+1]"""
    },
    {
        "title": "행렬 나선형 순회",
        "problem": "m×n 행렬이 주어질 때, 나선형(spiral) 순서로 모든 원소를 반환하시오.\n경계를 좁혀가며 순회하는 방식으로 구현합니다.\n입력: [[1,2,3],[4,5,6],[7,8,9]] → 출력: [1,2,3,6,9,8,7,4,5]",
        "solution": """def spiral_order(matrix):
    result = []
    while matrix:
        result += matrix.pop(0)
        matrix = list(zip(*matrix))[::-1]
    return result"""
    },
    {
        "title": "완전 제곱수 최소 개수 (DP)",
        "problem": "정수 n이 주어질 때, 합이 n이 되는 완전 제곱수(1, 4, 9, 16...)의 최소 개수를 반환하시오.\n동적 프로그래밍 또는 BFS로 풀 수 있습니다.\n입력: n = 12 → 출력: 3 (4+4+4)",
        "solution": """def num_squares(n):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], dp[i - j*j] + 1)
            j += 1
    return dp[n]"""
    },
    {
        "title": "LRU 캐시 구현",
        "problem": "LRU(Least Recently Used) 캐시를 구현하시오. get(key)와 put(key, value) 연산을 지원해야 합니다.\n두 연산 모두 O(1) 시간복잡도로 동작해야 합니다.\n캐시 용량이 초과되면 가장 오래 사용하지 않은 항목을 제거합니다.",
        "solution": """from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)"""
    },
    {
        "title": "문자열 압축",
        "problem": "문자열에서 연속된 같은 문자를 '문자+개수' 형태로 압축하시오. 압축 결과가 원본보다 길면 원본을 반환합니다.\n입력: s = 'aabcccccaaa' → 출력: 'a2b1c5a3'\n입력: s = 'abcde' → 출력: 'abcde' (압축이 더 길어서)",
        "solution": """def compress(s):
    result = ''
    i = 0
    while i < len(s):
        count = 1
        while i + count < len(s) and s[i + count] == s[i]:
            count += 1
        result += s[i] + str(count)
        i += count
    return result if len(result) < len(s) else s"""
    },
    {
        "title": "투 포인터: 정렬 배열에서 합이 0인 세 수",
        "problem": "정수 배열에서 합이 0이 되는 세 원소의 조합을 모두 반환하시오. 중복 조합은 제외합니다.\n정렬 후 투 포인터 방식으로 O(n²)에 풀 수 있습니다.\n입력: nums = [-1,0,1,2,-1,-4] → 출력: [[-1,-1,2],[-1,0,1]]",
        "solution": """def three_sum(nums):
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s == 0:
                result.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l+1]: l += 1
                while l < r and nums[r] == nums[r-1]: r -= 1
                l += 1; r -= 1
            elif s < 0:
                l += 1
            else:
                r -= 1
    return result"""
    },
]


def get_today_header():
    now = datetime.now(ZoneInfo("Asia/Seoul"))
    weekday = WEEKDAY_KR[now.weekday()]
    return f"##{now.strftime('%Y.%m.%d')}({weekday})"


def pick_problem():
    today = datetime.now(ZoneInfo("Asia/Seoul")).strftime("%Y-%m-%d")
    seed = int(hashlib.md5(today.encode()).hexdigest(), 16)
    random.seed(seed)
    return random.choice(PROBLEMS)


def update_readme(problem_data):
    readme_path = "README.md"
    header = get_today_header()
    title = problem_data["title"]
    problem = problem_data["problem"]
    solution = problem_data["solution"]

    new_entry = f"\n{header}\n\n<br>.\n**{title}**\n{problem}\n<br>.\n\n```python\n{solution}\n```\n"

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    title_end = content.find("\n", content.find("# ProgrammersAlgorithms"))
    updated = content[:title_end] + new_entry + content[title_end:]

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(updated)

    print(f"✅ 추가 완료: {header} - {title}")


if __name__ == "__main__":
    p = pick_problem()
    print(f"📝 오늘의 문제: {p['title']}")
    update_readme(p)
