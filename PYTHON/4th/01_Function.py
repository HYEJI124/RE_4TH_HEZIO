# ==========================================
# 함수 (Function) 완벽 정리
# ==========================================

'''
함수란?
- 자주 쓰는 코드를 하나로 묶어놓은 것
- 이름을 붙여서 필요할 때마다 불러서 사용
- "요리 레시피"처럼 한 번 만들어두고 계속 재사용
'''

# ==========================================
# 함수를 왜 사용할까?
# ==========================================

'''
1. 코드 재사용성: 똑같은 코드 복사-붙여넣기 안 해도 됨
2. 모듈화: 큰 프로그램을 작은 조각으로 나누기
3. 가독성 향상: 코드가 뭘 하는지 이름만 봐도 알 수 있음
4. 유지보수 용이: 고칠 때 함수 하나만 수정하면 끝
5. 추상화: 복잡한 내용을 간단하게 사용
'''

# ==========================================
# 함수 사용 전 - 반복의 고통
# ==========================================
print('=' * 20)
print('첫 번째 섹션')
print('=' * 20)

print('=' * 20)
print('두 번째 섹션')
print('=' * 20)

# 똑같은 형식을 복사-붙여넣기 반복

# ==========================================
# 함수 사용 - 깔끔하게 해결!
# ==========================================

def print_section(title):  # 함수 만들기 (레시피 작성)
    print('=' * 20)
    print(f'{title} 섹션')
    print('=' * 20)

# 필요할 때마다 호출
print_section('첫 번째')  # 함수 사용 1
print_section('두 번째')  # 함수 사용 2

# ==========================================
# 함수 정의와 호출 기본
# ==========================================

# 함수 정의(Definition) - 함수 만들기
'''
기본 형태

def 함수이름(매개변수):
    # 실행할 코드
    return 반환값
'''

# 1. 가장 간단한 함수 - 매개변수도 반환값도 없음

def say_hello():  # 함수 정의 (만들기)
    print("안녕하세요!")

say_hello()  # 함수 호출 (사용하기)

# 2. 매개변수가 있는 함수 - 입력을 받아서 처리

def greet(name):  # name: 매개변수 (받을 값의 이름)
    print(f'안녕하세요. {name}님!')

greet('김철수')  # '김철수'는 인자 (실제로 넘기는 값)
greet('이영희')  # 같은 함수로 다른 이름 출력

# 3. 반환값이 있는 함수 - 결과를 돌려줌

def add(a, b):  # 두 개의 매개변수
    result = a + b  # 계산
    return result   # 결과를 돌려줌

sum_result = add(3, 5)  # 반환된 값을 변수에 저장
print('sum_result:', sum_result)  # 8
print('add(10, 5):', add(10, 5))  # 바로 출력도 가능


# ==========================================
# 실전 예제: 사각형 넓이 구하기
# ==========================================

def calculate_area(width, height):
    """
    Docstring(문서화 문자열)
    함수가 뭘 하는지 설명

    직사각형의 넓이를 계산합니다.

    Parameters:
        width(float): 직사각형의 너비
        height(float): 직사각형의 높이

    Return:
        float: 직사각형의 넓이
    """
    return width * height  # 너비 x 높이

print('10x20 직사각형 넓이:', calculate_area(10, 20))  # 200

# Docstring 확인하는 방법
print('\n함수 설명 보기:')
print(calculate_area.__doc__)  # 함수 설명 출력
# help(calculate_area)  # 더 자세한 도움말 (주석 해제하면 실행)


# ==========================================
# 매개변수(Parameter) vs 인자(Argument)
# ==========================================

'''
헷갈리기 쉬운 용어 정리:
- 매개변수(Parameter): 함수 만들 때 쓰는 변수 이름
- 인자(Argument): 함수 호출할 때 넣는 실제 값
'''

def multiply(x, y):  # x, y는 매개변수 (이름표)
    return x * y

result = multiply(3, 5)  # 3, 5는 인자 (실제 값)


# ==========================================
# 위치 인자 (순서가 중요!)
# ==========================================

def introduce(name, age, city):
    print(f"이름: {name}, 나이: {age}, 도시: {city}")

# 순서대로 값이 들어감
introduce('김철수', 25, '서울')
# name='김철수', age=25, city='서울'

# ==========================================
# 키워드 인자 (이름표로 전달)
# ==========================================
# 같은 함수인데 이름을 써서 전달
introduce(city='서울', age=25, name='김철수')
# 순서가 바뀌어도 괜찮음(이름표가 있으니까)

# 위치 인자와 키워드 인자 섞어 쓰기
introduce('김철수', city='서울', age=25)
# <주의> 위치 인자가 키워드 인자보다 앞에 와야 함!

# introduce(20, city='부산', name='이영희')  # 에러!


# ==========================================
# 반환값 (return) 자세히 알아보기
# ==========================================

# 1. 단일 값 반환

def square(n):
    return n ** 2  # n의 제곱

result = square(5)
print('5의 제곱:', result)  # 25

# 2. 여러 값 한 번에 반환

def calculate_stats(numbers):
    """숫자 리스트의 통계를 계산"""
    total = sum(numbers)      # 합계
    avg = total / len(numbers)  # 평균
    max_num = max(numbers)      # 최대값
    min_num = min(numbers)      # 최소값

    # 4개 값을 한번에 반환!
    return total, avg, max_num, min_num

numbers = [100, 140, 230, 200]  # 테스트 데이터

# 각각의 변수로 받기
total, avg, maxnum, minnum = calculate_stats(numbers)

print('합계:', total)    # 670
print('평균:', avg)      # 167.5
print('최대값:', maxnum)  # 230
print('최소값:', minnum)  # 100

# 튜플로 한번에 받기
stats = calculate_stats(numbers)
print('전체 결과:', stats)  # (670, 167.5, 230, 100)


# ==========================================
# return의 특징 - 함수 종료
# ==========================================

def check_positive(number):
    if number > 0:
        return "양수"
    elif number < 0:
        return '음수'
    else:
        return '0'

    # 이 코드는 절대 실행 안 됨! (return 후에는 함수 끝)
    print('실행 안되는 코드')

print(check_positive(4))   # "양수"
print(check_positive(-1))  # "음수"
print(check_positive(0))   # "0"


# 조기 반환(Early Return) - 문제 상황 먼저 처리

def divide(a, b):
    # 문제가 될 상황을 먼저 체크!
    if b == 0:
        return "0으로 나눌 수 없습니다."

    # 정상적인 경우
    return a / b

print(divide(10, 2))  # 5.0
print(divide(10, 0))  # "0으로 나눌 수 없습니다."


# ==========================================
# 기본값 매개변수
# ==========================================

def greet(name, greeting='안녕하세요'):  # greeting에 기본값 설정
    print(f'{greeting}, {name}님')

greet('김철수')  # 기본값 사용: "안녕하세요, 김철수님"
greet('이영희', '반갑습니다')  # 다른 값: "반갑습니다, 이영희님"


# 여러 개의 기본값 사용
def create_profile(name, age=25, city='서울', job='개발자'):
    """프로필 만들기 (대부분 기본값 사용)"""
    return {
        'name': name,  # 필수 입력값!
        'age': age,    # 기본값: 25
        'city': city,  # 기본값: 서울
        'job': job     # 기본값: 개발자
    }

print(create_profile('박민수'))  # 이름만 주고 나머지는 기본값
# {'name': '박민수', 'age': 25, 'city': '서울', 'job': '개발자'}

print(create_profile('김철수', 30))  # 이름과 나이만 변경
# {'name': '김철수', 'age': 30, 'city': '서울', 'job': '개발자'}

print(create_profile('이영희', job='모델'))  # 이름과 직업만 변경
# {'name': '이영희', 'age': 25, 'city': '서울', 'job': '모델'}

# ==========================================
# 가변 위치 인자 (*args) - 개수 제한 없음!
# ==========================================

def sum_all(*numbers):  # *가 붙으면 여러 개를 받을 수 있음
    """몇 개든 받아서 모두 더하기"""
    print(f'받은 값들: {numbers} (타입: {type(numbers)})')

    total = 0
    for num in numbers:
        total += num  # 하나씩 더하기
    return total

print('합계:', sum_all(1, 2, 3))  # 3개 전달
print('합계:', sum_all(1, 2, 3, 4, 5, 6, 7, 8))  # 8개 전달
print('합계:', sum_all())  # 0개도 가능!


# ==========================================
# 가변 키워드 인자 (**kwargs) - 이름 있는 여러 값
# ==========================================

def print_info(**user):  # **가 붙으면 키워드 인자 여러 개
    """받은 정보를 모두 출력"""
    print(f'받은 정보: {user} (타입: {type(user)})')

    # 딕셔너리로 받아서 하나씩 출력
    for key, value in user.items():
        print(f'{key}: {value}')

print_info(name='김철수', age=20, city='서울')

'''
받은 정보: {'name': '김철수', 'age': 20, 'city': '서울'}

출력
name: 김철수
age: 20
city: 서울
'''

# 실전 예제: 유연한 학생 정보 생성

def create_student(**info):
    """학생 정보를 유연하게 생성"""
    student = {
        "name": info['name'],  # 필수 항목
        "age": info.get('age', 20),  # 없으면 20 사용
        "grade": info.get('grade', 1),  # 없으면 1학년
        "subjects": info.get('subjects', []),  # 없으면 빈 리스트
    }
    return student

student1 = create_student(name='김철수', subjects=['python'])
print('학생1:', student1)
# {'name': '김철수', 'age': 20, 'grade': 1, 'subjects': ['python']}

# ==========================================
# 함수 핵심 정리
# ==========================================

'''
함수는 "재사용 가능한 코드 조각"

1. 함수 기본
def 함수명(매개변수):
  실행 코드
  return 반환값

인자 전달 방식
- 위치 인자: 순서대로 전달
- 키워드 인자: 이름으로 전달
- 기본값: 자동으로 들어가는 값

특수 매개변수
- *args: 위치 인자 여러 개 (튜플)
- **kwargs: 키워드 인자 여러 개 (딕셔너리)

return 특징
- 함수를 즉시 종료
- 여러 값 반환 가능
- 없으면 None 반환
'''