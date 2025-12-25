from modules.heap import SmallHeap, LargeHeap
from modules.heapsort import heapsort_using_smallheap, heapsort_using_largeheap, inplace_heapsort
from modules.priority_queue import TaskQueue
import random

def demonstrate_heap_operations():
    """Пример базовых операций с min-кучей (SmallHeap)."""
    print("=== ДЕМОНСТРАЦИЯ ОСНОВНЫХ ОПЕРАЦИЙ С SmallHeap ===\n")

    heap = SmallHeap()
    values = [10, 4, 1, 8, 2, 9, 5, 7, 3]

    print(f"Исходные данные: {values}")

    print("\nПошаговая вставка элементов:")
    for value in values:
        heap.push(value)
        print(f"После добавления {value}: {heap}")

    print(f"\nСтруктура кучи:")
    print(heap.render())

    print(f"Минимальный элемент (корень): {heap.top()}")
    print(f"Куча корректна: {heap.validate_heap()}")

    print("\nИзвлечение элементов в порядке возрастания:")
    extracted = []
    while len(heap) > 0:
        value = heap.pop()
        extracted.append(value)
        print(f"Извлечено {value}; остаток: {heap}")

    print(f"Результат извлечения: {extracted}")
    print(f"Ожидаемый результат: {sorted(values)}")

def demonstrate_heap_construction():
    """Построение кучи из готового массива с помощью heapify."""
    print("\n\n=== ПОСТРОЕНИЕ КУЧИ ИЗ МАССИВА ===\n")

    array = [11, 6, 2, 9, 3, 10, 4]
    print(f"Исходный массив: {array}")

    heap = SmallHeap(array)
    print(f"Куча после heapify: {heap}")
    print(f"Проверка корректности: {heap.validate_heap()}")

    print("\nТекстовое представление:")
    print(heap.render())

def demonstrate_max_heap():
    """Пример работы max-кучи (LargeHeap)."""
    print("\n\n=== ДЕМОНСТРАЦИЯ LargeHeap (max-куча) ===\n")

    array = [11, 6, 2, 9, 3, 10, 4]
    heap = LargeHeap(array)

    print(f"Исходный массив: {array}")
    print(f"LargeHeap: {heap}")
    print(f"Максимальный элемент: {heap.top()}")
    print(f"Корректность структуры: {heap.validate_heap()}")

    print("\nВизуализация дерева:")
    print(heap.render())

    print("\nИзвлечение в порядке убывания:")
    extracted = []
    while len(heap) > 0:
        extracted.append(heap.pop())

    print(f"Результат: {extracted}")

def demonstrate_heapsort():
    """Демонстрация пирамидальной сортировки."""
    print("\n\n=== ПИРАМИДАЛЬНАЯ СОРТИРОВКА (HEAPSORT) ===\n")

    array = [10, 4, 1, 8, 2, 9, 5, 7, 3]
    print(f"Неотсортированный массив: {array}")

    sorted_array = inplace_heapsort(array[:])
    print(f"Отсортировано на месте: {sorted_array}")

    print(f"Совпадает с встроенной сортировкой: {sorted_array == sorted(array)}")

def demonstrate_priority_queue():
    """Пример использования кучи как приоритетной очереди."""
    print("\n\n=== ПРИОРИТЕТНАЯ ОЧЕРЕДЬ ЗАДАЧ ===\n")

    pq = TaskQueue()

    tasks = [
        ("Обычное", 2),
        ("Срочно", 1),
        ("Очень срочно", 0),
        ("Менее срочно", 3),
    ]

    print("Добавление задач:")
    for value, priority in tasks:
        pq.push_with_priority(value, priority)
        print(f"Добавлена задача: '{value}' с приоритетом {priority}")

    print(f"\nТекущее состояние очереди: {pq}")
    print(f"Следующая задача: {pq.peek_priority()}")

    print("\nОбработка задач по приоритету:")
    while not pq.empty():
        task = pq.pop_priority()
        print(f"Выполнена: {task}")

def demonstrate_large_example():
    """Пример работы с более крупным набором данных."""
    print("\n\n=== ДЕМОНСТРАЦИЯ НА РАСШИРЕННОМ НАБОРЕ ===\n")

    size = 20
    large_array = random.sample(range(100), size)

    print(f"Случайный массив ({size} эл.): {large_array[:10]}...")

    heap = SmallHeap(large_array)
    sorted_elements = []

    for i in range(min(5, size)):
        sorted_elements.append(heap.pop())

    print(f"Первые 5 минимальных: {sorted_elements}")
    print(f"Осталось в куче: {len(heap)}")

if __name__ == "__main__":
    random.seed(42)

    demonstrate_heap_operations()
    demonstrate_heap_construction()
    demonstrate_max_heap()
    demonstrate_heapsort()
    demonstrate_priority_queue()
    demonstrate_large_example()