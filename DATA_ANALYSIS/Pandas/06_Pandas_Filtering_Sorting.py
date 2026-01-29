import pandas as pd
import numpy as np

# 1: 조건 필터링 (Conditional Filtering)
# Boolean Indexing을 사용하여 원하는 조건의 데이터만 선택

df = pd.DataFrame({
    '이름': ['민준', '서연', '지후', '서준', '지민'],
    '점수': [78, 92, 85, 60, 88],
    '반': [1, 2, 1, 2, 1]
})

# 문제 1: 단일 조건 필터링
'''
점수가 80점 이상인 학생만 추출
df['점수'] >= 80 → Boolean Series [False, True, True, False, True]
df[Boolean Series] → True인 행만 선택
'''
print("1. 점수 80점 이상:")
print(df[df['점수'] >= 80])
print()

# 문제 2: 다중 조건 필터링 (AND 연산)
'''
& 연산자: 두 조건을 모두 만족 (AND)
주의: 각 조건을 괄호()로 묶어야 함!
(df['반'] == 1) AND (df['점수'] >= 85)
'''
print("2. 1반이면서 점수 85점 이상:")
print(df[(df['반'] == 1) & (df['점수'] >= 85)])
# 결과: 지후(1반, 85점), 지민(1반, 88점)
print()

# 문제 3: 다중 조건 필터링 (OR 연산)
'''
| 연산자: 둘 중 하나만 만족 (OR)
'''
print("3-1. 이름이 '서연' 또는 '지민' (OR 사용):")
print(df[(df['이름'] == '서연') | (df['이름'] == '지민')])
print()

'''
isin() 메소드: 여러 값 중 하나라도 포함되면 True
OR 연산보다 간결하고 가독성이 좋음
'''
print("3-2. 이름이 '서연' 또는 '지민' (isin 사용):")
print(df[df['이름'].isin(['서연', '지민'])])
# isin(['서연', '지민']) → ['서연', '지민'] 리스트에 포함된 값 찾기
print()

# 문제 4: 인덱스 재정렬 (reset_index)

# 필터링 후 인덱스가 불연속적일 때 0부터 재정렬
df_isin = df[df['이름'].isin(['서연', '지민'])]
print("4-1. 필터링 후 (인덱스 불연속):")
print(df_isin)  # 인덱스: 1, 4

'''
reset_index(): 인덱스를 0부터 재정렬
기존 인덱스는 'index'라는 새 컬럼으로 추가됨
'''
df_isin = df_isin.reset_index()
print("4-2. reset_index() 후:")
print(df_isin)  # 인덱스: 0, 1 / 기존 인덱스는 'index' 컬럼에 저장
print()

'''
reset_index(drop=True): 기존 인덱스를 버리고 재정렬
일반적으로 이 방법을 더 많이 사용
'''
df_isin_dropped = df[df['이름'].isin(['서연', '지민'])].reset_index(drop=True)
print("4-3. reset_index(drop=True) 후:")
print(df_isin_dropped)  # 인덱스: 0, 1 / 기존 인덱스 제거됨
print()

# 문제 5: 복합 조건 (OR)

# 점수가 80점 미만 OR 2반인 학생
print("5. 점수 80점 미만이거나 2반:")
result = df[(df['점수'] < 80) | (df['반'] == 2)]
print(result)
# 결과: 민준(78점), 서연(2반), 서준(2반, 60점)
print()

# 문제 6: 연속 필터링 (Chaining)

# 첫 번째 필터링 결과에서 추가 필터링 수행
print("6. 문제 5 결과에서 점수 70점 이상만 재추출:")
result = result[result['점수'] >= 70].reset_index(drop=True)
print(result)
# 결과: 민준(78점), 서연(92점)
# 서준(60점)은 제외됨
print()

'''
조건 필터링 핵심 정리:
┌─────────────┬──────────────┬─────────────────┐
│ 연산자        │ 의미          │ 예시             │
├─────────────┼──────────────┼─────────────────┤
│ &           │ AND (그리고)   │ (조건1) & (조건2) │
│ |           │ OR (또는)     │ (조건1) | (조건2) │
│ ~           │ NOT (부정)    │ ~(조건1)         │
│ ==          │ 같음          │ df['A'] == 10   │
│ !=          │ 다름          │ df['A'] != 10   │
│ >  >=  <  <=│ 크기 비교      │ df['A'] >= 80   │
│ isin()      │ 목록 포함      │ df['A'].isin([])│
└─────────────┴──────────────┴─────────────────┘

주의사항:
- 조건마다 괄호() 필수!
- and/or 대신 &/| 사용 (Python 예약어는 사용 불가)
- 여러 값 비교 시 isin() 사용 권장
'''

# 2: 행(Row)과 열(Column) 추가/삭제

df = pd.DataFrame({
    '이름': ['김철수', '이영희', '박민수'],
    '국어': [90, 80, 70]
})

# 문제 1: 열(Column) 추가
'''
새 열 추가: df['새열이름'] = 값
값: 리스트, 단일값, Series 등 가능
'''

print("1. '수학' 열 추가:")
df['수학'] = [95, 100, 88]  # 리스트 길이는 행 개수와 동일해야 함
print(df)
print()

# 문제 2: 열(Column) 삭제
'''
drop(컬럼명, axis=1): 열 삭제
axis=1: 열 방향, axis=0: 행 방향
'''

print("2. '이름' 열 삭제:")
df = df.drop('이름', axis=1)
print(df)
print()
'''
# 주의: drop()은 원본을 변경하지 않음 → 재할당 필요
# 또는 df.drop('이름', axis=1, inplace=True) 사용
'''

# 문제 3: 행(Row) 추가 방법 - 1) concat()

df = pd.DataFrame({
    '제품': ['A', 'B'],
    '가격': [1000, 2000]
})

'''
concat(): 여러 DataFrame을 합치기
ignore_index=True: 인덱스를 0부터 재정렬
'''

print("3-1. concat()으로 행 추가:")
new_row = pd.DataFrame({
    '제품': ['C'],
    '가격': [1500]
})
df = pd.concat([df, new_row], ignore_index=True)
print(df)
print()

# 문제 3: 행(Row) 추가 방법 - 2) loc[]

'''
loc[인덱스번호] = [값들]: 특정 위치에 행 추가
len(df): 현재 행 개수 → 다음 인덱스 번호
'''

print("3-2. loc[]으로 행 추가:")
df.loc[len(df)] = ['D', 2500]
# len(df) = 3 → df.loc[3] = ['D', 2500]
print(df)
print()

'''
행 추가 방법 비교:
┌─────────────┬────────────┬────────────────┐
│ 방법         │ 장점        │ 단점            │
├─────────────┼────────────┼────────────────┤
│ concat()    │ 안전, 명확   │ 코드 길이 긺      │
│ loc[]       │ 간결        │ 컬럼 순서 주의    │
│ append()    │ 직관적       │ deprecated됨   │
└─────────────┴────────────┴────────────────┘
권장: concat() 또는 loc[] 사용
'''

# 문제 4: 행(Row) 삭제

'''
drop(인덱스번호): 특정 행 삭제
axis=0 (기본값): 행 삭제
'''

print("4. 0번 행 삭제:")
df = df.drop(0)  # 인덱스 0번 행 삭제
print(df)
print()

# 문제 5: 조건에 맞는 행 삭제

df = pd.DataFrame({
    '과목': ['국어', '영어', '수학'],
    '점수': [85, 90, 78]
})

print("5. 점수 80 미만 행 삭제:")

# 방법 1: 필터링으로 원하는 행만 남기기 (간단!)
df = df[df['점수'] >= 80]

# 방법 2: drop()과 조건 인덱스 사용 (명시적)
df = df.drop(df[df['점수'] < 80].index)
print(df)
print()
'''
df[df['점수'] < 80].index → 조건에 맞는 행의 인덱스 번호
drop(인덱스 리스트) → 해당 인덱스 행들 삭제
'''

# 문제 6: 모든 행에 같은 값을 가진 열 추가

print("6. '학년' 열 추가 (모든 값 1):")
df['학년'] = 1  # 스칼라 값은 모든 행에 자동으로 브로드캐스팅됨
print(df)
print()

# 문제 7: 새 열과 함께 행 추가 (결측값 포함)

df = pd.DataFrame({
    '이름': ['A', 'B'],
    '나이': [20, 22]
})

'''
기존 DataFrame에 없던 열('키')을 포함한 행 추가
기존 행의 '키' 열은 자동으로 NaN으로 채워짐
'''

print("7. 새 열('키')을 포함한 행 추가:")

new_row = pd.DataFrame({
    '이름': ['C'],
    '나이': [25],
    '키': [np.nan]  # np.nan: NumPy의 결측값
})

df = pd.concat([df, new_row], ignore_index=True)
print(df)
'''
결과

  이름  나이   키
0  A   20  NaN  ← 기존 행, '키' 자동 추가됨
1  B   22  NaN  ← 기존 행
2  C   25  NaN  ← 새 행
'''
print()

# 문제 8: 조건 필터링으로 행 삭제

df = pd.DataFrame({
    '부서': ['영업', '기획', '개발', '디자인'],
    '인원': [3, 2, 5, 1]
})

print("8. 인원 2명 이하 행 삭제:")

df = df[df['인원'] > 2]  # 인원이 3명 이상인 행만 남김
print(df)
# 결과: 영업(3명), 개발(5명)만 남음
print()

# 문제 9: 열 추가 (모든 값 동일)

print("9. '평가' 열 추가 (모든 값 '미정'):")

df['평가'] = '미정'  # 문자열도 브로드캐스팅 가능
print(df)
print()

# 3: 정렬 (Sorting) - DataFrame의 행이나 열을 특정 기준으로 정렬

df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David'],
    'score': [88, 95, 70, 100]
})

# 문제 1: 단일 열 기준 오름차순 정렬

'''
sort_values(by='컬럼명'): 특정 열을 기준으로 정렬
기본값: ascending=True (오름차순)
'''

print("1. score 오름차순 정렬:")
print(df.sort_values(by='score'))
# 결과: 70 → 88 → 95 → 100
print("원본 확인 (변경 안 됨):")
print(df)
print()
'''
주의: sort_values()는 원본을 변경하지 않음
변경하려면: df = df.sort_values(...) 또는 inplace=True
'''

# 문제 2: 내림차순 정렬 + 인덱스 재정렬

'''
ascending=False: 내림차순 정렬
reset_index(drop=True): 인덱스를 0부터 재정렬
'''

print("2. score 내림차순 정렬 + 인덱스 재정렬:")
print(df.sort_values(by='score', ascending=False).reset_index(drop=True))
# 결과: 100 → 95 → 88 → 70 (인덱스: 0, 1, 2, 3)
print()

# 문제 3: 다중 열 기준 정렬

df = pd.DataFrame({
    '이름': ['가', '나', '다', '라', '마'],
    '반': [2, 1, 1, 2, 1],
    '점수': [90, 85, 80, 95, 85]
})

'''
sort_values(by=['열1', '열2']): 여러 열 기준 정렬
ascending=[True, False]: 각 열마다 다른 정렬 방향
'''

print("3. 반 오름차순 → 점수 내림차순:")

print(df.sort_values(by=['반', '점수'], ascending=[True, False]))
print()

'''
정렬 순서
1) 먼저 '반'을 오름차순 (1반 → 2반)
2) 같은 반 내에서 '점수'를 내림차순

결과
1반: 나(85), 마(85), 다(80) ← 점수 내림차순
2반: 라(95), 가(90)        ← 점수 내림차순
'''

# 문제 4: 열(컬럼) 이름 정렬

'''
sort_index(axis=1): 열 이름을 알파벳순으로 정렬
axis=0: 행 인덱스 정렬, axis=1: 열 이름 정렬
'''

print("4. 열 이름 알파벳순 정렬:")
print(df.sort_index(axis=1))
# 결과: '이름', '점수', '반' → '반', '이름', '점수'
print()

# 문제 5: 인덱스 기준 정렬

df = pd.DataFrame({
    'value': [10, 20, 30, 40]
}, index=[3, 1, 4, 2])  # 불규칙한 인덱스

# sort_index(): 행 인덱스를 기준으로 정렬
print("5-1. 원본 (인덱스 불규칙):")
print(df)
print()

print("5-2. 인덱스 오름차순 정렬:")
print(df.sort_index())
# 결과: 인덱스 1, 2, 3, 4 순서로 정렬
print()

# 문제 6: 다양한 정렬 방법

print("6-1. 인덱스 내림차순 정렬:")
print(df.sort_index(ascending=False))
# 결과: 인덱스 4, 3, 2, 1 순서
print()

print("6-2. value 열 기준 오름차순 정렬:")
print(df.sort_values(by='value'))
# 결과: 10, 20, 30, 40 순서 (인덱스는 원래대로)
print()

'''
정렬 메소드 정리:
┌──────────────────┬─────────────────────────────┐
│ 메소드             │ 용도                         │
├──────────────────┼─────────────────────────────┤
│ sort_values()    │ 열(컬럼) 값 기준 정렬            │
│ sort_index()     │ 행 인덱스 또는 열 이름 정렬        │
│ ascending        │ True=오름차순, False=내림차순    │
│ by               │ 정렬 기준 열 지정               │
│ axis             │ 0=행, 1=열                   │
│ inplace          │ True=원본 변경                │
│ reset_index()    │ 인덱스 재정렬                  │
└──────────────────┴─────────────────────────────┘

정렬 후 인덱스 처리:
- 정렬 후 인덱스가 불규칙해짐
- reset_index(drop=True)로 0부터 재정렬 권장
'''