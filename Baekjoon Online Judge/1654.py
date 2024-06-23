def binary_search(lines, target_count):
    left, right = 1, max(lines)

    while left <= right:
        mid = (left + right) // 2

        count = sum(line // mid for line in lines)
        if count >= target_count:
            left = mid + 1
        else:
            right = mid - 1
            
    return right


if __name__ == '__main__':
    k, n = map(int, input().split())
    lines = [int(input()) for _ in range(k)]

    result = binary_search(lines, n)
    print(result)
    
