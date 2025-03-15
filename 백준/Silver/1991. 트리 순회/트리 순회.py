nodes = int(input())
tree = {}

for _ in range(nodes):
    parent, leftChild, rightChild = input().split()
    tree[parent] = (leftChild, rightChild)

def preorder(node):
    if node == ".":
        return
    print(node, end="")
    preorder(tree[node][0])
    preorder(tree[node][1])


def midorder(node):
    if node == ".":
        return
    midorder(tree[node][0])  # 왼쪽 자식 방문
    print(node, end="")      # 현재 노드 출력
    midorder(tree[node][1])  # 오른쪽 자식 방문

def postorder(node):
    if node == ".":
        return
    postorder(tree[node][0])
    postorder(tree[node][1])
    print(node, end="")

root = list(tree.keys())[0]
preorder(root)
print()
midorder(root)
print()
postorder(root)