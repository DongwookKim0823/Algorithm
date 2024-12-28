import sys

input = sys.stdin.readline


if __name__ == '__main__':
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    
    nums_acc = [0] * (n + 1)
    
    acc_num = 0
    for i, num in enumerate(nums, start=1):
        acc_num += num
        nums_acc[i] = acc_num
        
    for _ in range(m):
        start, end = map(int, input().split())
        print(nums_acc[end] - nums_acc[start - 1])
