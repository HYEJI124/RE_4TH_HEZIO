import pandas as pd
import numpy as np

# 월별 매장 성과 분석

monthly_sales = pd.DataFrame({
    'month': [1, 1, 2, 2, 3, 3, 1, 2, 3],
    'store': ['A', 'B', 'A', 'B', 'A', 'B', 'C', 'C', 'C'],
    'sales': [100, 80, 120, 90, 150, 100, 110, 95, 130],  # 매출
    'customers': [50, 40, 60, 45, 75, 50, 55, 48, 65]     # 고객수
})

# 월별, 매장별 통합 분석
comprehensive = monthly_sales.groupby(['month', 'store']).agg({
    'sales': ['sum', 'mean'],
    'customers': ['sum', 'mean']
})

print('월별/매장별 종합 분석:')
print(comprehensive)
print()

# 매장별 총합 (월 구분 없이)
store_total = monthly_sales.groupby('store', as_index=False).agg({
    'sales': ['sum', 'mean'],
    'customers': 'sum'
})
print('매장별 총합:')
print(store_total)
print()

# 그룹화와 집계 (GroupBy And Aggregation)

df = pd.DataFrame({
    'grade': [1, 2, 1, 2, 1, 3],
    'name': ['Kim', 'Lee', 'Park', 'Choi', 'Jung', 'Han'],
    'kor': [85, 78, 90, 92, 80, 75]
})

# 문제 1: 단일 그룹, 단일 집계

# 학년별 평균 국어 점수
print("1. 학년별 평균 국어 점수:")
result = df.groupby('grade')['kor'].mean()
print(result)
print()

'''
결과

grade
1    85.0  (85+90+80)/3
2    85.0  (78+92)/2
3    75.0
'''

# 문제 2: 다중 그룹, 다중 집계 + 열 이름 변경

df = pd.DataFrame({
    'class': [1, 1, 1, 2, 2, 2],
    'subject': ['Math', 'Math', 'Eng', 'Math', 'Eng', 'Eng'],
    'score': [80, 90, 85, 70, 95, 90]
})

# 반별, 과목별 응시자 수와 평균 점수
print("2. 반별/과목별 응시자 수와 평균:")

'''
agg(['count', 'mean']): 두 집계 함수를 동시에 적용
결과 컬럼명: 'count', 'mean'
'''
result = df.groupby(['class', 'subject'])['score'].agg(['count', 'mean'])
'''
rename(): 컬럼명 변경
columns={'기존이름': '새이름'}
inplace=True: 원본 변경
'''
result.rename(columns={'mean': 'avg'}, inplace=True)
print(result)
print()

'''
결과

               count  avg
class subject
1     Eng          1   85.0
      Math         2   85.0  (80+90)/2
2     Eng          2   92.5  (95+90)/2
      Math         1   70.0
'''

# 문제 3: 다중 그룹, 다중 집계

df = pd.DataFrame({
    'region': ['Seoul', 'Seoul', 'Busan', 'Busan', 'Daegu', 'Daegu'],
    'seller': ['A', 'B', 'A', 'B', 'A', 'A'],
    'sales': [100, 200, 150, 120, 130, 200]
})

# 지역별, 판매자별 판매액 합계와 최댓값
print("3. 지역별/판매자별 판매액 합계와 최댓값:")
result = df.groupby(['region', 'seller'])['sales'].agg(['sum', 'max'])
print(result)
print()

'''
결과

               sum  max
region seller
Busan  A       150  150
       B       120  120
Daegu  A       330  200  (130+200, max=200)
Seoul  A       100  100
       B       200  200
'''

# 문제 4: 결측값 포함 그룹화

df = pd.DataFrame({
    'team': ['A', 'A', 'B', 'B', 'A', 'B'],
    'position': ['FW', 'DF', 'FW', 'DF', 'DF', 'FW'],
    'score': [3, 2, None, 1, 4, 2]  # None = 결측값
})

'''
dropna=False: 결측값도 그룹화에 포함
기본값(dropna=True)은 결측값이 있는 행을 제외함
'''

print("4. 팀별/포지션별 점수 평균 (결측값 포함):")
result = df.groupby(['team', 'position'], dropna=False)['score'].mean()
print(result)
print()

'''
결과

team  position
A     DF          3.0  (2+4)/2
      FW          3.0
B     DF          1.0
      FW          2.0  (None+2)/1 = 2.0 (None은 평균 계산 시 제외)
'''

# 문제 5: agg() 딕셔너리 방식 + 이름 지정

df = pd.DataFrame({
    'dept': ['HR', 'HR', 'IT', 'IT', 'Sales', 'Sales'],
    'gender': ['M', 'F', 'F', 'M', 'F', 'F'],
    'salary': [3500, 3200, 4000, 4200, 3000, 3100]
})

# 부서별, 성별 인원 수와 총 연봉 합계

# 방법 1: 기본 agg() (컬럼명 자동)
print("5-1. 기본 agg():")
result1 = df.groupby(['dept', 'gender'])['salary'].agg(['count', 'sum'])
print(result1)
print()

# 방법 2: 명명된 집계 (권장)
# 새컬럼명=('집계대상컬럼', '집계함수')
print("5-2. 명명된 집계:")
result2 = df.groupby(['dept', 'gender']).agg(
    count=('salary', 'count'),       # 새 컬럼: count
    total_salary=('salary', 'sum')   # 새 컬럼: total_salary
)
print(result2)
print()
'''
결과

              count  total_salary
dept  gender
HR    F           1          3200
      M           1          3500
IT    F           1          4000
      M           1          4200
Sales F           2          6100  (3000+3100)
'''

'''
GroupBy 정리

1. 기본 패턴:
   df.groupby('기준열')['집계열'].집계함수()

2. 다중 그룹:
   df.groupby(['열1', '열2'])['집계열'].집계함수()

3. 다중 집계:
   df.groupby('기준열')['집계열'].agg(['함수1', '함수2'])

4. 컬럼별 다른 집계:
   df.groupby('기준열').agg({
       '열1': '함수1',
       '열2': ['함수2', '함수3']
   })

5. 명명된 집계(가독성 최고):
   df.groupby('기준열').agg(
       새이름1=('열1', '함수1'),
       새이름2=('열2', '함수2')
   )

6. 결측값 처리:
   - dropna = True (기본): 결측값 제외
   - dropna = False: 결측값 포함

7. 인덱스 제어:
   - as_index = True (기본): 그룹 키가 인덱스
   - as_index = False: 그룹 키가 일반 컬럼
'''
