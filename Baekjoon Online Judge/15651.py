from itertools import product

if __name__ == '__main__':
    n, m = map(int, input().split())
    permutations_with_duplication = product(range(1, n+1), repeat=m)
    for p in permutations_with_duplication:
        print(*p)