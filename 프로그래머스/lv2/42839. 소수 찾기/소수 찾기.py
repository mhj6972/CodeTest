import math 
from itertools import permutations

def is_prime(n):
    if n==0 or n==1:
        return False
    else:
        for i in range(2, int(math.sqrt(n))+1):
            if n % i ==0:
                return False 
        return True
    
def solution(numbers):
    ans = []
    temp = []
    for i in range(1,len(numbers)+1):
        arr = permutations(list(numbers),i)
        for j in arr:
            ans.append(int(''.join(j)))
    
    ans = list(set(ans))
    for i in range(len(ans)):
        print(ans[i])
        if is_prime(int(ans[i])):
            temp.append(int(ans[i]))
    
    return len(temp)