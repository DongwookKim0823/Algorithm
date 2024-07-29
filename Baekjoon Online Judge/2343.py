def can_divide(videos, mid, M):
    acc_length = 0
    divide_count = 1
    for video in videos:
        if acc_length + video > mid:
            divide_count += 1
            acc_length = video
            if divide_count > M:
                return False
        else:
            acc_length += video

    return True


def binary_search(videos, M):
    left, right = max(videos), sum(videos)
    while left <= right:
        mid = (left + right) // 2
        if can_divide(videos, mid, M):
            right = mid - 1
        else:
            left = mid + 1

    return left


if __name__ == '__main__':
    N, M = map(int, input().split())
    videos = list(map(int, input().split()))

    print(binary_search(videos, M))
