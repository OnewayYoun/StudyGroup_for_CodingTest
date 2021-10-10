from math import ceil
import sys
from itertools import permutations
input = sys.stdin.readline


if __name__ == '__main__':
    N = int(input())
    sequence = list(map(int, input().split()))
    operators = list(map(int, input().split()))     # [덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)]
    ops = []

    for i, v in enumerate(operators):
        if i == 0:
            for _ in range(v):
                ops.append('+')
        elif i == 1:
            for _ in range(v):
                ops.append('-')
        elif i == 2:
            for _ in range(v):
                ops.append('*')
        elif i == 3:
            for _ in range(v):
                ops.append('/')

    answer = []
    for com in permutations(ops, len(ops)):
        tmp = sequence[0]
        for i in range(1, len(sequence)):
            if com[i-1] == '+':
                tmp += sequence[i]
            elif com[i-1] == '-':
                tmp -= sequence[i]
            elif com[i-1] == '*':
                tmp *= sequence[i]
            elif com[i-1] == '/':
                if tmp < 0:
                    tmp = ceil(tmp/sequence[i])
                else:
                    tmp = tmp // sequence[i]
        answer.append(tmp)

    print(max(answer))
    print(min(answer))

"""
6
1 2 3 4 5 6
2 1 1 1
"""