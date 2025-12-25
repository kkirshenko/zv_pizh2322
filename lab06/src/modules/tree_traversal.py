def inorder_rec(node, result=None):
    """
    Рекурсивный обход дерева в порядке: левое поддерево → узел → правое поддерево.
    Временная сложность: O(n)
    """
    if result is None:
        result = []

    if node:
        inorder_rec(node.left, result)
        result.append(node.value)
        inorder_rec(node.right, result)

    return result

def preorder_rec(node, result=None):
    """
    Рекурсивный обход дерева в порядке: узел → левое поддерево → правое поддерево.
    Временная сложность: O(n)
    """
    if result is None:
        result = []

    if node:
        result.append(node.value)
        preorder_rec(node.left, result)
        preorder_rec(node.right, result)

    return result

def postorder_rec(node, result=None):
    """
    Рекурсивный обход дерева в порядке: левое поддерево → правое поддерево → узел.
    Временная сложность: O(n)
    """
    if result is None:
        result = []

    if node:
        postorder_rec(node.left, result)
        postorder_rec(node.right, result)
        result.append(node.value)

    return result

def inorder_iter(root):
    """
    Итеративная реализация in-order обхода с использованием стека.
    Временная сложность: O(n)
    """
    result = []
    stack = []
    current = root

    while current or stack:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        result.append(current.value)
        current = current.right

    return result

def level_order(root):
    """
    Обход дерева по уровням (BFS) с использованием очереди.
    Временная сложность: O(n)
    """
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        current = queue.pop(0)
        result.append(current.value)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return result