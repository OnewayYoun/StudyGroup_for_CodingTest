import sys
from pprint import pprint

input = sys.stdin.readline


def check_rows(y, x):
    if 1 <= x <= 14 and graph[y][x] == graph[y][x-1]:
        return False
    if x + 4 <= 18:
        for i in range(1, 5):
            if graph[y][x] == graph[y][x + i]:
                continue
            else:
                return False
        if x == 14:
            return True
        else:
            if graph[y][x] != graph[y][x + 5]:
                return True
    else:
        return False


def check_columns(y, x):
    if 1 <= y <= 14 and graph[y][x] == graph[y-1][x]:
        return False
    if y + 4 <= 18:
        for i in range(1, 5):
            if graph[y][x] == graph[y + i][x]:
                continue
            else:
                return False
        if y == 14:
            return True
        else:
            if graph[y][x] != graph[y + 5][x]:
                return True
    else:
        return False


def check_dig1(y, x):
    if 1 <= x <= 14 and 1 <= y <= 14 and graph[y][x] == graph[y-1][x-1]:
        return False
    if x + 4 <= 18 and y + 4 <= 18:
        for i in range(1, 5):
            if graph[y][x] == graph[y + i][x + i]:
                continue
            else:
                return False
        if x == 14 or y == 14:
            return True
        else:
            if graph[y][x] != graph[y + 5][x + 5]:
                return True
    else:
        return False


def check_dig2(y, x):
    if 1 <= x <= 14 and 0 <= y <= 17 and graph[y][x] == graph[y+1][x-1]:
        return False
    if x + 4 <= 18 and 0 <= y - 4:
        for i in range(1, 5):
            if graph[y][x] == graph[y - i][x + i]:
                continue
            else:
                return False
        if x == 14:
            return True
        else:
            if graph[y][x] != graph[y - 5][x + 5]:
                return True
    else:
        return False


if __name__ == '__main__':
    graph = [list(map(int, input().split())) for i in range(19)]

    flag = False
    for i in range(19):
        for j in range(19):
            if graph[j][i] == 1 or graph[j][i] == 2:
                if check_rows(j, i) or check_columns(j, i) or check_dig1(j, i) or check_dig2(j, i):
                    print(graph[j][i])
                    print(j + 1, i + 1)
                    flag = True
                    break
        if flag:
            break

    if not flag:
        print(0)

"""
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 1 2 0 0 2 2 2 1 0 0 0 0 0 0 0 0 0 0
0 0 1 2 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0
0 0 0 1 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 2 2 0 0 0 0 0 0 0 0 0 0 0 0
0 0 1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 2 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
"""
