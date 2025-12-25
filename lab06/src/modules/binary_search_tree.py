class BNode:
    """Элемент (узел) бинарного дерева поиска."""

    def __init__(self, value):
        """
        Создание нового узла.
        Временная сложность: O(1)
        """
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f"BNode({self.value})"

class BinTree:
    """Реализация бинарного дерева поиска (BST)."""

    def __init__(self):
        """Инициализация пустого дерева."""
        self.root = None

    def add(self, value):
        """
        Добавление значения в дерево.
        Средняя сложность: O(log n), худшая (при вырождении): O(n)
        """
        if self.root is None:
            self.root = BNode(value)
        else:
            self._add_rec(self.root, value)

    def _add_rec(self, node, value):
        """
        Рекурсивное добавление значения в поддерево.
        Сложность совпадает с методом add.
        """
        if value < node.value:
            if node.left is None:
                node.left = BNode(value)
            else:
                self._add_rec(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = BNode(value)
            else:
                self._add_rec(node.right, value)
        # Повторяющиеся значения игнорируются

    def find(self, value):
        """
        Поиск узла по заданному значению.
        Средняя сложность: O(log n), худшая: O(n)
        """
        return self._find_rec(self.root, value)

    def _find_rec(self, node, value):
        """
        Рекурсивный поиск узла в поддереве.
        """
        if node is None or node.value == value:
            return node

        if value < node.value:
            return self._find_rec(node.left, value)
        else:
            return self._find_rec(node.right, value)

    def remove(self, value):
        """
        Удаление значения из дерева.
        Средняя сложность: O(log n), худшая: O(n)
        """
        if self.root is None:
            return False

        if self.find(value) is None:
            return False

        self.root = self._remove_rec(self.root, value)
        return True

    def _remove_rec(self, node, value):
        """
        Рекурсивное удаление узла из поддерева.
        """
        if node is None:
            return node

        if value < node.value:
            node.left = self._remove_rec(node.left, value)
        elif value > node.value:
            node.right = self._remove_rec(node.right, value)
        else:
            # Узел найден
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            min