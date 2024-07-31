N, M = map(int, input().split())
nums = []
for _ in range(2):
    for i in map(int, input().split()):
        nums.append(i)

print(*sorted(nums))
