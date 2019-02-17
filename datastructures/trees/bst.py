class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None


class BSTree:
    def __init__(self):
        self.root = None

    def contains(self, key):
        current = self.root
        while current.key != key:
            if key < current.key:
                current = current.left
            else:
                current = current.right
            if current is None:
                return
        return current

    def insert(self, key, data):
        node = Node(key, data)
        if self.root is None:
            self.root = node
            return
        current = self.root
        while True:
            parent = current
            if key < current.key:
                current = current.left
                if current is None:
                    parent.left = node
                    break
            else:
                current = current.right
                if current is None:
                    parent.right = node
                    break

    def get_min(self):
        current = self.root
        left_most = self.root
        while current is not None:
            left_most = current
            current = current.left
        return left_most

    def get_max(self):
        current = self.root
        right_most = self.root
        while current is not None:
            right_most = current
            current = current.right
        return right_most

    def remove(self, key):
        if self.root is None:
            return
        current = self.root
        parent = self.root
        is_left = True
        while current.key != key:
            parent = current
            if key < current.key:
                is_left = True
                current = current.left
            else:
                is_left = False
                current = current.right
            if current is None:
                return

        if current.right is None is current.left:
            if self.root == current:
                self.root = None
            elif is_left:
                parent.left = None
            else:
                parent.right = None

        elif current.right is None:
            if self.root == current:
                self.root = None
            elif is_left:
                parent.left = current.left
            else:
                parent.left = current.left
        elif current.left is None:
            if self.root == current:
                self.root = None
            elif is_left:
                parent.left = current.right
            else:
                parent.right = current.right
        else:
            successor = self.get_successor(current)
            if self.root == current:
                self.root = successor
            elif is_left:
                parent.left = successor
            else:
                parent.right = successor

    @staticmethod
    def get_successor(node_to_delete):
        successor = node_to_delete
        successor_parent = node_to_delete
        current = node_to_delete.right

        while current is not None:
            successor_parent = successor
            successor = current
            current = current.left

        if current != node_to_delete.right:
            successor_parent.left = successor.right
            successor.right = node_to_delete.right

        return successor

    def pre_order(self, root):
        if root:
            print(root.key, root.data)
            self.pre_order(root.left)
            self.pre_order(root.right)

    def in_order(self, root):
        if root:
            self.pre_order(root.left)
            print(root.key, root.data)
            self.pre_order(root.right)

    def post_order(self, root):
        if root:
            self.post_order(root.left)
            self.post_order(root.right)
            print(root.key, root.data)
