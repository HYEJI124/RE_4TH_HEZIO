import pandas as pd
import numpy as np

# 환경 데이터 정제

data = {
    "도시": ["서울", "부산", "광주", "대구", np.nan, "춘천"],
    "미세먼지": [45, 51, np.nan, 38, 49, np.nan],         # PM10
    "초미세먼지": [20, np.nan, 17, 18, 22, 19],           # PM2.5
    "강수량": [0.0, 2.5, 1.0, np.nan, 3.1, 0.0]          # mm
}

df = pd.DataFrame(data)

print('=== 환경 데이터 원본 ===')
print(df)
print()

# 결측값 현황 파악
print('=== 결측값 개수 ===')
print(df.isna().sum())
print()

'''
처리 전략 수립:
1. 도시명 결측 → 삭제 (도시를 모르면 데이터 무의미)
2. 미세먼지 결측 → 평균값 대체 (대기질은 인근 지역과 유사)
3. 초미세먼지 결측 → 중앙값 대체 (극단값 영향 최소화)
4. 강수량 결측 → 0으로 대체 (기록 없음 = 비 안 옴)
'''

# 1. 도시명 결측 행 제거
df_clean = df.dropna(subset=['도시'])
print('=== 도시명 결측 제거 후 ===')
print(df_clean)
print()

# 2. 미세먼지 평균값으로 대체
pm10_mean = df_clean['미세먼지'].mean()  # (45+51+38+49)/4 = 45.75
df_clean['미세먼지'] = df_clean['미세먼지'].fillna(pm10_mean)
print('=== 미세먼지 평균 대체 후 ===')
print(df_clean)
print()

# 3. 초미세먼지 중앙값으로 대체
pm25_median = df_clean['초미세먼지'].median()  # [17, 18, 20, 22] → 19
df_clean['초미세먼지'] = df_clean['초미세먼지'].fillna(pm25_median)
print('=== 초미세먼지 중앙값 대체 후 ===')
print(df_clean)
print()

# 4. 강수량 0으로 대체
df_clean['강수량'] = df_clean['강수량'].fillna(0)
print('=== 최종 정제 데이터 ===')
print(df_clean)
print()

# 최종 결측값 확인
print('=== 최종 결측값 확인 ===')
print(df_clean.isna().sum())
# 모든 결측값이 처리되어야 함!