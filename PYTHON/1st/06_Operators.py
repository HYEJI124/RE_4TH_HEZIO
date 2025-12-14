# ===========================
# 1. 비교 연산자 (x, y 값 비교)
# ===========================

x = 10
y = 20

# == : 두 값이 같으면 True, 다르면 False
print(f'x == y: {x == y}')  # 10과 20은 같지 않으므로 False

# != : 두 값이 다르면 True
print(f'x != y: {x != y}')  # 10과 20은 다르므로 True

# > : 왼쪽 값이 크면 True
print(f'x > y : {x > y}')   # 10은 20보다 작으므로 False

# >= : 왼쪽 값이 크거나 같으면 True
print(f'x >= y: {x >= y}')  # 10은 20보다 작으므로 False

# < : 왼쪽 값이 작으면 True
print(f'x < y : {x < y}')   # 10은 20보다 작으므로 True

# <= : 왼쪽 값이 작거나 같으면 True
print(f'x <= y: {x <= y}')  # 10은 20보다 작으므로 True

# x, y 값을 15로 다시 설정
x = 15
y = 15

print(f'x <= y: {x <= y}')  # 15는 15와 같으므로 True
print(f'x >= y: {x >= y}')  # 15는 15와 같으므로 True


# ===========================
# 2. 논리 연산자 (and, or, not)
# ===========================

# and : 양쪽 조건이 모두 True여야 True
print(True and True)    # 둘 다 True → True
print(True and False)   # 한쪽이 False → False
print(False and True)   # 한쪽이 False → False
print(False and False)  # 둘 다 False → False

# or : 둘 중 하나라도 True면 True
print(True or True)     # 둘 다 True → True
print(True or False)    # 하나가 True → True
print(False or True)    # 하나가 True → True
print(False or False)   # 둘 다 False → False

# not : True ↔ False 반전
print(f'not True : {not True}')     # True → False
print(f'not False : {not False}')   # False → True

# and, or 혼합
# (True and False) → False, False or True → True
print(True and False or True)
# (False or True) → True, (True and True) → True, True and False → False
print(True and (False or True) and False)


