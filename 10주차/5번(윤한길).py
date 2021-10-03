import sys
from collections import deque
from itertools import combinations, permutations

input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    nums = [i + 1 for i in range(N)]
    all_possible_combs = []
    min_num = float('inf')

    dq = deque()
    for i in combinations(nums, N // 2):
        dq.append(i)

    while dq:
        all_possible_combs.append([dq.popleft(), dq.pop()])

    # print(all_possible_combs)
    for i in all_possible_combs:
        tmp = []
        for j in i:
            sum = 0
            for per in permutations(j, 2):
                sum += S[per[0] - 1][per[1] - 1]
            tmp.append(sum)
        min_num = min(min_num, abs(tmp[0] - tmp[1]))
    print(min_num)

"""
6
0 1 2 3 4 5
1 0 2 3 4 5
1 2 0 3 4 5
1 2 3 0 4 5
1 2 3 4 0 5
1 2 3 4 5 0

result = 2
"""
