import anthropic
import os
from datetime import datetime
from zoneinfo import ZoneInfo

WEEKDAY_KR = ["월", "화", "수", "목", "금", "토", "일"]

def get_today_header():
    now = datetime.now(ZoneInfo("Asia/Seoul"))
    weekday = WEEKDAY_KR[now.weekday()]
    return f"##{now.strftime('%Y.%m.%d')}({weekday})"

def generate_problem_and_solution():
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

    prompt = """알고리즘 문제를 하나 생성하고 Python으로 풀이를 작성해줘.

조건:
- 난이도: 프로그래머스 Level 1~2 수준 (간단하지만 사고가 필요한 문제)
- 문제 유형: 배열, 문자열, 해시, 탐색, 정렬, DP 중 랜덤하게 선택
- 중복 방지: 슬라이딩 윈도우, 투 포인터, 이진 탐색 등 다양하게 출제

출력 형식 (이 형식을 정확히 지켜줘):
---PROBLEM---
[문제 설명을 한국어로 2~4줄로 작성. 입력/출력 조건 포함]
---SOLUTION---
[Python 풀이 코드만. 주석 없이 함수 하나]
---END---"""

    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )

    response = message.content[0].text
    problem = response.split("---PROBLEM---")[1].split("---SOLUTION---")[0].strip()
    solution = response.split("---SOLUTION---")[1].split("---END---")[0].strip()

    return problem, solution

def update_readme(problem, solution):
    readme_path = "README.md"
    header = get_today_header()

    new_entry = f"\n{header}\n\n<br>.\n{problem}\n<br>.\n\n```python\n{solution}\n```\n"

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    title_end = content.find("\n", content.find("# ProgrammersAlgorithms"))
    updated = content[:title_end] + new_entry + content[title_end:]

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(updated)

    print(f"✅ 새 항목 추가 완료: {header}")

if __name__ == "__main__":
    print("🔄 알고리즘 문제 생성 중...")
    problem, solution = generate_problem_and_solution()
    print(f"문제:\n{problem}\n")
    print(f"풀이:\n{solution}\n")
    update_readme(problem, solution)
