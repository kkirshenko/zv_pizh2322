from modules.binary_search_tree import BinTree
from modules.tree_traversal import *
from modules.analysis import build_balanced_tree, build_degenerate_tree

def demo_tree_operations():
    print("=== ДЕМОНСТРАЦИЯ BST ===\n")

    tree = BinTree()

    
    values = [55, 28, 72, 18, 33, 63, 88, 12, 24, 37, 47]  # Добавление узлов в дерево
    print(f"Добавляем узлы: {values}")

    for value in values:
        tree.add(value)

    print("\nСтруктура дерева:")
    print(tree._render())

    
    print(f"Количество узлов: {tree.size()}")  # Проверка основных характеристик
    print(f"Высота дерева: {tree.compute_height()}")
    print(f"Минимальный элемент: {tree.get_min().value}")
    print(f"Максимальный элемент: {tree.get_max().value}")
    print(f"Дерево соответствует свойствам BST: {tree.validate_bst()}")

    
    print(f"\nIn-order (рекурсивно): {inorder_rec(tree.root)}")  # Разные способы обхода
    print(f"In-order (итеративно): {inorder_iter(tree.root)}")
    print(f"Pre-order: {preorder_rec(tree.root)}")
    print(f"Post-order: {postorder_rec(tree.root)}")
    print(f"Level-order (по уровням): {level_order(tree.root)}")

    
    search_values = [37, 58, 18]  # Поиск элементов
    for value in search_values:
        result = tree.find(value)
        if result:
            print(f"Элемент {value} найден")
        else:
            print(f"Элемент {value} отсутствует")

 
    delete_values = [18, 28, 55]     # Удаление узлов
    for value in delete_values:
        print(f"\nУдаляем узел {value}")
        success = tree.remove(value)
        if success:
            print(f"Узел успешно удалён")
            print(f"In-order после удаления: {inorder_rec(tree.root)}")
            print(f"Дерево остаётся корректным BST: {tree.validate_bst()}")
            print(f"Текущее количество узлов: {tree.size()}")
        else:
            print(f"Узел {value} не найден для удаления")

def demo_tree_comparison():
    print("\n\n=== СРАВНЕНИЕ СБАЛАНСИРОВАННОГО И ВЫРОЖДЕННОГО ДЕРЕВЬЕВ ===\n")

    size = 15

    # Сбалансированное дерево
    balanced_tree, values_used = build_balanced_tree(size)
    print("Сбалансированное дерево (на основе случайных значений):")
    print(balanced_tree._render())
    print(f"Высота: {balanced_tree.compute_height()}")
    print(f"Количество узлов: {balanced_tree.size()}")

    # Вырожденное дерево
    degenerate_tree, values_used = build_degenerate_tree(size)
    print("\nВырожденное дерево (построенное из отсортированного списка):")
    print(degenerate_tree._render())
    print(f"Высота: {degenerate_tree.compute_height()}")
    print(f"Количество узлов: {degenerate_tree.size()}")

if __name__ == "__main__":
    demo_tree_operations()
    demo_tree_comparison()