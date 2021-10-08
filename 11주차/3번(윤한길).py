import sys
input = sys.stdin.readline


# 투포인터 방식
def two_pointer():
    n = int(input())
    sequence = list(map(int, input().split()))

    right = 0
    sum = 0
    max_num = -float('inf')

    for left in range(n):
        while sum >= 0 and right < n:
            sum += sequence[right]
            right += 1
            max_num = max(max_num, sum)
        sum -= sequence[left]
    print(max_num)


# dp 방식
def sol_with_dp():
    n = int(input())
    sequence = list(map(int, input().split()))
    dp = [0] * n
    dp[0] = sequence[0]

    for i in range(1, n):
        dp[i] = max(sequence[i], dp[i-1] + sequence[i])

    print(max(dp))


if __name__ == '__main__':
    two_pointer()
    # sol_with_dp()


"""
10
10 -4 3 1 5 6 -35 12 21 -1
"""