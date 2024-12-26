import sys
from collections import defaultdict

input = sys.stdin.readline

if __name__ == '__main__':
    q, a = map(int, input().split())
    
    password_dict = defaultdict(str)
    for _ in range(q):
        url, password = input().split()
        password_dict[url] = password

    for _ in range(a):
        url = input().rstrip()
        print(password_dict[url])
