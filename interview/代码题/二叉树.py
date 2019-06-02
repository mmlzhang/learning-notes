

class Node(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def display(tree):

    if tree is None:
        return

    if tree.right is not None:
        display(tree.right)

    print(tree.value)

    if tree.left is not None:
        display(tree.left)

    return


def depth_of_tree(tree):

    if tree is None:
        return 0

    else:
        depth_l_tree = depth_of_tree(tree.left)
        depth_r_tree = depth_of_tree(tree.right)
        if depth_l_tree > depth_r_tree:
            return depth_l_tree + 1
        else:
            return depth_r_tree + 1


def is_full_tree(tree):
    if tree is None:
        return True
    if (tree.left is None) and (tree.right is None):
        return True
    if (tree.left is not None) and (tree.right is None):
        return is_full_tree(tree.left) and is_full_tree(tree.right)
    return False


if __name__ == '__main__':
    tree = Node(1)
    tree.left = Node(2)
    # tree.left.left = Node(4)
    # tree.left.right = Node(5)
    # tree.left.right.left = Node(6)

    tree.right = Node(3)
    # tree.right.left = Node(7)
    # tree.right.left.left = Node(8)
    # tree.right.left.left.right = Node(9)

    print(is_full_tree(tree))
    print(depth_of_tree(tree))
    print("Tree is: ")
    print(display(tree))
