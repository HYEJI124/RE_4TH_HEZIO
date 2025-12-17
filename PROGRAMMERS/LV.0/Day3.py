# 나머지 구하기

'''
정수 num1, num2가 매개변수로 주어질 때, num1를 num2로 나눈 나머지를 return 하도록 solution 함수를 완성해주세요.
'''

def solution(num1, num2):
    answer = num1 % num2
    return answer

print(solution(3, 2)) # 1
print(solution(10, 5)) # 0

# 중앙값 구하기

'''
중앙값은 어떤 주어진 값들을 크기의 순서대로 정렬했을 때 가장 중앙에 위치하는 값을 의미합니다. 
예를 들어 1, 2, 7, 10, 11의 중앙값은 7입니다. 정수 배열 array가 매개변수로 주어질 때, 중앙값을 return 하도록 solution 함수를 완성해보세요.
'''

def solution(array):
    array.sort()
    answer = array[len(array) // 2]
    return answer

print(solution([1, 2, 7, 10, 11])) # 7
print(solution([9, -1, 0])) # 0

# 최빈값 구하기

'''
최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다. 
정수 배열 array가 매개변수로 주어질 때, 최빈값을 return 하도록 solution 함수를 완성해보세요. 최빈값이 여러 개면 -1을 return 합니다.
'''

# 예시: [1, 2, 3, 3, 3, 4]
def solution(array):
    # max(array) = 4 -> [0, 0, 0, 0, 0]
    count = [0] * (max(array) + 1) # 횟수 저장할 리스트 초기화

    for i in array: # 각 숫자가 몇 번 나왔는 지 count에 기록
        count[i] += 1 # [0, 1, 1, 3, 1]

    m = 0 # 최빈값 개수 확인하기 위한 변수

    for c in count: # 최빈값 개수를 확인하기 위함
        if c == max(count): # c가 기존의 최빈값 개수와 같다면 최빈값 개수 증가
            m += 1 
    
    if m > 1: # 최빈값이 여러 개면 -1 반환
        return -1
    else: # 최빈값이 한 개면 최빈값의 인덱스 반환
        return count.index(max(count))

print(solution([1, 2, 3, 3, 3, 4])) # 3
print(solution([1, 1, 2, 2])) # -1
print(solution([1])) # 1

# 짝수는 싫어요

'''
정수 n이 매개변수로 주어질 때, n 이하의 홀수가 오름차순으로 담긴 배열을 return하도록 solution 함수를 완성해주세요.
'''
# 1)
def solution(n):
    answer = []
    for i in range(1, n+1, 2):
        answer.append(i)
    return answer

# 2)
def solution(n):
    return list(range(1, n+1, 2))

print(solution(10)) # [1, 3, 5, 7, 9]
print(solution(15)) # [1, 3, 5, 7, 9, 11, 13, 15]