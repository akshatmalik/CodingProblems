import collections
import queue


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def dfs_binary_tree(node):
    if node is not None:
        # Visit the current node
        print(node.value, end=' ')

        # Recursively visit the left and right subtrees
        dfs_binary_tree(node.left)
        dfs_binary_tree(node.right)

def bfs_binary_tree(node):

    if node is None:
        return

    q = collections.deque()
    q.append(node)

    while q:

        node = q.popleft()

        print(node.value, end=' ')

        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)




# Create a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Perform DFS traversal on the binary tree
print("DFS traversal of the binary tree:")
dfs_binary_tree(root)
print()
print("BFS traversal of the binary tree:")
bfs_binary_tree(root)
