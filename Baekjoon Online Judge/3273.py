def binary_search(nums, target):

    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return 0


if __name__ == '__main__':
    n = int(input())
    nums = sorted(map(int, input().split()))
    x = int(input())

    result = 0
    for num in nums:
        target = x - num

        result += binary_search(nums, target)

    print(result//2)

