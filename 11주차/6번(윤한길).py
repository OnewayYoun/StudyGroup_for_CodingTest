import sys

input = sys.stdin.readline

if __name__ == '__main__':
    N, C = map(int, input().split())
    l = [int(input()) for _ in range(N)]
    l.sort()
    # print(l)

    left, right = 1, l[-1] - l[0]

    answer = 0
    while left <= right:
        mid = (left + right) // 2
        cnt = 1
        current = l[0]

        for i in range(1, len(l)):
            if l[i] >= current + mid:
                cnt += 1
                current = l[i]

        if cnt >= C:
            left = mid + 1
            answer = mid
        elif cnt < C:
            right = mid - 1

print(answer)