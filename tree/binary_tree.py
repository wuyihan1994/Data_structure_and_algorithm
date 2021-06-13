class TreeNode():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder_traversal(root):
    if root == None:
        return
    print(root.val)
    preorder_traversal(root.left)
    preorder_traversal(root.right)

def preorder_traversal_non_recursive(root):
    stack = []
    while root:
        stack.append(root)
        print(root.val)
        root = root.left
    while stack:
        node = stack.pop(-1)
        node = node.right
        while node:
            stack.append(node)
            print(node.val)
            node = node.left


def in_order_traversal(root):
    if root == None:
        return
    in_order_traversal(root.left)
    print(root.val)
    in_order_traversal(root.right)


def in_order_traversal_non_recursive(root):
    stack = []
    while root:
        stack.append(root)
        root = root.left
    while stack:
        node = stack.pop(-1)
        print(node.val)
        node = node.right
        while node:
            stack.append(node)
            node = node.left

def post_order_traversal(root):
    if root == None:
        return
    post_order_traversal(root.left)
    post_order_traversal(root.right)
    print(root.val)


def post_order_traversal_non_recursive(root):
    stack, flag  = [], []
    while root:
        stack.append(root)
        flag.append(1)
        root = root.left
    while stack:
        node = stack[-1]
        if node.right:
            if flag[-1] == 1:
                node = node.right
                flag[-1] = 2
                while node:
                    stack.append(node)
                    flag.append(1)
                    node = node.left
            else:
                node = stack.pop(-1)
                flag.pop(-1)
                print(node.val)
        else:
            node = stack.pop(-1)
            flag.pop(-1)
            print(node.val)


def output_binary_tree_by_pre_and_in_order(preorder, inorder):
    if not preorder:
        return
    root = TreeNode(preorder[0])
    index = inorder.index(root.val)
    root.left = output_binary_tree_by_pre_and_in_order(preorder[1:index+1], inorder[:index])
    root.right = output_binary_tree_by_pre_and_in_order(preorder[index+1:], inorder[index+1:])
    return root



t4 = TreeNode(4)
t5 = TreeNode(5)
t6 = TreeNode(6)
t7 = TreeNode(7)
t2 = TreeNode(2, t4, t5)
t3 = TreeNode(3, t6, t7)
t1 = TreeNode(1, t2, t3)

root = output_binary_tree_by_pre_and_in_order([1,2,4,5,3,6,7], [4,2,5,1,6,3,7])
post_order_traversal(root)