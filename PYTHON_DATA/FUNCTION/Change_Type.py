# ================================
# 4. 타입 변환 함수
# ================================

'''
[1. int(), float(), str() - 기본 타입 변환]
'''

# 다양한 변환 예제
conversion_examples = [
    ("문자열 → 정수", "123", int),
    ("실수 → 정수", 3.14, int),
    ("정수 → 실수", 42, float),
    ("문자열 → 실수", "3.14", float),
    ("정수 → 문자열", 123, str),
    ("실수 → 문자열", 3.14, str)
]

for description, value, func in conversion_examples:
    try:
        result = func(value)
        print(f'{description}: {value} -> {result} (타입: {type(result.__name__)})')
    except ValueError as e:
        print(f'{description}: {value} -> 변환 실패 ({e})')

# 진법 변환
number = 42
print(f'10진수 {number}')
print(f'2진수: {bin(number)}')
print(f'8진수: {oct(number)}')
print(f'16진수: {hex(number)}')

# 역변환
binary_str = "101010"
print(f'2진수 "{binary_str}" -> 10진수: {int(binary_str, 2)}')

'''
[2. list(), tuple(), set(), dict() - 컬렉션 변환]
'''

# 원본 데이터
original_string = "python"
original_list = [1, 2, 3, 2, 1]
original_tuple = (10, 20, 30)

print('컬렉션 간 변환')
print(f'문자열 -> 리스트: {original_string} -> {list(original_string)}')
print(f'리스트 -> 튜플: {original_list} -> {tuple(original_list)}')
print(f'리스트 -> 집합: {original_list} -> {set(original_list)}') # 중복 제거됨
print(f'튜플 -> 리스트: {original_tuple} -> {list(original_tuple)}')

# 딕셔너리 생성
key_value_pairs = [('이름', '김철수'), ('나이', 25), ('직업', '개발자')]
person_dict = dict(key_value_pairs)
print(f'리스트 -> 딕셔너리: {key_value_pairs} -> {person_dict}')

# 중복 제거
duplicated_list = [1, 2, 2, 3, 3, 3, 4, 4, 5]
unique_list = list(set(duplicated_list)) # 집합으로 변환 후 다시 리스트로

print(f'원본: {duplicated_list}')
print(f'중복제거: {unique_list}')
print(f'순서유지 중복제거: {list(dict.fromkeys(duplicated_list))}')