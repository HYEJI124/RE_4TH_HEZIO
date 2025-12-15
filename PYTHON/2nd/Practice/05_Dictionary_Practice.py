# Dictionary 실습

# 문제 1
# 단계 1. user라는 이름의 빈 딕셔너리 생성

user = dict()
# user = {}
print()

# 단계 2. 사용자 기본 정보 추가
user['username'] = 'hyeji'
user['email'] = 'hyeji@example.com'
user['level'] = 5
print('user', user)
print()

# 단계 3. 값 읽기
email_value = user['email']
print('email_value', email_value)
print()

# 단계 4. 값 수정
user['level'] = 6
print('user', user)
print()

# 단계 5. 안전하게 키 조회
print(user.get('phone', '미입력'))
print()

# 단계 6. 항목 추가 및 삭제
user.update({'nickname': 'hezio'})
del user['email']
print(user.setdefault('signup_date', '2025-07-10'))
print('user', user)
print()

# 문제 2. 학생 점수 관리
students = {}

names = ['Alice', 'Bob', 'Charlie']
score = [85, 90, 95]

students = dict(zip(names, score))

students.update({'David': 80})
students['Alice'] = 88

del students['Bob']

print('students', students)
