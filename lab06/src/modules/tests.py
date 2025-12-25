import unittest
from modules.binary_search_tree import BinTree, BNode
from modules.tree_traversal import *

class TestBinTree(unittest.TestCase):
    """Набор тестов для проверки корректности реализации бинарного дерева поиска."""

    def setUp(self):
        """Инициализация пустого дерева перед каждым тестом."""
        self.tree = BinTree()

    def test_insert_and_find(self):
        """Проверка вставки элементов и их последующего поиска."""
        values = [50, 30, 70, 20, 40, 60, 80]

        for value in values:
            self.tree.add(value)

        for value in values:
            node = self.tree.find(value)
            self.assertIsNotNone(node)
            self.assertEqual(node.value, value)

        self.assertIsNone(self.tree.find(100))
        self.assertIsNone(self.tree.find(10))

    def test_remove(self):
        """Проверка корректности удаления узлов разного типа (листья, узлы с одним или двумя потомками)."""
        values = [50, 30, 70, 20, 40, 60, 80]

        for value in values:
            self.tree.add(value)

        success = self.tree.remove(20)  # удаление листа
        self.assertTrue(success)
        self.assertIsNone(self.tree.find(20))
        self.assertTrue(self.tree.validate_bst())

        success = self.tree.remove(30)  # удаление узла с двумя потомками
        self.assertTrue(success)
        self.assertIsNone(self.tree.find(30))
        self.assertTrue(self.tree.validate_bst())

        success = self.tree.remove(50)  # удаление корня
        self.assertTrue(success)
        self.assertIsNone(self.tree.find(50))
        self.assertTrue(self.tree.validate_bst())

        success = self.tree.remove(100)  # попытка удалить несуществующий элемент
        self.assertFalse(success)

    def test_min_max(self):
        """Проверка поиска минимального и максимального значений в дереве и поддеревьях."""
        values = [50, 30, 70, 20, 40, 60, 80]

        for value in values:
            self.tree.add(value)

        self.assertEqual(self.tree.get_min().value, 20)
        self.assertEqual(self.tree.get_max().value, 80)

        node_30 = self.tree.find(30)
        self.assertEqual(self.tree.get_min(node_30).value, 20)
        self.assertEqual(self.tree.get_max(node_30).value, 40)

    def test_height(self):
        """Проверка вычисления высоты дерева."""
        self.assertEqual(self.tree.compute_height(), -1)  # пустое дерево

        self.tree.add(50)
        self.assertEqual(self.tree.compute_height(), 0)  # один узел

        self.tree.add(30)
        self.tree.add(70)
        self.assertEqual(self.tree.compute_height(), 1)  # корень + 1 уровень

        self.tree.add(20)
        self.tree.add(40)
        self.assertEqual(self.tree.compute_height(), 2)  # три уровня

    def test_validate_bst(self):
        """Проверка корректности валидации структуры BST."""
        values = [50, 30, 70, 20, 40, 60, 80]
        for value in values:
            self.tree.add(value)
        self.assertTrue(self.tree.validate_bst())

        # Намеренное нарушение свойства BST
        self.tree.root = BNode(50)
        self.tree.root.left = BNode(60)  # левый потомок больше корня — ошибка
        self.tree.root.right = BNode(70)
        self.assertFalse(self.tree.validate_bst())

    def test_traversals(self):
        """Проверка различных способов обхода дерева."""
        values = [50, 30, 70, 20, 40, 60, 80]
        sorted_values = sorted(values)

        for value in values:
            self.tree.add(value)

        self.assertEqual(inorder_rec(self.tree.root), sorted_values)
        self.assertEqual(inorder_iter(self.tree.root), sorted_values)

        preorder_result = preorder_rec(self.tree.root)
        self.assertEqual(preorder_result[0], 50)  # корень первый

        postorder_result = postorder_rec(self.tree.root)
        self.assertEqual(postorder_result[-1], 50)  # корень последний

        level_order_vals = level_order(self.tree.root)
        self.assertEqual(len(level_order_vals), len(values))  # все узлы обойдены

    def test_size(self):
        """Проверка корректности подсчёта количества узлов в дереве."""
        self.assertEqual(self.tree.size(), 0)

        values = [50, 30, 70, 20, 40]
        for value in values:
            self.tree.add(value)

        self.assertEqual(self.tree.size(), len(values))

        self.tree.remove(30)
        self.assertEqual(self.tree.size(), len(values) - 1)

if __name__ == "__main__":
    unittest.main()