from pprint import pprint
from collections import deque


def rotate(queries, graph, answer):
    for query in queries:
        dq = deque()
        minus_one = [i-1 for i in query]
        y1, x1, y2, x2 = minus_one

        # 기준점에서 우측 넣기
        for i in graph[y1][x1:x2]:
            dq.append(i)
        # 우측 끝에서 아래쪽 넣기
        for i in [row[x2] for row in graph[y1:y2+1]]:
            dq.append(i)
        # 우측아래에서 왼쪽 넣기
        for i in graph[y2][x2-1:x1:-1]:
            dq.append(i)
        # 왼쪽아래에서 위쪽 넣기
        for i in [row[x1] for row in graph[y2:y1:-1]]:
            dq.append(i)
        # 한칸 이동을위한 사전작업
        dq.insert(0, dq.pop())
        # print(dq)

        # 최소값 넣기
        answer.append(min(dq))

        # 맵 이동시키기
        for i in range(x1, x2):
            graph[y1][i] = dq.popleft()
        for i in range(y1, y2+1):
            graph[i][x2] = dq.popleft()
        for i in range(x2-1, x1, -1):
            graph[y2][i] = dq.popleft()
        for i in range(y2, y1, -1):
            graph[i][x1] = dq.popleft()
        # pprint(graph)


def solution(rows, columns, queries):
    answer = []
    graph = [[(j * columns) + i + 1 for i in range(columns)] for j in range(rows)]
    rotate(queries, graph, answer)

    return answer


if __name__ == '__main__':
    rows, columns, queries, result = 6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]], [8, 10, 25]
    print(solution(rows, columns, queries))

    rows, columns, queries, result = 3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]], [1, 1, 5, 3]
    print(solution(rows, columns, queries))

    rows, columns, queries, result = 100, 97, [[1, 1, 100, 97]], [1]
    print(solution(rows, columns, queries))
