from collections import defaultdict

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

card_dict = defaultdict(int)
for card in cards:
    card_dict[card] += 1

result = []
for target in targets:
    result.append(card_dict[target])

print(*result, sep=' ')
