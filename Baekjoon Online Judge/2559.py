N, K = map(int, input().split())
temperatures = list(map(int, input().split()))

current_sum = current_max = sum(temperatures[:K])

for i in range(1, N-K+1):
    current_sum = current_sum - temperatures[i-1] + temperatures[i+K-1]
    current_max = max(current_sum, current_max)

print(current_max)
