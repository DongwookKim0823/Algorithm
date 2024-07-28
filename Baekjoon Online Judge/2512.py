def binary_search(budgets, M):
    left, right = 0, max(budgets)

    while left <= right:
        mid = (left + right) // 2

        accumulated_budget = sum((min(budget, mid) for budget in budgets))

        if accumulated_budget <= M:
            left = mid + 1
        else:
            right = mid - 1
            
    return right


if __name__ == '__main__':
    N = int(input())
    budgets = list(map(int, input().split()))
    M = int(input())

    if sum(budgets) <= M:
        print(max(budgets))
    else:
        print(binary_search(budgets, M))
