# ==========================================
# 반복문 제어하기 (break, continue, pass)
# ==========================================

'''
반복문 제어 키워드란?
- break: "그만! 여기서 나가자" (반복문 완전 종료)
- continue: "이번 건너뛰고 다음" (이번 반복만 건너뛰기)
- pass: "아무것도 안 해" (자리만 채우기)
'''

# ==========================================
# break - 반복문 탈출하기
# ==========================================
print('==== break =====')

# 예제 1: i가 2가 되면 반복문 종료
for i in range(3):  # 원래는 0, 1, 2 출력해야 함
    if i == 2:
        # i가 2가 되는 순간 "그만!"
        break  # 여기서 for문 완전히 끝! 밑에 코드도 실행 안 함
    print(i)  # 0, 1만 출력됨 (2는 break 때문에 출력 안 됨)
print()

# 예제 2: 첫 번째 반복에서 바로 종료
for i in range(10):  # 원래는 0~9까지 출력해야 함
    print(i)  # 0만 출력
    break     # 첫 번째 반복에서 바로 "그만!"
    # 이 아래 코드는 절대 실행되지 않음

print('for문 종료')
print()

# break 활용 예시: 특정 조건에서 검색 중단
print('break 실전 예시 - 찾으면 멈추기')
numbers = [1, 3, 5, 7, 9, 11, 13]
target = 7

for num in numbers:
    print(f'검색중... {num}')
    if num == target:
        print(f'{target}을 찾았어요!')
        break  # 찾았으니 더 이상 검색할 필요 없음
print()

# ==========================================
# continue - 건너뛰기
# ==========================================
print('==== continue =====')

# 예제 1: 홀수는 건너뛰고 짝수만 출력
for i in range(10):  # 0~9까지
    if i % 2:  # i를 2로 나눈 나머지가 있으면 (=홀수면)
        continue  # "이번건 패스! 다음거 해"
        # continue 아래 코드는 실행 안 됨
    print(i)  # 짝수만 출력: 0, 2, 4, 6, 8
print()

# continue 활용 예시: 특정 값 제외하고 처리
print('continue 실전 예시 - 음수 제외하기')
scores = [85, -1, 92, 78, -999, 88]  # -1과 -999는 오류값

for score in scores:
    if score < 0:  # 음수는 오류값이니까
        print(f'{score}는 잘못된 점수, 건너뜀')
        continue  # 이번 점수는 무시하고 다음 점수로
    print(f'유효한 점수: {score}점')
print()

# ==========================================
# pass - 아무것도 안 하기
# ==========================================
print('==== pass =====')

# 예제 1: pass는 아무것도 안 함
for i in range(10):
    pass      # 그냥 통과(아무 일도 안 일어남)
    print(i)  # 0~9 모두 정상 출력
print()

# pass 활용 예시: 나중에 구현할 코드 자리 채우기
print('pass 실전 예시 - 미완성 코드')

def process_data(data):
    if data > 100:
        pass  # TODO: 나중에 여기 특별 처리 코드 넣을 예정
    else:
        print(f'데이터 처리: {data}')

process_data(50)   # 정상 처리
process_data(150)  # pass라서 아무 일 안 일어남
print()

# ==========================================
# for-else: 특별한 기능
# ==========================================
print('==== for - else =====')

# break로 종료되지 않고 정상 종료되면 else 실행
for i in range(10):
    print(i)
    if i == 3:
        break  # i가 3일 때 강제 종료
else:
    # break 때문에 이 부분은 실행 안 됨!
    print('루프 정상 종료')
print()

# for-else 활용: 검색 실패 감지
print('for-else 실전 예시 - 못 찾았을 때 처리')
items = ['사과', '바나나', '딸기']
search_item = '수박'

for item in items:
    if item == search_item:
        print(f'{search_item}을 찾았습니다!')
        break
else:
    # break가 안 됐다 = 못 찾았다
    print(f'{search_item}을 찾을 수 없습니다.')
print()

# ==========================================
# 중첩 반복문 (반복문 안의 반복문)
# ==========================================
print('==== 중첩 반복문 =====')

colors = ['red', 'blue']
fruits = ['apple', 'banana']

# 모든 색상과 과일 조합 만들기
for color in colors:           # 색상 하나씩
    for fruit in fruits:        # 각 색상마다 모든 과일 조합
        print(f'{color} {fruit}')
# 결과:
# red apple
# red banana
# blue apple
# blue banana

# 리스트 컴프리헨션으로 같은 결과 만들기 (고급 기법)
new_list = [(c, f) for c in colors for f in fruits]
print('리스트 컴프리헨션 결과:', new_list)
print()

# ==========================================
# break vs continue vs pass 비교
# ==========================================
print('='*50)
print('break vs continue vs pass 한눈에 비교')
print('='*50)

# break 예시
print('break: 1~5 중에 3에서 멈추기')
for i in range(1, 6):
    if i == 3:
        print('→ break! 여기서 끝!')
        break
    print(f'숫자: {i}')
print()

# continue 예시
print('continue: 1~5 중에 3만 건너뛰기')
for i in range(1, 6):
    if i == 3:
        print('→ continue! 3은 건너뜀')
        continue
    print(f'숫자: {i}')
print()

# pass 예시
print('pass: 1~5 모두 출력 (pass는 아무 영향 없음)')
for i in range(1, 6):
    if i == 3:
        pass  # 아무것도 안 함
    print(f'숫자: {i}')
print()

# ==========================================
# 실전 활용 예제
# ==========================================
print('='*50)
print('실전 활용 예제')
print('='*50)

# 실전 1: 비밀번호 검증 (break 활용)
print('\n비밀번호 검증')
passwords = ['1234', 'abcd', 'secret', 'python']
correct_pass = 'secret'

for idx, pwd in enumerate(passwords, 1):
    print(f'시도 {idx}: {pwd}', end=' ')
    if pwd == correct_pass:
        print('비밀번호가 일치합니다!')
        break
    print('비밀번호가 틀렸습니다')

# 실전 2: 유효한 데이터만 처리 (continue 활용)
print('\n 성적 평균 구하기 (잘못된 데이터 제외)')
scores = [85, -1, 92, 200, 78, -999, 88]  # -1, 200, -999는 오류
valid_scores = []

for score in scores:
    if score < 0 or score > 100:  # 잘못된 점수
        print(f'{score}는 무시 (0~100 범위 벗어남)')
        continue
    valid_scores.append(score)
    print(f'{score}점 추가')

if valid_scores:
    average = sum(valid_scores) / len(valid_scores)
    print(f'평균: {average:.1f}점')

# ==========================================
# 핵심 정리
# ==========================================
'''
반복문 제어 핵심 정리

break
- 반복문을 완전히 종료
- "찾았으니 그만 찾자"
- 사용처: 검색, 조건 만족시 종료

continue  
- 현재 반복만 건너뛰고 다음 반복 진행
- "이건 패스하고 다음거"
- 사용처: 특정 조건 제외, 필터링

pass
- 아무것도 하지 않음 (빈 자리 채우기용)
- "일단 비워두고 나중에"
- 사용처: 미완성 코드, 예외 무시

for-else
- break 없이 정상 종료시 else 블록 실행
- "끝까지 다 돌았는데 못 찾았네"
- 사용처: 검색 실패 감지
'''
