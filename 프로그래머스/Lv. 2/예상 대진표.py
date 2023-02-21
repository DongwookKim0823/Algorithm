def solution(n,a,b):
    game = [0 for _ in range(n)]
    game[a - 1] = 1
    game[b - 1] = 1

    cnt = 0
    while game.count(1) != 1:
        cnt += 1

        next_game = []
        for i in range(len(game) // 2):
            if game[i * 2] == 1 or game[i * 2 + 1] == 1:
                next_game.append(1)
            else:
                next_game.append(0)

        game = next_game

    return cnt