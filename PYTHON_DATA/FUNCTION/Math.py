# ================================
# 2. 수학 관련 내장함수
# ================================

'''
[1. abs() - 절댓값]
음수를 양수로, 양수는 그대로
'''

# 절댓값 계산
numbers = [-10, -3.14, 0, 5, 15.7]
for num in numbers:
    print(f'abs({num}) = {abs(num)}')

# 두 점 사이의 거리
def distance_1d(x1, x2):
    """1차원에서 두 점 사이의 거리"""
    return abs(x2 - x1)

point_pairs = [(10, 3), (-5, 7), (0, -8)]
for x1, x2 in point_pairs:
    dist = distance_1d(x1, x2)
    print(f'점 {x1}과 점 {x2} 사이의 거리: {dist}')

'''
[2. round() - 반올림]
소수점 자리수 지정 가능
'''

# 다양한 반올림
values = [3.14159, 2.71828, 1.41421, 9.99999, 10.5, 11.5]
for val in values:
    print(f'{val} -> 정수: {round(val)}, 소수점 2자리: {round(val, 2)}')

# 성적 평균 계산
scores = [85.7, 92.3, 78.9, 88.1, 95.6]
average = sum(scores) / len(scores)
print(f'원점수들: {scores}')
print(f'평균: {average} -> 반올림: {round(average, 1)}')

'''
[3. min(), max() - 최솟값, 최댓값]
여러 값 또는 시퀀스에서 최솟값/최댓값 찾기
'''

# 여러 값에서 찾기
temp_today = [15.2, 18.7, 22.1, 19.8, 16.3]
print(f'오늘 온도 변화: {temp_today}')
print(f'최저 온도: {min(temp_today)}°C')
print(f'최고 온도: {max(temp_today)}°C')
print(f'온도 차: {max(temp_today) - min(temp_today):.1f}°C')

# 여러 인수로 사용
print(f'min(10, 5, 15, 3) = {min(10, 5, 15, 3)}')
print(f'max(10, 5, 15, 3) = {max(10, 5, 15, 3)}')

# 문자열에서 사용 (사전순)
names = ['김철수', '이영희', '박민수', '최지연']
print(f'이름 리스트: {names}')
print(f'사전순 첫 번째: {min(names)}')
print(f'사전순 마지막{max(names)}')

print('성적 분석')
student_scores = {
    '김철수': 85,
    '이영희': 92,
    '박민수': 78,
    '최지연': 88,
    '정다영': 95
}

# 점수만 추출해서 최고/최저 찾기
scores = student_scores.values()
min_score = min(scores)
max_score = max(scores)

# 최고/최저 점수 받은 학생 찾기
top_student = max(student_scores, key=student_scores.get)
bottom_student = min(student_scores, key=student_scores.get)

print(f"최고점: {max_score}점 ({top_student})")
print(f"최저점: {min_score}점 ({bottom_student})")

'''
[4. sum() - 합계]
숫자 시퀀스의 총합 계산
'''

# 기본 사용법
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(f'{numbers}의 합: {total}')

# 시작값 지정
total_with_start = sum(numbers, 100) # 100부터 더하기 시작
print(f'{numbers}의 합 (시작값 100): {total_with_start}')

# 예제 1: 쇼핑몰 장바구니
cart_items = {
    '노트북': 1200000,
    '마우스': 50000,
    '키보드': 120000,
    '모니터': 300000
}

for item, price in cart_items.items():
    print(f'{item}: {price:,}원')

total_price = sum(cart_items.values())
print(f'총 금액: {total_price:,}원')

# 할인 적용
if total_price >= 1000000:
    discount = total_price * 0.1 # 10% 할인
    final_price = total_price - discount
    print(f'할인액(10%): -{discount:,}원')
    print(f'최종 금액: -{final_price:,}원')