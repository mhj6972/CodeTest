def solution(n):
    k =1
    cnt = 0
    total = 0
    for i in range(1,n+1):
        k = i
        while k<=n:
            total += k
            if total > n:
                total = 0
                break
            elif total == n:
                cnt += 1
                total = 0
                break
            k += 1
    
    return cnt