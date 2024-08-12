if __name__ == '__main__':
    n, m = map(int, input().split())
    selected = []

    def recursive_func(k):
        if m == k:
            print(*selected)
        else:
            for i in range(1, n + 1):
                if not selected or selected[-1] <= i:
                    selected.append(i)
                    recursive_func(k + 1)
                    selected.pop()

    recursive_func(0)
