import sys


def find_minimum_gap(nums, target):
    nums.sort()

    left, right = 0, 1
    min_gap = sys.maxsize

    while right < len(nums):
        gap = nums[right] - nums[left]
        if gap < target:
            right += 1
        else:
            min_gap = min(min_gap, gap)
            left += 1

            if left == right:
                right += 1

    return min_gap


if __name__ == '__main__':
    N, M = map(int, input().split())
    nums = [int(input()) for _ in range(N)]

    result = find_minimum_gap(nums, M)
    print(result)
