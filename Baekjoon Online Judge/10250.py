import sys

input = sys.stdin.readline


if __name__ == '__main__':
    
    T = int(input())
    for _ in range(T):
        H, W, N = map(int, input().split())
        floor = H if N % H == 0 else N % H
        room = N // H if N % H == 0 else N // H + 1
        print(f'{floor}{room:02d}')
