from typing import List


def two_pointer(nums: List[int], target: int) -> int:
    result = 0
    num_sum = 0
    j = 0

    for i in range(len(nums)):
        while j < len(nums) and num_sum < target:
            num_sum += nums[j]
            j += 1
        if num_sum == target:
            result += 1
        num_sum -= nums[i]

    return result


if __name__ == '__main__':
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    print(two_pointer(nums, int(m)))
