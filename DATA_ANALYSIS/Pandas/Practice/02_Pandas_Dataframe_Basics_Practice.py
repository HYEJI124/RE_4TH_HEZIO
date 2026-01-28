import pandas as pd

# 실무 예제 - 직원 데이터 분석
print("실무 예제 - 직원 데이터 분석")

# 현실적인 직원 데이터
employee_data = pd.DataFrame({
    'employee_id': ['E001', 'E002', 'E003', 'E004', 'E005'],
    'name': ['김철수', '이영희', '박민수', '정수진', '최지훈'],
    'age': [27, 23, 35, 29, 31],
    'department': ['Dev', 'HR', 'Sales', 'Dev', 'Sales'],
    'position': ['Junior', 'Senior', 'Manager', 'Senior', 'Junior'],
    'salary': [4500, 4800, 5200, 4700, 4600],
    'join_year': [2020, 2021, 2018, 2019, 2020]
})

print("직원 데이터:")
print(employee_data)
print()

print("데이터 요약:")
print(f"• 총 직원 수: {len(employee_data)}명")
print(f"• 데이터 항목: {employee_data.shape[1]}개")
print(f"• 평균 연봉: {employee_data['salary'].mean():.0f}만원")
print(f"• 평균 나이: {employee_data['age'].mean():.1f}세")
print(f"• 최고 연봉: {employee_data['salary'].max()}만원")
print(f"• 최저 연봉: {employee_data['salary'].min()}만원")