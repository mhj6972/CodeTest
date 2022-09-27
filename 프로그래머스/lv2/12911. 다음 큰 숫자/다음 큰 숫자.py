def solution(n):
    answer = 0
    k = n+1
    stop = binary(n)
    while stop != binary(k):
        k += 1
    
    return k

def binary(n):
    answer = ''
    cnt = 0
    while n!=0:
        answer += str(n%2)
        if n%2 == 1: cnt += 1
        n //= 2
    return cnt