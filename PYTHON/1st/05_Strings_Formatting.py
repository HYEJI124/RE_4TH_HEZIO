# ========================================
# f-string을 이용한 문자열 포매팅
# ========================================

"""
f-string (f-문자열)은 Python 3.6부터 도입된 강력한 문자열 포매팅 방법
문자열 앞에 f를 붙이고, 중괄호 {} 안에 변수나 표현식을 넣어 사용
"""

student_age = 20
student_grade = 85.7

# f-string 사용법
print(f'학생의 나이는 {student_age}세이고, 성적은 {student_grade}점입니다.')

# 중괄호 안에서 계산도 가능
print(f'내년 나이: {student_age + 1}세')
print(f'성적 반올림: {round(student_grade)}점')


