def recursive_func(n, current_sum):
    if current_sum > n:
        return 0
    if current_sum == n:
        return 1

    return recursive_func(n, current_sum + 1) + recursive_func(n, current_sum + 2) + recursive_func(n, current_sum + 3)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        sum = 0
        result = recursive_func(n, 0)
        print(result)
