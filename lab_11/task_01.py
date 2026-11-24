class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        return Node(value)

    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    return root


def inorder_traversal(root):
    if root is None:
        return

    # Узел ждёт своей очереди, пока мы не обойдём всё его левое поддерево.
    yield from inorder_traversal(root.left)
    yield root.value
    yield from inorder_traversal(root.right)


if __name__ == "__main__":
    numbers = map(int, input("Введите целые числа через пробел: ").split())

    root = None
    for number in numbers:
        root = insert(root, number)

    if root is None:
        print("Дерево пустое.")
    else:
        print("Симметричный обход:", *inorder_traversal(root))
