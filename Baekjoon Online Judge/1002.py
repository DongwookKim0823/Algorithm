import math

if __name__ == '__main__':
    for _ in range(int(input())):
        x1, y1, r1, x2, y2, r2 = map(int, input().split())
        
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        r_sum = r1 + r2
        r_diff = abs(r1 - r2)
        
        if x1 == x2 and y1 == y2 and r1 == r2:
            print(-1)
        elif distance == r_sum or distance == r_diff:
            print(1)
        elif r_diff < distance < r_sum:
            print(2)
        else:
            print(0)
