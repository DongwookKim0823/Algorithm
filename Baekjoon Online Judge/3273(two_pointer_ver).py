def find_count(nums, x):
    nums.sort()
    left, right = 0, len(nums) - 1
    count = 0

    while left < right:
        sum = nums[left] + nums[right]
        if sum == x:
            count += 1
            left += 1
        elif sum < x:
            left += 1
        else:
            right -= 1

    return count


if __name__ == '__main__':
    N = int(input())
    nums = list(map(int, input().split()))
    x = int(input())

    result = find_count(nums, x)
    print(result)
