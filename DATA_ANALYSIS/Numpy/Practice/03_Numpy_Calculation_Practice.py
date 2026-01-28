import numpy as np

print('=== 실전 예제: 학생 성적 처리 ===')

# 학생 성적 데이터
scores = np.array([45, 78, 92, 35, 88, 67, 55, 98, 42, 73])
print('학생 성적:', scores)
print()

# 1. 낙제자(60점 미만) 찾기
fail = scores[scores < 60]
print('낙제자 점수:', fail)
print('낙제자 수:', len(fail), '명')
print()

# 2. 등급 부여
grades = np.where(scores >= 90, 'A',
                  np.where(scores >= 80, 'B',
                           np.where(scores >= 70, 'C',
                                    np.where(scores >= 60, 'D', 'F'))))
print('등급:', grades)
print()

# 3. 보정 (60점 미만은 60점으로 상향)
adjusted = np.where(scores < 60, 60, scores)
print('보정 후 점수:', adjusted)
print()

# 4. 통계
print(f'평균: {scores.mean():.2f}점')
print(f'최고점: {scores.max()}점')
print(f'최저점: {scores.min()}점')
print(f'합격률: {(scores >= 60).sum() / len(scores) * 100:.1f}%')
