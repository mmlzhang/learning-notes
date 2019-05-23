

class Node(object):

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.right = right
        self.left = left


tree = Node(1, )


# 层次遍历
def lookup(root):
    row = [root]
    while row:
        print(row)
        row = [kid for item in row for kid in (item.left, item.right) if kid]


# 深度遍历
def deep(root):
    if not root:
        return Node
    print(root.data)
    deep(root.left)
    deep(root.right)


# 前中后遍历


# 最大树深度
def max_depth(root):
    if not root:
        return 0
    return max(max_depth(root.left), max_depth(root.right)) + 1


# 前中后求序
def rebuild(pre, center):
    if not pre:
        return None
    cur = Node(pre[0])
    index = center.index(pre[0])
    cur.left = rebuild(pre[1: index + 1], center[:index])
    cur.right = rebuild(pre[index + 1:], center[index + 1:])
    return cur
