import sys

n = int(sys.stdin.readline())
cards = []
count_card = {}
for _ in range(n):
    cards.append(int(sys.stdin.readline()))

for card in cards:
    if card in count_card:
        count_card[card] += 1
    else:
        count_card[card] = 1

count_card_tuple = list(zip(count_card.keys(), count_card.values()))
count_card_tuple.sort(key=lambda x: (-x[1], x[0]))
print(count_card_tuple[0][0])
