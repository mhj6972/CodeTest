def solution(arr):
    answer = 0
    arr.sort(reverse=True)
    k = 1
    while True:
        temp = arr[0] * k
        flag = True
        for i in arr:
            if temp%i != 0:
                flag = False
                break
        if flag:
            return arr[0]*k
        k += 1
