import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
a.sort()

L, R = 0, n - 1
sum = 2_000_000_001
result = []
while L < R:
    if abs(a[L] + a[R]) < sum:
        sum = abs(a[L] + a[R])
        result = [a[L], a[R]]

    if a[L] + a[R] < 0:
        L += 1
    else:
        R -= 1

result.sort()
print(*result)
