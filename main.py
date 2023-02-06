class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(data, node.right)

    def in_order_traversal(self, node, result):
        if node.left:
            self.in_order_traversal(node.left, result)
        result.append(node.data)
        if node.right:
            self.in_order_traversal(node.right, result)
        return result

    def get_ascending_order(self):
        result = []
        return self.in_order_traversal(self.root, result)

    def get_descending_order(self):
        result = []
        return self.in_order_traversal(self.root, result)[::-1]


def create_tree(numbers):
    tree = BinaryTree()
    for number in numbers:
        tree.insert(number)
    return tree


numbers = [4, 2, 3, 1, 5]
tree = create_tree(numbers)
print("Ascending order:", tree.get_ascending_order())
print("Descending order:", tree.get_descending_order())