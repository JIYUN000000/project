class Edge:
    def __init__(self, a, b, distance):
        self.node = [a, b] # 두 노드 저장
        self.distance = distance # 거리(비용) 정보 저장

    # '__lt__'는 두 객체 간의 '<' 연산을 정의
    def __lt__(self, other):
        return self.distance < other.distance  # 거리 기준으로 오름차순 비교

# 부모 노드를 가져오는 함수
def getParent(set, x):
    if set[x] == x: # x는 이미 루트 노드이고, 더 이상 부모를 찾을 필요가 없으므로 x를 반환
        return x
    set[x] = getParent(set, set[x]) # 경로 압축
    return set[x]

# 부모 노드를 병합하는 함수
def unionParent(set, a, b):
    a = getParent(set, a)
    b = getParent(set, b)
    if a < b:
        set[b] = a
    else:
        set[a] = b

# 같은 부모를 가지는지 확인하는 함수
def find(set, a, b):
    a = getParent(set, a)
    b = getParent(set, b)
    if a == b:
        return True
    return False

def main():
    n = 7 # 정점의 수
    m = 11 # 간선의 수

    v = []
    v.append(Edge(1, 7, 12))
    v.append(Edge(1, 4, 28))
    v.append(Edge(1, 2, 67))
    v.append(Edge(1, 5, 17))
    v.append(Edge(2, 4, 24))
    v.append(Edge(2, 5, 62))
    v.append(Edge(3, 5, 20))
    v.append(Edge(3, 6, 37))
    v.append(Edge(4, 7, 13))
    v.append(Edge(5, 6, 45))
    v.append(Edge(5, 7, 73))

    # 간선의 비용을 기준으로 오름차순 저장
    v.sort()


    # 각 정점이 포함된 그래프의 부모를 저장
    # 부모 배열 초기화, 각 정점이 자기 자신을 부모로 시작
    parent = list(range(n))
    print(parent)

    sum = 0
    for edge in v:
        # 사이클이 발생하지 않는 경우 그래프에 포함
        if not find(parent, edge.node[0] - 1, edge.node[1] - 1):
            sum += edge.distance
            unionParent(parent, edge.node[0] - 1, edge.node[1] - 1)

    print(sum)

if __name__ == "__main__":
    main()
