class AvlTree:
    head = None

    class Node:
        value = None
        left = None
        right = None
        parent = None
        count = 1
        height = 0

        def __init__(self, value):
            self.value = value

        # Balance measures the right-heaviness
        # negative indicates left heaviness
        def balance(self):
            right_height = self.right.height if self.right else -1
            left_height = self.left.height if self.left else -1
            return right_height - left_height

        def rotateRight(self):
            new_parent = self.left
            new_grandparent = self.parent
            new_left_child = self.left.right
            # set new parent
            self.parent = new_parent
            new_parent.right = self
            # set new left
            self.left = new_left_child
            if new_left_child:
                new_left_child.parent = self
            # set new grandparent
            if new_grandparent:
                if new_grandparent.right == self:
                    new_grandparent.right = new_parent
                else:
                    new_grandparent.left = new_parent
            new_parent.parent = new_grandparent
            return new_grandparent if new_grandparent else new_parent

        def rotateLeft(self):
            # make right my new parent and rights parent my parent
            new_parent = self.right
            new_grandparent = self.parent
            new_right_child = self.right.left
            # set new parent
            self.parent = new_parent
            new_parent.left = self
            # set new left
            self.right = new_right_child
            if new_right_child:
                new_right_child.parent = self
            # set new grandparent
            if new_grandparent and new_grandparent.right == self:
                new_grandparent.right = new_parent
            elif new_grandparent:
                new_grandparent.left = new_parent
            new_parent.parent = new_grandparent
            return new_grandparent if new_grandparent else new_parent

        def reBalance(self):
            self.height = 1 + max(self.right.height if self.right else -1, self.left.height if self.left else -1)
            balance = self.balance
            new_parent = None
            if balance() > 1:
                if self.right.balance() < 0:
                    self.right.rotateRight()
                new_parent = self.rotateLeft()
            if balance() < -1:
                if self.left.balance() > 0:
                    self.left.rotateLeft()
                new_parent = self.rotateRight()
            return new_parent

        def appendChild(self, child):
            if child.value < self.value:
                if self.right:
                    self.right.appendChild(child)
                else:
                    child.parent = self
                    self.right = child
            elif child.value > self.value:
                if self.left:
                    self.left.appendChild(child)
                else:
                    child.parent = self
                    self.left = child
            else:
                self.count += 1
                return
            return self.reBalance()

        def inOrderTraversal(self):
            if self.left is None:
                if self.right is None:
                    return [self.value]
                return [self.value] + [self.right.inOrderTraversal()]
            return self.left.inOrderTraversal() + [self.value] + self.right.inOrderTraversal()

    def add(self, value):
        node = self.Node(value)
        if self.head:
            if np := self.head.appendChild(node):
                self.head = np
        else:
            self.head = node

    def all(self):
        return self.head.inOrderTraversal()


def levelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    res = [[root[0]]]
    next_indexes = [0]
    length = len(root)
    while next_indexes:
        layer = []
        children = []
        while next_indexes:
            if (index := next_indexes.pop()) is not None:
                if (child_one := index * 2 + 1) < length:
                    if item := root[child_one]:
                        layer.append(item)
                        children.append(child_one)
                if (child_two := index * 2 + 2) < length:
                    if (item := root[child_two]) is not None:
                        layer.append(item)
                        children.append(child_two)
        next_indexes = children
        if layer:
            res.append(layer)
    return res



t = AvlTree()
for i in range(1, 1000):
    t.add(i)
t.all()
