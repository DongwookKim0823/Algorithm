from typing import List


def func(a: List[int], b: List[int]) -> int:
    result = 0
    for a_member in a:
        left, right = 0, len(b) - 1
        while left <= right:
            mid = (left + right) // 2
            if a_member <= b[mid]:
                right = mid - 1
            else:
                left = mid + 1
        result += left

    return result


if __name__ == '__main__':
    count = int(input())
    for _ in range(count):
        a_size, b_size = map(int, input().split())
        a = sorted([int(i) for i in input().split()])
        b = sorted([int(i) for i in input().split()])

        print(func(a, b))
