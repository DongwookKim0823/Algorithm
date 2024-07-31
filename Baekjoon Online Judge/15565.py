import sys

N, K = map(int, input().split())
dolls = list(map(int, input().split()))

left = 0
min_length = sys.maxsize
current_count = 0

for right in range(N):
    if dolls[right] == 1:
        current_count += 1

    while current_count >= K:
        min_length = min(min_length, right - left + 1)
        if dolls[left] == 1:
            current_count -= 1
        left += 1
        
print(-1 if min_length == sys.maxsize else min_length)
