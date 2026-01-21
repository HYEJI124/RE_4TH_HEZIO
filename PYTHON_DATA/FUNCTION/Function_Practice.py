# 모든 내장함수를 활용한 종합 예제

def student_grade_system():
    # 샘플 데이터 생성
    students = [
        {'name': '김철수', 'scores': [85, 90, 78, 92, 88]},
        {'name': '이영희', 'scores': [92, 94, 89, 96, 91]},
        {'name': '박민수', 'scores': [78, 82, 75, 80, 79]},
        {'name': '최지연', 'scores': [88, 85, 91, 87, 89]},
        {'name': '정다영', 'scores': [95, 97, 93, 98, 96]}
    ]

    print('학생 성적 분석 시스템')

    # 1. 각 학생의 통계 계산
    for student in students:
        name = student['name']
        scores = student['scores']

        # 다양한 내장함수 활용
        avg_score = sum(scores) / len(scores)
        min_score = min(scores)
        max_score = max(scores)

        # 학점 계산
        if avg_score >= 95:
            grade = 'A+'
        elif avg_score >= 90:
            grade = 'A'
        elif avg_score >= 85:
            grade = 'B+'
        elif avg_score >= 80:
            grade = 'B'
        else:
            grade = 'C'

        student['average'] = round(avg_score, 1)
        student['min'] = min_score
        student['max'] = max_score
        student['grade'] = grade

        print(f'{name}')
        print(f'점수: {scores}')
        print(f'평균: {avg_score:.1f}점 (학점: {grade})')
        print(f'최고점: {max_score}점, 최저점: {min_score}점')
        print(f'점수차: {max_score - min_score}점')

    # 2. 전체 통계
    all_averages = [s['average'] for s in students]
    class_average = sum(all_averages) / len(all_averages)

    print('전체 통계')
    print(f'학급 평균: {class_average:.1f}점')
    print(f'최고 평균: {max(all_averages)}점')
    print(f'최저 평균: {min(all_averages)}점')

    # 3. 평균 점수순 정렬
    sorted_students = sorted(students, key=lambda x: x['average'], reverse=True)
    print('평균 점수 순위')
    for rank, student in enumerate(sorted_students, 1):
        print(f'{rank}위: {student['name']} ({student['average']}점, {student['grade']})')

    # 4. 학점별 분류
    grade_groups = {}
    for student in students:
        grade = student['grade']
        if grade not in grade_groups:
            grade_groups[grade] = []
        grade_groups[grade].append(student['name'])

    print(f'학점별 분류')
    for grade in sorted(grade_groups.keys(), reverse=True):
        students_in_grade = grade_groups[grade]
        print(f'{grade}학점: {','.join(students_in_grade)} ({len(students_in_grade)}명)')

    # 5. 우수학생 선정 (평균 90점 이상)
    excellent_students = list(filter(lambda s: s['average'] >= 90, students))
    print('우수학생 (평균 90점 이상)')
    for student in excellent_students:
        print(f'{student['name']}: {student['average']}점')

    # 6. 모든 학생이 80점 이상인지 확인
    all_above_80 = all(s['average'] >= 80 for s in students)
    any_above_95 = any(s['average'] >= 95 for s in students)

    print('성취도 확인')
    print(f'모든 학생이 평균 80점 이상: {'예' if all_above_80 else '아니오'}')
    print(f'평균 95점 이상인 학생 존재: {'예' if any_above_95 else '아니오'}')

    return students

# 시스템 실행
final_results = student_grade_system()