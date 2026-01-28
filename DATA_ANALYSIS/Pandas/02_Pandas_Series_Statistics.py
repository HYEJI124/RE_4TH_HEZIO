import pandas as pd

# 통계 함수란?
"""
통계 함수 (Statistical Functions):
    - 데이터의 특징을 숫자로 요약하는 것
    - 대량의 데이터를 몇 개의 숫자로 표현
    - 데이터의 경향성과 분포를 파악
    
왜 필요한가?
    - 데이터를 한눈에 이해하기 위해
    - 데이터 간 비교를 쉽게 하기 위해
    - 이상치(Outlier)를 발견하기 위해
    - 의사결정의 근거를 마련하기 위해

크게 두 가지 범주:
    1. 중심 경향성 측정 (Central Tendency)
       - 평균, 중앙값, 최빈값
       - "데이터의 중심이 어디인가?"
    
    2. 산포도 측정 (Dispersion)
       - 범위, 분산, 표준편차
       - "데이터가 얼마나 흩어져 있는가?"
"""

# 샘플 데이터 준비
"""
실무 시나리오:
    - 한 달간의 일일 매출 데이터
    - 총 30일 (9월 1일 ~ 9월 30일)
    - 단위: 만원
"""

daily_sales = pd.Series([
    302, 423, 123, 437, 890,  # 1주차 (9/1 ~ 9/5)
    124, 781, 920, 478, 901,  # 2주차 (9/6 ~ 9/10)
    241, 891, 123, 678, 912,  # 3주차 (9/11 ~ 9/15)
    367, 894, 355, 123, 674,  # 4주차 (9/16 ~ 9/20)
    891, 234, 678, 943, 524,  # 5주차 (9/21 ~ 9/25)
    782, 394, 327, 891, 237   # 6주차 (9/26 ~ 9/30)
],
    index=pd.date_range('2025-09-01', periods=30),
    name='Sales'
)

print("[원본 데이터]")
print(daily_sales)
print()

# 1. 중심 경향성 측정 (Central Tendency)
"""
중심 경향성이란?
    - 데이터의 '중심'이 어디에 있는지 나타내는 지표
    - 데이터를 대표하는 값
"""

print("1. 중심 경향성 측정 (Central Tendency)")

# 1-1. 평균 (Mean)
"""
평균 (Mean, Average):
    - 모든 값의 합을 개수로 나눈 값
    - 공식: (x₁ + x₂ + ... + xₙ) / n
    
장점:
    - 모든 데이터를 고려
    - 계산이 간단
    - 가장 널리 사용되는 통계량
    
단점:
    - 이상치(극단값)에 민감
    - 예: [10, 20, 30, 1000] → 평균 = 265 (왜곡됨)
    
사용 시기:
    - 데이터가 정규분포를 따를 때
    - 이상치가 없을 때
"""

mean_value = daily_sales.mean()
print(f'[1-1] 평균 (Mean): {mean_value:.2f}만원')
print(f"해석: 한 달간 평균 매출은 약 {mean_value:.0f}만원입니다.")
print()

# 1-2. 중앙값 (Median)
"""
중앙값 (Median):
    - 데이터를 크기 순으로 정렬했을 때 가운데 위치한 값
    - 데이터 개수가 홀수: 가운데 값
    - 데이터 개수가 짝수: 가운데 두 값의 평균
    
예시:
    [1, 2, 3, 4, 5] → 중앙값 = 3
    [1, 2, 3, 4, 5, 6] → 중앙값 = (3+4)/2 = 3.5
    
장점:
    - 이상치에 강함 (Robust)
    - [10, 20, 30, 1000] → 중앙값 = 25
    
단점:
    - 모든 데이터를 고려하지 않음
    - 계산이 평균보다 복잡
    
사용 시기:
    - 이상치가 있을 때
    - 소득, 부동산 가격 등 왜곡된 분포
"""

median_value = daily_sales.median()
print(f'[1-2] 중앙값 (Median): {median_value:.0f}만원')
print(f"해석: 매출을 크기순으로 정렬하면 가운데 값은 {median_value:.0f}만원입니다.")

# 평균 vs 중앙값 비교
if mean_value > median_value:
    print(f"비교: 평균({mean_value:.0f}) > 중앙값({median_value:.0f})")
    print(f"→ 고액 매출이 있어 평균이 높아진 것으로 보입니다.")
elif mean_value < median_value:
    print(f"비교: 평균({mean_value:.0f}) < 중앙값({median_value:.0f})")
    print(f"→ 저액 매출이 있어 평균이 낮아진 것으로 보입니다.")
else:
    print(f"비교: 평균과 중앙값이 같습니다 (대칭 분포)")
print()

# 1-3. 최빈값 (Mode)
"""
최빈값 (Mode):
    - 데이터에서 가장 자주 나타나는 값
    - 빈도가 가장 높은 값
    
특징:
    - 여러 개의 최빈값이 존재할 수 있음
    - 최빈값이 없을 수도 있음 (모든 값이 한 번씩만 나타나는 경우)
    
장점:
    - 범주형 데이터에도 사용 가능
    - 예: 가장 많이 팔린 제품
    
사용 시기:
    - 범주형 데이터 분석
    - "가장 흔한" 값을 알고 싶을 때
"""

mode_value = daily_sales.mode()
print(f'[1-3] 최빈값 (Mode):')
if len(mode_value) > 0:
    print(f'{mode_value.values}만원')
    print(f"해석: {mode_value.values[0]:.0f}만원 매출이 가장 자주 발생했습니다.")
    if len(mode_value) > 1:
        print(f"(여러 개의 최빈값이 있습니다)")
else:
    print("최빈값이 없습니다 (모든 값이 1회씩만 등장)")
print()


# 2. 산포도 측정 (Dispersion / Variability)
"""
산포도란?
    - 데이터가 얼마나 퍼져있는지를 나타내는 지표
    - 데이터의 변동성(Variability)
    
왜 중요한가?
    - 평균만으로는 데이터의 전체 모습을 알 수 없음
    - 예: A반 평균 80점, B반 평균 80점
         하지만 A반은 70~90점, B반은 50~100점으로 분포
         → 평균은 같지만 산포도가 다름
"""

print("2. 산포도 측정 (Dispersion)")

# ----------------------------------------------------------------------------
# 2-1. 최댓값과 최솟값
# ----------------------------------------------------------------------------
"""
최댓값 (Maximum), 최솟값 (Minimum):
    - 데이터의 범위를 알려주는 가장 기본적인 통계량
    - 이상치를 발견하는 데 유용
"""

max_value = daily_sales.max()
min_value = daily_sales.min()

print(f'[2-1] 최댓값 (Max): {max_value}만원')
print(f"→ 가장 매출이 좋았던 날의 매출")
print(f'[2-2] 최솟값 (Min): {min_value}만원')
print(f"→ 가장 매출이 안 좋았던 날의 매출")
print()

# 2-3. 범위 (Range)
"""
범위 (Range):
    - 최댓값 - 최솟값
    - 데이터의 전체 폭을 나타냄
    
장점:
    - 직관적이고 계산이 간단
    
단점:
    - 극단값 2개만 사용 (나머지 데이터 무시)
    - 이상치에 매우 민감
"""

range_value = max_value - min_value
print(f'[2-3] 범위 (Range): {range_value}만원')
print(f"해석: 최고 매출과 최저 매출의 차이는 {range_value}만원입니다.")
print()

# 2-4. 분산 (Variance)
"""
분산 (Variance):
    - 각 데이터가 평균으로부터 떨어진 거리의 제곱의 평균
    - 공식: Σ(xᵢ - μ)² / n
    
계산 과정:
    1. 각 값에서 평균을 뺌 (편차)
    2. 편차를 제곱 (음수 제거, 큰 편차에 가중치)
    3. 모든 제곱의 평균
    
특징:
    - 단위가 원래 데이터의 제곱
    - 예: 매출이 만원 단위면 분산은 (만원)²
    - 해석이 어려움 → 표준편차 사용
    
장점:
    - 모든 데이터를 고려
    - 수학적으로 다루기 좋음
    
단점:
    - 해석이 직관적이지 않음
    - 이상치에 민감
"""

variance = daily_sales.var()
print(f'[2-4] 분산 (Variance): {variance:.2f} (만원)²')
print(f"해석: 매출의 변동성을 제곱 단위로 표현한 값입니다.")
print(f"(단위 때문에 해석이 어려움 → 표준편차 사용)")
print()

# 2-5. 표준편차 (Standard Deviation)
"""
표준편차 (Standard Deviation, SD):
    - 분산의 제곱근 (√분산)
    - 공식: σ = √(Σ(xᵢ - μ)² / n)
    
특징:
    - 원래 데이터와 같은 단위
    - 예: 매출이 만원 단위면 표준편차도 만원 단위
    - 가장 널리 사용되는 산포도 측정치
    
해석:
    - 표준편차가 작을수록: 데이터가 평균 근처에 모여있음 (안정적)
    - 표준편차가 클수록: 데이터가 넓게 퍼져있음 (변동성 큼)
    
경험 법칙 (정규분포를 따를 때):
    - 평균 ± 1σ: 약 68%의 데이터
    - 평균 ± 2σ: 약 95%의 데이터
    - 평균 ± 3σ: 약 99.7%의 데이터
"""

std_dev = daily_sales.std()
print(f'[2-5] 표준편차 (Standard Deviation): {std_dev:.2f}만원')
print(f"해석: 평균적으로 매출은 평균에서 ±{std_dev:.0f}만원 정도 떨어져 있습니다.")
print()

# 표준편차를 이용한 데이터 범위 추정
print("표준편차를 이용한 범위 추정:")
lower_bound = mean_value - std_dev
upper_bound = mean_value + std_dev
print(f"평균 ± 1 표준편차: {lower_bound:.0f}만원 ~ {upper_bound:.0f}만원")
print(f"→ 대부분의 매출이 이 범위 안에 있을 것으로 예상됩니다.")
print()

# 실제로 범위 안에 있는 데이터 비율 계산
within_range = daily_sales[(daily_sales >= lower_bound)
                           & (daily_sales <= upper_bound)]
percentage = (len(within_range) / len(daily_sales)) * 100
print(f"실제 데이터: {len(within_range)}/{len(daily_sales)}일 ({percentage:.1f}%)이 이 범위 안에 있습니다.")
print()

# 3. describe() - 모든 통계량 한 번에 보기
"""
describe() 메서드:
    - 주요 통계량을 한 번에 출력
    - 데이터 탐색(EDA)의 첫 단계로 자주 사용
    
출력 내용:
    - count: 데이터 개수
    - mean: 평균
    - std: 표준편차
    - min: 최솟값
    - 25%: 1사분위수 (하위 25% 지점)
    - 50%: 2사분위수 (중앙값)
    - 75%: 3사분위수 (하위 75% 지점)
    - max: 최댓값
"""

print("3. describe() - 통계 요약")

print(daily_sales.describe())
print()

print("통계량 해석 가이드")
print(f"""
중심 경향성:
   • 평균: {mean_value:.2f}만원 → 전체적인 매출 수준
   • 중앙값: {median_value:.0f}만원 → 이상치의 영향을 받지 않는 중심값
   • 차이: {abs(mean_value - median_value):.2f}만원 → 분포의 비대칭성

산포도:
   • 표준편차: {std_dev:.2f}만원 → 매출의 변동성
   • 범위: {range_value}만원 → 최고-최저 매출 차이
   • 변동계수: {(std_dev/mean_value)*100:.1f}% → 상대적 변동성

실무 인사이트:
   • 대부분의 매출은 {lower_bound:.0f}~{upper_bound:.0f}만원 사이
   • 이 범위를 벗어나면 '비정상적인 날'로 볼 수 있음
   • 재고 관리, 인력 배치 등에 활용 가능
""")

# 4. 추가 유용한 통계 함수들

print("4. 추가 통계 함수")

# 4-1. 합계
print(f"[4-1] 합계 (Sum): {daily_sales.sum():,}만원")
print(f"→ 한 달 총 매출")

# 4-2. 사분위수 (Quantile)
print(f"[4-2] 사분위수 (Quantile):")
print(f"25% (Q1): {daily_sales.quantile(0.25):.0f}만원 (하위 25%)")
print(f"50% (Q2): {daily_sales.quantile(0.50):.0f}만원 (중앙값)")
print(f"75% (Q3): {daily_sales.quantile(0.75):.0f}만원 (하위 75%)")
print(f"IQR: {daily_sales.quantile(0.75) - daily_sales.quantile(0.25):.0f}만원 (사분위수 범위)")

# 4-3. 개수
print(f"[4-3] 개수 (Count): {daily_sales.count()}일")
print(f"→ 결측치가 없는 유효한 데이터 개수")

# 4-4. 누적 합계
print(f"[4-4] 누적 합계 (Cumulative Sum) - 처음 5일:")
print(daily_sales.cumsum().head())
print(f"→ 매일매일 누적되는 총 매출")