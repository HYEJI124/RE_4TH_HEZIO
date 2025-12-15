# 1. 두 수의 나눗셈

'''
정수 num1과 num2가 매개변수로 주어질 때, num1을 num2로 나눈 값에 1,000을 곱한 후 정수 부분을 return 하도록 solution 함수를 완성해주세요.
'''

def solution(num1, num2):
    answer = (num1 / num2) * 1000
    return int(answer)

print(solution(3, 2))
print(solution(7, 3))
print(solution(1, 16))

# 2. 숫자 비교하기

'''
정수 num1과 num2가 매개변수로 주어집니다. 두 수가 같으면 1 다르면 -1을 retrun하도록 solution 함수를 완성해주세요.
'''

def solution(num1, num2):
    if num1 == num2:
        return 1
    else:
        return -1
    
print(solution(2, 3))
print(solution(11, 11))
print(solution(7, 99))

# 3. 분수의 덧셈

'''
첫 번째 분수의 분자와 분모를 뜻하는 numer1, denom1, 두 번째 분수의 분자와 분모를 뜻하는 numer2, denom2가 매개변수로 주어집니다.
두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.
'''

import math

def solution(numer1, denom1, numer2, denom2):
    denom = denom1 * denom2 # 분모
    numer = numer1 * denom2 + numer2 * denom1 # 분자
    GCD = math.gcd(denom, numer) # 최대공약수
    answer = [numer//GCD, denom//GCD]
    return answer

print(solution(1, 2, 3, 4))
print(solution(9, 2, 1, 3))

# 4. 배열 두 배 만들기

'''
정수 배열 numbers가 매개변수로 주어집니다. 
numbers의 각 원소에 두배한 원소를 가진 배열을 return하도록 solution 함수를 완성해주세요.
'''

def solution(numbers):
    answer = []
    for num in numbers:
        answer.append(num * 2)
    return answer

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 2, 100, -99, 1, 2, 3]))

