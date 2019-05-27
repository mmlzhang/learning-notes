

class Node(object):

    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):

    def __init__(self):
        self.root = Node()
        self.my_queue = []

    def add(self, elem):
        node = elem(elem)
        if self.root.elem == -1:
            self.root = node
            self.my_queue.append(self.root)
        else:
            tree_node = self.my_queue[0]
            if tree_node.lchild == None:
                tree_node.lchild = node
                self.my_queue.append(tree_node.lchild)
            else:
                tree_node.rchild = node
                self.my_queue.append(tree_node.rchild)
                self.my_queue.pop(0)

    def front_digui(self, root):
        """递归实现　先序遍历"""
        if root == None:
            return None
        print(root.elem)
        self.front_digui(root.lchild)
        self.front_digui(root.rchild)

    def middle_digui(self, root):
        """中序遍历"""
        if root == None:
            return None
        self.middle_digui(root.lchild)
        print(root.elem)
        self.middle_digui(root.rchild)

    def later_digui(self, root):
        """后序遍历"""
        if not root:
            return None
        self.later_digui(root.lchild)
        self.later_digui(root.rchild)
        print(root.elem)

    """堆栈实现"""

    def front_stack(self, root):
        """先序遍历"""
        if not root:
            return None
        my_stack = []
        node = root
        while node or my_stack:
            while node:
                print(node.elem)
                node = node.child
            node = my_stack.pop()
            node = node.rchild

    def middle_stack(self, root):
        """中序遍历"""
        if not root:
            return None
        my_stack = []
        node = root
        while node or my_stack:
            while node:
                my_stack.append(node)
                node = node.lchild
            node = my_stack.pop()
            print(node.elem)
            node = node.rchild

    def later_stack(self, root):
        """后序遍历"""
        if not root:
            return
        my_stack1 = []
        my_stack2 = []
        node = root
        my_stack1.append(node)
        while my_stack1:
            node = my_stack1.pop()
            if node.lchild:
                my_stack1.append(node.lchild)
            if node.rchild:
                my_stack1.append(node.rchild)
            my_stack2.append(node)
        while my_stack2:
            print(my_stack2.pop().elem)

    def level_queue(self, root):
        """层次遍历　队列实现"""
        if not root:
            return
        my_queue = []
        node = root
        my_queue.append(node)
        while my_queue:
            node = my_queue.pop(0)
            print(node.elem)
            if node.lchild:
                my_queue.append(node.lchild)
            if node.rchild:
                my_queue.append(node.rchild)
