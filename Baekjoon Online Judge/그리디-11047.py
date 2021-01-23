import sys

N, K = map(int, sys.stdin.readline().strip().split())

wallet = []
for i in range(N):
  wallet.append(int(sys.stdin.readline().strip()))

result = 0
for i in reversed(wallet):
  if i > K:
    continue
  
  result += K//i
  K %= i

print(result)