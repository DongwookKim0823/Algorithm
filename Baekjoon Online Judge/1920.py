import sys


def binary_search(array, n):
    left, right = 0, len(array) - 1

    while left <= right:
        mid = (left + right) // 2

        if array[mid] == n:
            return 1
        elif array[mid] > n:
            right = mid - 1
        elif array[mid] < n:
            left = mid + 1

    return 0


def main():
    input = sys.stdin.readline

    n = int(input())
    target_array = list(map(int, input().split()))
    target_array.sort()

    m = int(input())
    source_array = list(map(int, input().split()))

    for source in source_array:
        print(binary_search(target_array, source))


if __name__ == "__main__":
    main()
