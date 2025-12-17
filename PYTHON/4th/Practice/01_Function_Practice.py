# 문제 1. 계산기 만들기
# 함수를 이용하지 않은 계산기
a = int(input('숫자를 입력해주세요:'))
b = int(input('숫자를 입력해주세요:'))
op = input('연산자를 입력해주세요:')

# 결과값
result = 0

if op == "+":
    result = a + b
elif op == '-':
    result = a - b
elif op == '*':
    result = a * b
elif op == '/':
    result = a / b
else:
    result = '지원하지 않는 연산입니다.'

print(result)

# 함수 이용한 계산기
def calculate(a, b, op):

    # 결과값
    result = 0

    if op == "+":
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    elif op == '/':
        result = a / b
    else:
        result = '지원하지 않는 연산입니다.'

    return result

print(calculate(2, 3, '+'))
print(calculate(2, 3, '-'))
print(calculate(2, 3, '*'))
print(calculate(2, 3, '/'))
print(calculate(2, 3, '//'))


# 가변인자 연습하기

# 1. args 사용 연습

# 문제 1. 숫자 여러 개의 평균 구하기
# 숫자를 몇 개든 받을 수 있는 average() 함수를 만들어보세요.

def average(*args):
    total = sum(args)
    size = len(args)
    return total / size

print(average(1, 2, 3, 4, 5,))
print(average(31, 22, 37, 24, 25, 32,))

# 문제 2. 가장 긴 문자열 찾기(max 함수에 대해 찾아보고 풀기)
# 여러 개의 문자열을 받아, 가장 긴 문자열을 반환하는 함수를 만들어보세요
# print(max(["hello", "banana", 'car', 'apple'], key=len))  # banana

def max_len_word(*args):
    return max(args, key=len)

print(max_len_word("hello", "banana", 'car', 'apple'))

# 2. kwargs 사용 연습

# 문제 3. 사용자 정보 출력 함수
# 사용자의 이름, 나이, 이메일 등의 정보를 받아 출력하는 함수를 **kwargs로 구현하세요.

def user_info_print(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} {value}')

user_info_print(name='김철수', age=25, email='hyeji@gmail.com')

# 문제 4. 할인 계산기
# 상품 가격 목록을 **kwargs로 받아, 각각 10 % 씩 할인된 가격을 출력하는 함수를 작성하세요.

def product_info_print(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} {value * 0.9}')

product_info_print(product1=1000, product2=2500,
                   product3=3200, product4=1600,)


# 전역변수, 지역변수 사용하기

# 문제 1. 로그인 정보
current_user = None  # 로그아웃 상태

def login(name):
    global current_user
    if current_user != None:
        print('이미 로그인 되어 있습니다.')
    else:
        current_user = name
        print(f'{name}님 로그인 성공!')

def logout():
    global current_user
    if current_user == None:
        print('로그인 되어 있지 않습니다.')
    else:
        print(f'{current_user}님 로그아웃 성공!')
        current_user = None

login('Hyeji')
login('CodingOwl')
logout()
logout()
login('CodingOwl')
print(current_user)

# 재귀함수 사용하기

# 문제 1. a를 b번 곱한 값

def power(a, b):
    if b == 0:
        return 1
    
    return a * power(a, b-1)

power(2, 3)
# 2 x power(2,2)
# 2 x 2 x power(2,1)
# 2 x 2 x 2 x 1


# 문제 2. 1부터 n까지의 합
# 문제: 1 + 2 + 3 + ... + n을 구하세요.

# 1)
def sum_to_n(n):
    """
    예: sum_to_n(5) = 1 + 2 + 3 + 4 + 5 = 15
    """
    if n == 1:
        return 1

    return n + sum_to_n(n-1)

# 2)
def sum_to_n(n):
    return sum(range(1, n+1))

# 문제 3: 문자열 뒤집기
# 문제: 문자열을 재귀로 뒤집으세요.

# 1)
def reverse_string(s):
    """
    예: reverse_string("hello") = "olleh"
    """
    if len(s) == 0:
        return ''

    return s[-1] + reverse_string(s[:-1])

# 2)
def reverse_string(s):
    return s[::-1]
