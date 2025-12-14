# ========================================
# 자료형(Data Types) 상세 설명
# ========================================

"""
Python의 주요 자료형들:
1. 정수(int): 소수점이 없는 숫자 → 2, 3, 12, 25, -10
2. 실수(float): 소수점이 있는 숫자 → 1.1, 41.123, 3.1415
3. 문자(char): 한 글자 → 'a', 'B', '가' (Python에서는 길이 1인 문자열)
4. 문자열(str): 여러 글자의 조합 → "hello", "안녕하세요"
5. 불린(bool): 참/거짓 값 → True, False
"""

# 1. 정수형 (Integer)
student_count = 30              # 학생 수
temperature = -5                # 기온
year = 2024                     # 연도

# 2. 실수형 (Float)
pi = 3.14159                   # 원주율
average_score = 85.5           # 평균 점수
body_temperature = 36.5        # 체온

# 3. 문자열 (String)
greeting_message = "안녕하세요!"    # 인사말
programming_language = "Python"  # 프로그래밍 언어명

# 4. 불리언 (Boolean)
is_student = True             # 학생인가? (참)
is_adult = False              # 성인인가? (거짓)

# type() 함수로 자료형 확인
print(f"student_count의 타입: {type(student_count)}")       # <class 'int'>
print(f"pi의 타입: {type(pi)}")                           # <class 'float'>
print(f"greeting_message의 타입: {type(greeting_message)}")  # <class 'str'>
print(f"is_student의 타입: {type(is_student)}")           # <class 'bool'>

# ========================================
# 문자열에서 따옴표 사용하기
# ========================================

# 문자열 안에 따옴표를 포함시키는 방법들:

# 방법 1: 큰따옴표 안에 작은따옴표 사용
message1 = "'파이썬'은 가장 널리 사용되는 프로그래밍 언어입니다."
print(message1)

# 방법 2: 작은따옴표 안에 큰따옴표 사용
message2 = '"파이썬"은 가장 널리 사용되는 프로그래밍 언어입니다.'
print(message2)

# 방법 3: 이스케이프 문자(\) 사용
message3 = "\"파이썬\"은 최고의 언어입니다."
message4 = '\'파이썬\'은 최고의 언어입니다.'
print(message3)
print(message4)

# ========================================
# 불리언(Boolean) 자료형 상세
# ========================================

# 불리언 변수명은 is_, has_, can_ 등으로 시작하는 것이 관례
is_raining = True             # 비가 오고 있나요?
has_license = False           # 면허증이 있나요?
can_drive = True              # 운전할 수 있나요?

print(f'비가 오나요? {is_raining}, 타입: {type(is_raining)}')
print(f'면허증이 있나요? {has_license}, 타입: {type(has_license)}')
