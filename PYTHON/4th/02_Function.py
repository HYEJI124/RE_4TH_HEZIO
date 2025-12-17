# ==========================================
# 함수의 범위(Scope) 이해하기
# ==========================================

'''
변수의 범위(Scope)란?
- 변수가 접근 가능한 영역
- 변수가 어디서 사용될 수 있는지의 규칙

쉬운 비유: 집
- 거실 = 전역 범위 (모든 방에서 볼 수 있는 거실)
- 방 = 지역 범위 (그 방에서만 쓸 수 있는 공간)
- 방 안의 물건 = 지역 변수 (그 방에서만 사용)
- 거실의 물건 = 전역 변수 (모든 방에서 사용 가능)
'''

# ==========================================
# 전역 변수 vs 지역 변수
# ==========================================

# 전역 변수 (Global Variable) - 함수 밖에서 선언
global_var = '전역 변수: 어디서든 접근 가능'

def my_fun():
    # 지역 변수 (Local Variable) - 함수 안에서 선언
    local_var = '지역 변수: 이 함수 안에서만 사용 가능'

    print('함수 안에서:')
    print('전역 변수:', global_var)  # 접근 가능
    print('지역 변수:', local_var)   # 접근 가능

my_fun()

print('\n함수 밖에서:')
print('전역 변수:', global_var)  # 접근 가능
# print('지역 변수:', local_var)  # 에러! 함수 밖에서 지역 변수 접근 불가


# ==========================================
# global 키워드 사용하기
# ==========================================

'''
중요: 함수 안에서 전역 변수를 수정하려면 global 키워드가 필요!
'''

count = 0  # 전역 변수

# 잘못된 방법 (에러 발생)
# def increment_wrong():
#     count += 1  # 에러! 파이썬이 count를 지역 변수로 착각
#     # UnboundLocalError 발생!

# 올바른 방법 (global 사용)

def increment_right():
    global count  # 전역 변수 count를 사용
    count = count + 1  # 전역 변수 수정 가능

print('초기값:', count)  # 0
increment_right()
print('1회 증가:', count)  # 1
increment_right()
print('2회 증가:', count)  # 2


# 실전 예제: 게임 점수 관리
print('\n=== 게임 점수 시스템 ===')
score = 0  # 전역 변수

def add_score(points):
    """점수를 추가하는 함수"""
    global score  # 전역 score 사용 선언
    score += points
    print(f'{points}점 획득! 현재 점수: {score}')

def reset_score():
    """점수를 초기화하는 함수"""
    global score
    score = 0
    print('점수 초기화!!')

# 게임 플레이
add_score(100)  # 100점 획득
add_score(200)  # 200점 추가
print(f'총점: {score}')  # 300

reset_score()  # 리셋
print(f'리셋 후: {score}')  # 0

# ==========================================
# 전역 변수 사용 주의사항
# ==========================================
print('\n=== 전역 변수 남용 예시 ===')

# 나쁜 예: 전역 변수 남용
total = 0
count = 0

def add_number(num):
    global total, count  # 여러 전역 변수 동시 사용
    total += num
    count += 1

def get_average():
    global total, count  # 또 전역 변수 사용
    return total / count if count > 0 else 0

# 좋은 예: 매개변수와 반환값 사용
def calculate_average(numbers):
    """전역 변수 없이 깔끔하게 평균 계산"""
    if not numbers:  # 빈 리스트면
        return 0
    return sum(numbers) / len(numbers)

# 사용 예시
numbers = [53, 56, 34, 64]
avg = calculate_average(numbers)
print(f'평균: {avg}')


# ==========================================
# 가변 타입 vs 불변 타입
# ==========================================
print('\n=== 가변/불변 타입 차이 ===')

# 불변 타입 (Immutable) 처리

def increment_num(num_copy):  # 복사본이 넘어옴
    """불변 타입은 함수 안에서 바꿔도 원본 안 바뀜"""
    num_copy += 1
    print(f'함수 안에서: {num_copy}')

# 불변 타입: 정수, 실수, 문자열, 튜플
num = 10
print('불변 타입 (정수):')
print(f'함수 호출 전: {num}')  # 10
increment_num(num)  # 11 (함수 안에서만)
print(f'함수 호출 후: {num}')  # 10 (원본 그대로!)


# 가변 타입 (Mutable) 처리

def num_append(numbers):  # 원본이 넘어옴
    """가변 타입은 함수 안에서 바꾸면 원본도 바뀜!"""
    numbers.append(6)  # 원본에 6 추가
    numbers[0] += 1    # 원본의 첫 번째 값 증가


# 가변 타입: 리스트, 딕셔너리, set
numbers = [1, 2, 3, 4, 5]
print('\n 가변 타입 (리스트):')
print(f'함수 호출 전: {numbers}')  # [1, 2, 3, 4, 5]
num_append(numbers)
print(f'함수 호출 후: {numbers}')  # [2, 2, 3, 4, 5, 6] (원본 변경!)

# 딕셔너리도 가변 타입
info_dic = {'name': '김철수', 'age': 20}

def change_info(info):
    """딕셔너리 정보 변경"""
    info['name'] = '이영희'  # 원본 수정
    info['age'] = 25        # 원본 수정

print('\n 가변 타입 (딕셔너리):')
print(f'함수 호출 전: {info_dic}')  # {'name': '김철수', 'age': 20}
change_info(info_dic)
print(f'함수 호출 후: {info_dic}')  # {'name': '이영희', 'age': 25}



# ==========================================
# 재귀 함수 (Recursive Function)
# ==========================================
print('\n' + '='*50)
print('재귀 함수 - 자기 자신을 호출하는 함수')
print('='*50)

'''
재귀 함수란?
- 함수가 자기 자신을 다시 호출하는 함수
- 러시아 인형처럼 같은 패턴이 반복될 때 사용

재귀 함수 필수 요소:
1. 기저 조건(Base Case): 언제 멈출지 (없으면 무한 반복!)
2. 재귀 호출(Recursive Call): 자기 자신 호출
'''

# 재귀 함수 기본 구조 (주석 처리)
"""
def recursive_function(n):
    # 1. 기저 조건 - 언제 멈출지
    if n == 종료_조건:
        return 기저값
    
    # 2. 재귀 호출 - 자기 자신 호출
    return recursive_function(n을_작게_만든_값)
"""

# 예제 1: 팩토리얼 계산
print('\n 팩토리얼 계산 (5! = 5x4x3x2x1)')

def factorial(n):
    """n! 계산하기"""
    # 기저 조건: 1! = 1, 0! = 1
    if n <= 1:
        return 1

    # 재귀 호출: n! = n × (n-1)!
    return n * factorial(n-1)

result = factorial(5)
print(f'5! = {result}')  # 120

# 실행 과정 설명
print('\n실행 과정:')
print('factorial(5) = 5 x factorial(4)')
print('= 5 x 4 x factorial(3)')
print('= 5 x 4 x 3 x factorial(2)')
print('= 5 x 4 x 3 x 2 x factorial(1)')
print('= 5 x 4 x 3 x 2 x 1')
print('= 120')


# 예제 2: 피보나치 수열
print('\n 피보나치 수열 (0, 1, 1, 2, 3, 5, 8, 13...)')

def fibonacci(n):
    """n번째 피보나치 수 구하기"""
    # 기저 조건
    if n <= 1:
        return n

    # 재귀 호출: F(n) = F(n-1) + F(n-2)
    return fibonacci(n-1) + fibonacci(n-2)

# 피보나치 수열 출력
print('피보나치 수열 (0~7번째):')
for i in range(8):
    print(f'F({i}) = {fibonacci(i)}')


# ==========================================
# 람다 함수 (Lambda Function)
# ==========================================
print('\n' + '='*50)
print('람다 함수 - 이름 없는 간단한 함수')
print('='*50)

'''
람다 함수란?
- 이름이 없는 한 줄짜리 간단한 함수
- 간단한 계산을 빠르게 처리할 때 사용
- lambda 매개변수: 표현식
'''

# 일반 함수 vs 람다 함수 비교
print('\n일반 함수 vs 람다 함수')

# 일반 함수
def square(x):
    return x ** 2

# 람다 함수 (같은 기능!)
def square_lambda(x): return x ** 2

print(f'일반 함수: square(5) = {square(5)}')
print(f'람다 함수: square_lambda(5) = {square_lambda(5)}')

# 여러 매개변수 람다
def add(x, y): return x + y

print(f'\n두 수 더하기: add(5, 3) = {add(5, 3)}')

# ==========================================
# 람다 함수 활용 (map, filter, sorted)
# ==========================================
print('\n=== 람다 함수 실전 활용 ===')

numbers = [1, 2, 3, 4, 5]

# 1. map(): 모든 요소에 함수 적용
print('\n map() - 모든 요소 제곱하기')
squared = list(map(lambda x: x ** 2, numbers))
print(f'원본: {numbers}')
print(f'제곱: {squared}')  # [1, 4, 9, 16, 25]

# 일반 함수로도 가능
def increment_fun(x):
    return x + 1

incre_numbers = list(map(increment_fun, numbers))
print(f'+1씩: {incre_numbers}')  # [2, 3, 4, 5, 6]

# 2. filter(): 조건에 맞는 요소만 선택
print('\n filter() - 3보다 큰 수만 선택')
evens = list(filter(lambda x: x > 3, numbers))
print(f'원본: {numbers}')
print(f'3보다 큰 수: {evens}')  # [4, 5]

# 3. sorted(): 정렬 기준 지정
print('\n sorted() - 학생 점수 정렬')

students = [
    {'name': "홍길동", 'score': 80},
    {'name': "김철수", 'score': 92},
    {'name': "이영희", 'score': 72}
]

# 점수순 정렬
students_by_score = sorted(students, key=lambda x: x['score'])
print('\n점수 낮은 순서:')
for student in students_by_score:
    print(f'{student["name"]}: {student["score"]}점')

# 이름순 정렬
students_by_name = sorted(students, key=lambda x: x['name'])
print('\n이름 순서:')
for student in students_by_name:
    print(f'  {student["name"]}: {student["score"]}점')

# ==========================================
# 핵심 정리
# ==========================================

'''
함수 심화 개념 핵심 정리

범위(Scope)
- 전역 변수: 어디서든 접근 가능
- 지역 변수: 함수 안에서만 사용
- global 키워드: 함수 안에서 전역 변수 수정

타입별 특성
- 불변 타입: 함수에서 바꿔도 원본 그대로
- 가변 타입: 함수에서 바꾸면 원본도 변경

재귀 함수
- 자기 자신을 호출하는 함수
- 반드시 종료 조건 필요!
- 예: 팩토리얼, 피보나치

람다 함수
- 이름 없는 한 줄 함수
- lambda 매개변수: 표현식
- map(), filter(), sorted()와 함께 자주 사용
'''
