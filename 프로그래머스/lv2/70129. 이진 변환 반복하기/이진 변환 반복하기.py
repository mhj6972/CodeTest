def solution(s):
    answer = []
    left = 0
    cnt = 0
    right = s
    while right != "1":
        a = right.count("1")
        left += len(right) - a
        right = str(bin(a)[2:])
        cnt += 1
    return [cnt,left]