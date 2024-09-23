# standard node, + left and right, + height(for fast work time)
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None
        # root is just "main" node

    def height(self, node):
        # height - quantity of node
        if not node:
            return 0
        return node.height

    def balance(self, node):
        # balancing tree
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def insert(self, root, value):
        if not root:
            return Node(value)
        elif value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)

        if balance > 1 and value < root.left.value:
            # Left rotation
            return self.right_rotate(root)

        if balance < -1 and value > root.right.value:
            # Right rotation
            return self.left_rotate(root)

        if balance > 1 and value > root.left.value:
            # Left-Right rotation
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and value < root.right.value:
            # Right-Left rotation
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    # delete node, delete main node -> find new main, remake high of node
    def delete(self, root, value):
        if not root:
            return root

        if value < root.value:
            root.left = self.delete(root.left, value)
        elif value > root.value:
            root.right = self.delete(root.right, value)
        else:
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp

            temp = self.min_value_node(root.right)
            root.value = temp.value
            root.right = self.delete(root.right, temp.value)

        if not root:
            return root

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)

        # here is rebalancing (if tree is broken after deleting node):
        # Left rotation of node
        if balance > 1 and self.balance(root.left) >= 0:
            return self.right_rotate(root)

        # Right rotation of node
        if balance < -1 and self.balance(root.right) <= 0:
            return self.left_rotate(root)

        # Left-Right rotation of node
        if balance > 1 and self.balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right-Left rotation of node
        if balance < -1 and self.balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        # rotating in left
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def right_rotate(self, z):
        # rotating in right
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    # min value
    def min_value_node(self, root):
        current = root
        while current.left:
            current = current.left
        return current

    def search(self, root, value):
        if not root or root.value == value:
            return root
        if root.value < value:
            return self.search(root.right, value)
        return self.search(root.left, value)

    def insert_value(self, value):
        self.root = self.insert(self.root, value)

    def delete_value(self, value):
        self.root = self.delete(self.root, value)

    def search_value(self, value):
        return self.search(self.root, value)


# Example usage:
if __name__ == "__main__":
    tree = AVLTree()
    tree.insert_value(5)
    tree.insert_value(15)
    tree.insert_value(22)
    tree.insert_value(31)
    tree.insert_value(52)
    tree.insert_value(40)
    tree.insert_value(10)

    print("\nTree after insertion:")


    def inorder_traversal(root):
        # In-order traversal to print the tree
        if root:
            inorder_traversal(root.left)
            print(root.value),
            inorder_traversal(root.right)


    inorder_traversal(tree.root)
    print()

    tree.delete_value(22)
    print("Tree after deletion of 22:")
    inorder_traversal(tree.root)
    print()

    result = tree.search_value(5)
    if result:
        print("Node 5 found\n")
    else:
        print("Node 5 not found\n")

    result = tree.search_value(22)
    if result:
        print("Node 22 found\n")
    else:
        print("Node 22 not fouwnd\n")
