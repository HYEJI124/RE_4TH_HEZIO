# Variables 실습

# ========================================
# 실습 1: 영화 정보 출력
# ========================================

# 영화 정보를 변수에 저장
title = "Inception"                   # 영화 제목
director = "Christopher Nolan"        # 감독명
year = 2010                           # 개봉연도
genre = "Sci-Fi"                      # 장르

# f-string을 사용하여 영화 정보 출력
print(f"영화 제목: {title}")
print(f"감독: {director}")
print(f"개봉연도: {year}")
print(f"장르: {genre}")

# 한 줄로 모든 정보 출력
print(f"Title: {title}, Director: {director}, Year: {year}, Genre: {genre}")

# ========================================
# 실습 2: 자기소개 출력 (여러 줄 문자열)
# ========================================

# 개인 정보를 변수에 저장
person_name = "HYEJI"                 # 이름
person_age = 23                       # 나이
person_mbti = "ESTP"                  # MBTI 성격유형

# 여러 줄 문자열(""")과 f-string 조합 사용
introduction = f"""안녕하세요!
제 이름은 {person_name}이고,
{person_age}살입니다.
제 MBTI는 {person_mbti}예요.
만나서 반갑습니다!"""

print(introduction)

# 한 줄로도 출력 가능
print(f"안녕하세요! 제 이름은 {person_name}, {person_age}살, 제 MBTI는 {person_mbti}예요.")

# Operators 연습
# ===========================
# 실습 2 : 문자열 연산
# ===========================

intro = "둠칫"
drop = "두둠칫"

# + 연산자: 문자열을 이어 붙임
# * 연산자: 문자열을 반복
# 결과 : "둠칫두둠칫두둠칫둠칫"
print(intro + drop * 2 + intro)


# ===========================
# 실습 3 : 입력받아 변수에 저장하기
# ===========================

# input()으로 입력을 받으면 문자열 한 줄이 들어옴
# split() → 공백 기준으로 나눠서 여러 변수에 저장 가능
name, age = input('이름과 나이를 입력하세요.').split()
print(f'안녕하세요. 저는 {name} 이고, {age}살 입니다.')
# 예) 입력: 홍길동 20 → 출력: 안녕하세요. 저는 홍길동 이고, 20살 입니다.


# ===========================
# 실습 4 : 사각형의 넓이와 둘레
# ===========================

# int(input()) : 입력값을 정수로 변환
width = int(input('가로 길이:'))   # 가로 길이 입력받음
height = int(input('세로 길이:'))  # 세로 길이 입력받음

# 넓이 = 가로 × 세로
print(f'넓이: {width * height}')

# 둘레 = (가로 + 세로) × 2
print(f'둘레: {(width + height) * 2}')


# ===========================
# 실습 5. 네 자릿수 정수 자리수 분리
# ===========================

num = int(input('네 자릿수 정수:'))  # 예) 1234
# // : 몫 연산, % : 나머지 연산
print(f'천의 자리: {num // 1000}')  # 1234 // 1000 = 1
num %= 1000                          # num = 234
print(f'백의 자리: {num // 100}')    # 234 // 100 = 2
num %= 100                           # num = 34
print(f'십의 자리: {num // 10}')     # 34 // 10 = 3
num %= 10                            # num = 4
print(f'일의 자리: {num // 1}')      # 4


# ===========================
# 실습 6 : 팀 발표자와 주제 입력
# ===========================

# 입력 예시:
# 홍길동 이순신 세종
# 파이썬 자바 C언어
# → 각각 이름과 주제를 변수에 저장
name1, name2, name3 = input().split()
topic1, topic2, topic3 = input().split()
#
print(f'1조 발표자: {name1} - 주제: {topic1}')
print(f'2조 발표자: {name2} - 주제: {topic2}')
print(f'3조 발표자: {name3} - 주제: {topic3}')


# ===========================
# 실습 7. 날짜와 시간 입력받기
# ===========================

# 입력 예시:
# 2025.03.01
# 09:30:00

# split('.') : 마침표 기준으로 나눔 → ['2025', '03', '01']
year, month, day = input().split('.')

# split(':') : 콜론 기준으로 나눔 → ['09', '30', '00']
hour, minute, second = input().split(':')

# 출력 시 f-string으로 보기 좋게 표현
print(f'RE4의 개강일은 {year}년 {month}월 {day}일')
print(f'시작 시간은 {hour}시 {minute}분 {second}초입니다.')
