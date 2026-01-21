# ================================
# 6. 기타 유용한 함수들
# ================================

'''
[1. zip() - 여러 시퀀스를 묶기]
같은 인덱스의 요소들을 튜플로 묶어줌
'''

names = ['김철수', '이영희', '박민수']
ages = [25, 24, 26]
cities = ['서울', '부산', '대구']

# 기본 사용법
zipped = list(zip(names, ages, cities))
for person_info in zipped:
    print(f'{person_info}')

# 딕셔너리 생성
person_dict = {name: age for name, age in zip(names, ages)}
print(f'이름-나이 딕셔너리: {person_dict}')

# 두 리스트를 딕셔너리로
keys = ['name', 'age', 'city']
values = ['김철수', 25, '서울']

person = dict(zip(keys, values))
print(f"생성된 딕셔너리: {person}")

# 길이가 다른 리스트 zip
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
zipped_different = list(zip(list1, list2))
print(f"{list1} + {list2} = {zipped_different}")
print('짧은 리스트 길이에 맞춰서 결합됨')

'''
[2. enumerate() - 인덱스와 값을 함께]
반복문에서 인덱스와 값을 동시에 사용할 때 유용
'''

fruits = ['사과', '바나나', '오렌지', '포도', '키위']

# 기본 사용법
for index, fruit in enumerate(fruits):
    print(f'{index}: {fruit}')

# 시작 인덱스 지정
for index, fruit in enumerate(fruits, start=1):
    print(f'{index}번째: {fruit}')

# 예제 1: 메뉴 선택
menu_items = ['신규 생성', '파일 열기', '저장', '다른 이름으로 저장', '종료']
for i, item in enumerate(menu_items, 1):
    print(f'{i}. {item}')

# 특정 조건의 인덱스 찾기
numbers = [10, 15, 8, 23, 42, 7, 30]
print(f"숫자 리스트: {numbers}")

even_indices = []
for i, num in enumerate(numbers):
    if num % 2 == 0: # 짝수인 경우
        even_indices.append((i, num))

print('짝수인 요소들')
for index, value in even_indices:
    print(f'인덱스 {index}: {value}')

'''
[3. range() - 숫자 범위 생성]
반복문과 함께 자주 사용되는 숫자 시퀀스 생성
'''

# 기본 사용법
print(f"range(5): {list(range(5))}")
print(f"range(2, 8): {list(range(2, 8))}")
print(f"range(0, 10, 2): {list(range(0, 10, 2))}")  # 짝수
print(f"range(10, 0, -1): {list(range(10, 0, -1))}")  # 역순

# 예제 1: 구구단 출력
for i in range(2, 6): # 2 - 5단까지
    print(f'{i}단', end=" ")
    for j in range(1, 10):
        print(f'{i} x {j} = {i*j}', end=' ')
    print()

# 예제 2: 피보나치 수열 생성(첫 10개)
fib = [0, 1]
for i in range(2, 10):
    next_fib = fib[i-1] + fib[i-2]
    fib.append(next_fib)
print(f'피보나치 수열: {fib}')

# 예제 3: 별 패턴 그리기
for i in range(1, 6):
    stars = '*' * i
    spaces = ' ' * (5-i)
    print(f'{spaces}{stars}')

'''
[4. map() - 함수를 모든 요소에 적용]
시퀀스의 모든 요소에 함수를 적용하여 새로운 이터레이터 반환
'''

# 기본 사용법
numbers_str = ['1', '2', '3', '4', '5']
numbers_int = list(map(int, numbers_str))
print(f"문자열 리스트: {numbers_str}")
print(f"정수 리스트: {numbers_int}")

# 함수와 함께 사용

def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
squared = list(map(square, numbers))
print(f'제곱 계산: {numbers} -> {squared}')

# lambda와 함께 사용
temperatures_f = [32, 68, 86, 104]  # 화씨온도
temperatures_c = list(map(lambda f: (f-32) * 5/9, temperatures_f))

print(f"화씨온도: {temperatures_f}")
print(f"섭씨온도: {[round(c, 1) for c in temperatures_c]}")

# 여러 리스트에 함수 적용
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

added = list(map(lambda x, y: x + y, list1, list2))
print(f'두 리스트 합: {list1} + {list2} = {added}')

# 예제 1: 데이터 전처리
user_inputs = ['  김철수  ', '  25  ', '  서울시  ']

cleaned_data = list(map(str.strip(), user_inputs))
print(f"원본: {user_inputs}")
print(f"정리됨: {cleaned_data}")

'''
[5. filter() - 조건에 맞는 요소만 필터링]
조건 함수가 True를 반환하는 요소만 남김
'''

# 기본 사용법
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
odds = list(filter(lambda x: x % 2 == 1, numbers))

print(f"전체 숫자: {numbers}")
print(f"짝수: {evens}")
print(f"홀수: {odds}")

# 문자열 필터링
words = ['python', 'java', 'c', 'javascript', 'go', 'ruby']
long_words = list(filter(lambda w: len(w) > 4, words))

print(f"프로그래밍 언어: {words}")
print(f"5글자 이상: {long_words}")

# 성적 필터링
students = [
    {'name': '김철수', 'score': 85},
    {'name': '이영희', 'score': 92},
    {'name': '박민수', 'score': 78},
    {'name': '최지연', 'score': 88},
    {'name': '정다영', 'score': 95}
]

# A학점 학생들 (90점 이상)
A_students = list(filter(lambda s: s['score'] >= 90, students))
print(f'A학점 학생들')
for student in A_students:
    print(f'{student['name']}: {student['score']}점')


# None 값 제거
mixed_list = [1, None, 2, '', 3, 0, 4, None, 5]
filtered = list(filter(None, mixed_list)) # False 값들 제거
print(f"원본: {mixed_list}")
print(f"False 제거: {filtered}")

'''
[6. all(), any() - 논리 검증 함수]
all(): 모든 요소가 True인지 확인
any(): 하나라도 True인지 확인
'''

# 기본 사용법
bool_list1 = [True, True, True, True]
bool_list2 = [True, False, True, True]
bool_list3 = [False, False, False, False]

# 논리값 리스트 검증
print(f"{bool_list1} → all(): {all(bool_list1)}, any(): {any(bool_list1)}")
print(f"{bool_list2} → all(): {all(bool_list2)}, any(): {any(bool_list2)}")
print(f"{bool_list3} → all(): {all(bool_list3)}, any(): {any(bool_list3)}")

# 숫자와 함께 사용
numbers = [2, 4, 6, 8, 10]
print(f'{numbers}가 모두 짝수인가? {all(x % 2 == 0 for x in numbers)}')

mixed_numbers = [1, 3, 5, 6, 7]
print(f'{mixed_numbers}에 짝수가 있나? {any(x % 2 == 0 for x in mixed_numbers)}')

# 예제 1: 폼 검증

def validate_user_data(data):
    """사용자 데이터 유효성 검사"""
    required_fields = ['name', 'email', 'phone']

    # 모든 필수 필드가 있는지 확인
    has_all_fieldes = all(field in data for field in required_fields)

    # 모든 필수 필드가 비어있지 않은지 확인
    all_fileds_filled = all(bool(data.get(field, '').strip()) for field in required_fields)

    return has_all_fieldes and all_fileds_filled

# 테스트 데이터
user_data1 = {'name': '김철수', 'email': 'kim@example.com',
              'phone': '010-1234-5678'}
user_data2 = {'name': '이영희', 'email': '', 'phone': '010-5678-1234'}
user_data3 = {'name': '박민수', 'email': 'park@example.com'}

print(f"사용자 데이터 검증")
for i, data in enumerate([user_data1, user_data2, user_data3], 1):
    is_valid = validate_user_data(data)
    print(f"데이터{i}: {'유효' if is_valid else '무효'} - {data}")

'''
[7. isinstance(), type() - 타입 확인]
객체의 타입을 확인하는 함수들
'''

# 다양한 타입의 객체들
objects = [
    42,
    3.14,
    "hello",
    [1, 2, 3],
    {'key': 'value'},
    (1, 2, 3),
    {1, 2, 3},
    True
]

# 타입 확인
for obj in objects:
    obj_type = type(obj)
    print(f' {obj:< 20} -> type: {obj_type.__name__}')

# isinstance 사용법
test_value = 42
print(f'isinstance({test_value}, int): {isinstance(test_value, int)}')
print(f'isinstance({test_value}, (int, float)): {isinstance(test_value,(int, float))}')
print(f'isinstance({test_value}, str): {isinstance(test_value, str)}')

# 안전한 함수 만들기
def safe_divide(a, b):
    """안전한 나누기 함수 - 타입 검증 포함"""
    # 타입 검증
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return '오류: 숫자만 입력 가능합니다.'
    
    # 0으로 나누기 방지
    if b == 0:
        return '오류: 0으로 나눌 수 없습니다.'
    
    return a / b

# 테스트
test_cases = [
    (10, 2),
    (15, 3),
    (10, 0),
    ("10", 2),
    (10, "2")
]

for a, b in test_cases:
    result = safe_divide(a, b)
    print(f'{a} + {b} = {result}')

'''
[8. dir(), help() - 객체 정보 확인]
객체의 속성과 메서드 확인, 도움말 보기
'''

# dir() 사용법 (실제 출력은 너무 길어서 일부만)
sample_string = 'hello'
string_methods = [method for method in dir(sample_string)
                  if not method.startswith('_')]
print(f'문자열의 주요 메소드들: {string_methods[:10]} ...')

# 실전에서 자주 사용하는 패턴 - 객체가 특정 메소드를 가지고 있는지 확인
test_objects = [
    ("문자열", "hello"),
    ("리스트", [1, 2, 3]),
    ("딕셔너리", {'a': 1})
]

for name, obj in test_objects:
    has_append = hasattr(obj, 'append')
    has_keys = hasattr(obj, 'keys')
    print(f'{name}: append 메소드 {'있음' if has_append else '없음'}, keys 메소드 {'있음' if has_keys else '없음'}')