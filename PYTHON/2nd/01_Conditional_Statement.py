# ===========================
# 1. if 조건문 기초
# ===========================

age = 20

# age가 18 이상이면 성인 출력
if age >= 18:
    print("성인입니다.")


# ===========================
# 2. 문자열을 조건으로 사용
# ===========================

name = "HYEJI"
name = ""  # 빈 문자열로 바꿨으므로 False로 평가됨

# 문자열이 비어 있지 않으면 True → 출력
if name:
    print("이름이 존재합니다.")  # 출력되지 않음 (name은 "")


# ===========================
# 3. True / False 조건문
# ===========================

if True:
    print("무조건 실행")  # 항상 실행됨

if False:
    print("실행되지 않습니다.")  # 실행 안됨

if True:
    pass  # 실행할 코드가 없을 때 pass 사용
print('조건문과는 상관없습니다.')  # if와 상관없이 항상 실행


# ===========================
# 4. 단축 평가 (Short-Circuit Evaluation)
# ===========================

# and : 앞 조건이 False면 뒤 조건은 확인하지 않음
# 따라서 print("단축 평가")는 실행되지 않음
if False and print("단축 평가"):
    print('실행')

# or : 앞 조건이 False면 뒤 조건을 확인함
# print("단축 평가")가 실행되고, 그 결과 None(False 취급)이지만
# 마지막 True 때문에 조건문이 실행됨
if False or print("단축 평가") or True:
    print('실행')


# ===========================
# 5. if ~ else 기본
# ===========================

name = ""  # 빈 문자열 → False 취급됨

if name:
    print(f'이름은: {name}')
else:
    print('이름을 작성해주세요')  # 실행됨

if False:
    print('if 실행')
else:
    print('else 실행')  # 실행됨


# ===========================
# 6. if ~ elif ~ else (다중 조건문)
# ===========================

name = '철수'

if name == '김철수':
    print(f'김철수 입니다.')
elif name == '철수':
    print(f'철수 입니다.')
else:
    print('이름을 입력해주세요.')


# ===========================
# 7. 나이와 학년 조건문
# ===========================

age = 20
name = '철수'
grade = 2

# name이 빈 문자열이 아니므로 True → 출력됨
if name:
    print(f'이름: {name}')

# 나이가 20보다 큰지 검사
if age > 20:
    print('성인입니다.')
else:
    print('미성년자입니다.')  # age = 20이므로 else 실행

# 학년 검사
if grade >= 3:
    print('3학년 입니다')
elif grade == 2:
    print('2학년 입니다')  # grade = 2이므로 실행
else:
    print('1학년 입니다')


if True:
    if True:
        if True:
            pass
        if True:
            pass
        if True:
            pass
