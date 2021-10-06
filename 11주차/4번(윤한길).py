import sys


input = sys.stdin.readline


if __name__ == '__main__':
    N = int(input())
    TP = [list(map(int, input().split())) for _ in range(N)]


"""
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200
"""