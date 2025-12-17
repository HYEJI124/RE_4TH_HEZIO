# 피자 나눠 먹기(1)

'''
머쓱이네 피자가게는 피자를 일곱 조각으로 잘라 줍니다. 
피자를 나눠먹을 사람의 수 n이 주어질 때, 모든 사람이 피자를 한 조각 이상 먹기 위해 필요한 피자의 수를 return 하는 solution 함수를 완성해보세요.
'''

def solution(n):
    if n % 7 == 0: # 사람의 수가 7의 배수일 때
        answer = n // 7
    else: # 사람의 수가 7의 배수가 아닐 때는 1판 더 필요
        answer = n // 7 + 1

    return answer

print(solution(7)) # 1
print(solution(1)) # 1
print(solution(15)) # 3

# 피자 나눠 먹기(2)

'''
머쓱이네 피자가게는 피자를 여섯 조각으로 잘라 줍니다. 
피자를 나눠먹을 사람의 수 n이 매개변수로 주어질 때, n명이 주문한 피자를 남기지 않고 모두 같은 수의 피자 조각을 먹어야 한다면 최소 몇 판을 시켜야 하는지를 return 하도록 solution 함수를 완성해보세요.
'''
# 1)

import math

def solution(n):
    lcm = n * 6 // math.gcd(n, 6) # 피자 여섯 조각에 한 판인 피자를 n명이 모두 같은 수의 피자 조각을 먹을 수 있게 최소공배수 구함
    return lcm // 6

# 2)

def solution(n):

    answer = 1

    while (6 * answer) % n != 0: # 피자 판 수를 늘려가며 n명이 똑같이 나눠먹으면 나머지가 0이 되기 때문에 while문 탈출
        answer += 1

    return answer

print(solution(6)) # 1
print(solution(10)) # 5
print(solution(4)) # 2

# 피자 나눠 먹기(3)

'''
머쓱이네 피자가게는 피자를 두 조각에서 열 조각까지 원하는 조각 수로 잘라줍니다. 
피자 조각 수 slice와 피자를 먹는 사람의 수 n이 매개변수로 주어질 때, n명의 사람이 최소 한 조각 이상 피자를 먹으려면 최소 몇 판의 피자를 시켜야 하는지를 return 하도록 solution 함수를 완성해보세요.
'''
# 1)

def solution(slice, n):
    if n % slice != 0: # n명이 slice 조각 피자를 나눠먹는데 나머지가 있으면 피자 조각 부족한 것 -> 피자 한 판 추가
        answer = n // slice + 1
    else: # n이 slice의 배수라면 피자 조각 부족하지 않음
        answer = n // slice

    return answer

# 2)
import math
def solution(slice, n):
    return math.ceil(n / slice) # ceil(): 무조건 1 올림 -> n을 slice로 나눈 나머지가 존재하면 1판이 추가로 필요함

print(solution(7, 10)) # 2
print(solution(4, 12)) # 3

# 배열의 평균값

'''
정수 배열 numbers가 매개변수로 주어집니다. 
numbers의 원소의 평균값을 return하도록 solution 함수를 완성해주세요.
'''

# 평균 = 요소의 합 / 요소의 개수
def solution(numbers):
    return sum(numbers) / len(numbers)

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # 5.5
print(solution([89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])) # 94.0