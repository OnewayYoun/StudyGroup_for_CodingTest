def solution(rows, columns, queries):
    answer = []
    return answer


if __name__ == '__main__':
    rows, columns, queries, result = 6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]], [8, 10, 25]
    solution(rows,columns, queries)

    rows, columns, queries, result = 3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]], [1, 1, 5, 3]
    solution(rows, columns, queries)

    rows, columns, queries, result = 100, 97, [[1, 1, 100, 97]], [1]
    solution(rows, columns, queries)
