def solution(n):
    cnt = 1
    for i in range(1, n//2 + 1):
        temp = 0
        for j in range(i, n + 1):
            temp += j
            if temp > n:
                break
            elif temp == n:
                cnt += 1
                break

    return cnt