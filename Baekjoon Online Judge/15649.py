if __name__ == '__main__':
    n, m = map(int, input().split())
    selected = []

    def recursive_func(k):
        if k == m:
            print(*selected)
        else:
            for i in range(1, n + 1):
                if i not in selected:
                    selected.append(i)
                    recursive_func(k + 1)
                    selected.pop()

    recursive_func(0)
