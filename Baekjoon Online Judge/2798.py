from itertools import combinations


if __name__ == '__main__':
    n, m = map(int, input().split())
    cards = list(map(int, input().split()))
    
    result = 0
    for comb in combinations(cards, 3):
        cand = sum(comb)
        if result < cand and cand <= m:
            result = cand
    
    print(result)
