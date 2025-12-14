# ========================================
# 자료형 변환 (Type Conversion)
# ========================================

"""
때로는 한 자료형을 다른 자료형으로 변환해야 할 때가 있음
int(), float(), str() 함수를 사용하여 변환 가능
"""

# 문자열을 숫자로 변환
string_number = "123"           # 문자열 "123"
converted_int = int(string_number)     # 정수 123으로 변환
converted_float = float(string_number)  # 실수 123.0으로 변환

print(f"원본: {string_number} (타입: {type(string_number)})")
print(f"정수 변환: {converted_int} (타입: {type(converted_int)})")
print(f"실수 변환: {converted_float} (타입: {type(converted_float)})")

# 숫자를 문자열로 변환
number = 456
converted_string = str(number)   # "456"으로 변환
print(f"원본: {number} (타입: {type(number)})")
print(f"문자열 변환: {converted_string} (타입: {type(converted_string)})")

# 주의: 변환할 수 없는 경우 에러 발생
# a = "1a"  # 문자가 섞여 있어서 숫자로 변환 불가능
# a1 = int(a)  # ValueError 발생!

