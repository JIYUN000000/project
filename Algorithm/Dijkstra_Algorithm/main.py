INF = 1000000000
number = 6

# 그래프 인접 행렬(a[i][j]는 i에서 j로 가는 비용)
a = [
    [0, 2, 5, 1, INF, INF],
    [2, 0, 3, 2, INF, INF],
    [5, 3, 0, 3, 1, 5],
    [1, 2, 3, 0, 1, INF],
    [INF, INF, 1, 1, 0, 2],
    [INF, INF, 5, INF, 2, 0]
]

v = [False] * number # 방문 여부
d = [0] * number # 최단 거리

# 가장 최단 거리를 가지는 노드의 인덱스 반환
def get_small_index():
    min_value = INF
    index = 0
    for i in range(number):
        if d[i] < min_value and not v[i]:
            min_value = d[i]
            index = i
    return index

# 다익스트라 알고리즘
def dijkstra(start):
    for i in range(number):
        d[i] = a[start][i]
    v[start] = True
    for i in range(number - 2):
        current = get_small_index()
        v[current] = True
        for j in range(number):
            if not v[j]:
                if d[current] + a[current][j] < d[j]:
                    d[j] = d[current] + a[current][j]

dijkstra(0)

# 출력
for i in range(number):
    print(d[i], end='')
