import math

if __name__ == '__main__':
    n = int(input())
    tshirts = list(map(int, input().split()))
    t, p = map(int, input().split())
    
    print(sum(math.ceil(tshirt / t) for tshirt in tshirts))
    print(sum(tshirts) // p, sum(tshirts) % p)
