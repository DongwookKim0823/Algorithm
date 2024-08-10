import sys
from itertools import permutations


def calculator(nums, operators):
    result = nums[0]
    for index, num in enumerate(nums[1:]):
        operator = operators[index]
        if operator == 0:
            result += num
        elif operator == 1:
            result -= num
        elif operator == 2:
            result *= num
        elif operator == 3:
            if result < 0 and num > 0:
                result = abs(result) // num
                result *= -1
            else:
                result //= num

    return result


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    operators = []
    for index, count in enumerate(map(int, input().split())):
        operators.extend([index] * count)

    operators_permutation = set(permutations(operators))

    max_result = -sys.maxsize
    min_result = sys.maxsize
    for operator in operators_permutation:
        max_result = max(max_result, calculator(nums, operator))
        min_result = min(min_result, calculator(nums, operator))

    print(max_result)
    print(min_result)
