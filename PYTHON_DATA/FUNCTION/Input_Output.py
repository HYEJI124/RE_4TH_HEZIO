# ================================
# 5. 입출력 함수
# ================================

'''
[1. print() - 출력 함수의 활용]
'''

# 기본 구분자 변경
print('기본:', 1, 2, 3, 4, 5)
print('쉼표:', 1, 2, 3, 4, 5, sep=',')
print('대시:', 1, 2, 3, 4, 5, sep='-')
print('구분자 없이:', 1, 2, 3, 4, 5, sep='')

# 끝 문자 변경
print('첫 번째 줄', end=' ')
print('같은 줄 계속')
print('새 줄에서', end='!!!\n')
print('다음줄')

# 다양한 출력 방법
name = "김철수"
age = 25
score = 85.67

print(f'f-string: {name}님은 {age}세이고 점수는 {score:.1f}점입니다.')
print('format: {}님은 {}세이고 점수는 {:.1f}점입니다.'.format(name, age, score))
print('% 포매팅: %s님은 %d세이고 점수는 %.1f점입니다.' % (name, age, score))

# 표 형태 출력
students_data = [
    ('김철수', 25, 85.67),
    ('이영희', 24, 92.45),
    ('박민수', 26, 78.23)
]

print(f'{'이름':<10} {'나이':<5} {'점수':<8}')
for name, age, score in students_data:
    print(f'{name:<10} {age:<5} {score:<8.2f}')

'''
[2. input() - 타입 변환과 함께 사용하는 패턴들]
'''

# 정수 입력받기
age = int(input('나이를 입력하세요: '))

# 실수 입력받기
height = float(input('키를 입력하세요(cm): '))

# 여러 값을 한 번에 입력받기
numbers = input('숫자들을 공백으로 구분해서 입력: ').split()
numbers = [int(x) for x in numbers]

# 예/아니오 입력받기
answer = input('계속하시겠습니까? (y/n): ').lower().strip()
continue_flag = answer in ['y', 'yes', '예', 'ㅇ']