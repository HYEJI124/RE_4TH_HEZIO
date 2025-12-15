# Tuple 실습

# 실습 1. 손상된 고객 정보 복원하기
user = ("minji", 25, "Seoul")
restored_user = ("eunji", user[1], user[2])
print(restored_user)

# 실습 2. 고객 정보 언패킹하여 변수에 저장
name, age, city = restored_user
print(name, age, city, sep=', ')

# 실습 3. 지역별 보안 정책 분기 처리
if city == 'Seoul':
    print('서울 지역 보안 정책 적용 대상입니다.')
else:
    print('일반 지역 보안 정책 적용 대상입니다.')

# 실습 4. 고객 데이터 통계 분석
users = ("minji", "eunji", "soojin", "minji", "minji", "minji")

print('minji:', users.count('minji'))

print('soojin', users.index('soojin'))

# 실습 5. 고객 이름 정렬
sorted_users = sorted(users)
print('sorted_users', sorted_users)

# ----------------------------------------------------------------------------------------------
# Set 실습
 
# 문제 1. 중복 제거 및 개수 세기
submissions = ['kim', 'lee', 'kim', 'park', 'choi', 'lee', 'lee']
set_sub = set(submissions)

print('제출한 학생 수:', len(set_sub))
print('제출자 명단:', set_sub)

# 문제 2. 공통 관심사 찾기
user1 = {'SF', 'Action', 'Drama'}
user2 = {'Drama', 'Romance', 'Action'}

# 교집합
print('공통 관심 장르:', user1 & user2)
# 대칭차집합
print('서로 다른 장르:', user1 ^ user2)
# 합집합
print('전체 장르: ', user1 | user2)

# 문제 3. 부분집합 관계 판단
my_certificates = {"SQL", "Python", "Linux"}
job_required = {"SQL", "Python"}

print('지원 자격 충족 여부: ', my_certificates >= job_required)
