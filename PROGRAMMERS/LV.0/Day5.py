# 옷가게 할인 받기

'''
머쓱이네 옷가게는 10만 원 이상 사면 5%, 30만 원 이상 사면 10%, 50만 원 이상 사면 20%를 할인해줍니다.
구매한 옷의 가격 price가 주어질 때, 지불해야 할 금액을 return 하도록 solution 함수를 완성해보세요.
'''
def solution(price):
    if price >= 500000:
        answer = price * 0.8
    elif price >= 300000:
        answer = price * 0.9
    elif price >= 100000:
        answer = price * 0.95
    else:
        answer = price

    return int(answer)

print(solution(150,000)) # 142,500
print(solution(580,000)) # 464,000

# 아이스 아메리카노

'''
머쓱이는 추운 날에도 아이스 아메리카노만 마십니다. 
아이스 아메리카노는 한잔에 5,500원입니다. 
머쓱이가 가지고 있는 돈 money가 매개변수로 주어질 때, 머쓱이가 최대로 마실 수 있는 아메리카노의 잔 수와 남는 돈을 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.
'''

# 1)

def solution(money):
    coffee = 0

    while money >= 5500:
        coffee = money // 5500
        remain = money % 5500
        return coffee, remain

    else:
        return coffee, money
    
# 2)

def solution(money):
    answer = [money // 5500, money % 5500]
    return answer

print(solution(5,500)) # [1, 0]
print(solution(15,000)) # [2, 4000]

# 나이 출력

'''
머쓱이는 선생님이 몇 년도에 태어났는지 궁금해졌습니다. 
2022년 기준 선생님의 나이 age가 주어질 때, 선생님의 출생 연도를 return 하는 solution 함수를 완성해주세요
'''

def solution(age):
    answer = 2022 - age + 1
    return answer

print(solution(40)) # 1983
print(solution(23)) # 2000


# 배열 뒤집기

'''
정수가 들어 있는 배열 num_list가 매개변수로 주어집니다. 
num_list의 원소의 순서를 거꾸로 뒤집은 배열을 return하도록 solution 함수를 완성해주세요.
'''

def solution(num_list):
    answer = num_list[::-1]
    return answer

print(solution([1, 2, 3, 4, 5])) # [5, 4, 3, 2, 1]
print(solution([1, 1, 1, 1, 1, 2])) # [2, 1, 1, 1, 1, 1]
print(solution([1, 0, 1, 1, 1, 3, 5])) # [5, 3, 1, 1, 1, 0, 1]