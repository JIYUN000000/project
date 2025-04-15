class TreeNode:
    def __init__(self, data):
        self.data = data # 이 노드에 저장될 값을 기록
        self.leftChild = None # 왼쪽 자식 노드, 처음엔 없음 (추후 연결)
        self.rightChild = None # 오른쪽 자식 노드, 처음엔 없음

# 전위 순회
def preorder(node):
    if node: # if node가 false일 때, 오른쪽 노드로 이동
        print(node.data, end=' ')
        preorder(node.leftChild)
        preorder(node.rightChild)

# 중위 순회
def inorder(node):
    if node:
        inorder(node.leftChild)
        print(node.data, end=' ')
        inorder(node.rightChild)

# 후위 순회
def postorder(node):
    if node:
        postorder(node.leftChild)
        postorder(node.rightChild)
        print(node.data, end=' ')

# 노드 생성
number = 15 # 총 노드 개수 설정
# 인덱스 1번부터 쓰기 위해 0번 인덱스에 None을 넣음
# TreeNode(1)부터 TreeNode(15)까지 15개의 노드 생성
nodes = [None] + [TreeNode(i) for i in range(1, number + 1)]

# 트리 연결 (완전 이진 트리 구조)
# leftChild와 rightChild는 TreeNode 객체를 가리키는 변수 (포인터)
for i in range(1, number + 1):
    if i * 2 <= number:
        nodes[i].leftChild = nodes[i * 2]
    if i * 2 + 1 <= number:
        nodes[i].rightChild = nodes[i * 2 + 1]

# 순회 테스트
print("Preorder:")
preorder(nodes[1])  # 루트는 nodes[1]

print("\nInorder:")
inorder(nodes[1])

print("\nPostorder:")
postorder(nodes[1])
