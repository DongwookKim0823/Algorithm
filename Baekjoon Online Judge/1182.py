def recursive_sum(index, current_sum):
    global count
    if index == n:
        if current_sum == s:
            count += 1
        return

    recursive_sum(index + 1, current_sum)
    recursive_sum(index + 1, current_sum + nums[index])


if __name__ == "__main__":
    n, s = map(int, input().split())
    nums = list(map(int, input().split()))
    count = 0

    recursive_sum(0, 0)

    if s == 0:
        count -= 1

    print(count)

# 완전 탐색 풀이
# import itertools
# 
# if __name__ == "__main__":
#     n, s = map(int, input().split())
#     nums = list(map(int, input().split()))
#     count = 0
# 
#     for i in range(1, n+1):
#         for j in itertools.combinations(nums, i):
#             if sum(j) == s:
#                 count += 1
# 
#     print(count)
