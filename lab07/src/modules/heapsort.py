from modules.heap import SmallHeap, LargeHeap

def heapsort_using_smallheap(array):
    """
    Сортировка с использованием min-кучи: извлекаем минимальные элементы по очереди.
    
    Временная сложность: O(n log n)
    """
    heap = SmallHeap(array)
    sorted_array = []
    while len(heap) > 0:
        sorted_array.append(heap.pop())
    return sorted_array


def heapsort_using_largeheap(array):
    """
    Сортировка с использованием max-кучи: извлекаем максимальные элементы и записываем их с конца массива.
    
    Временная сложность: O(n log n)
    """
    heap = LargeHeap(array)
    sorted_array = [0] * len(array)
    for i in range(len(array) - 1, -1, -1):
        sorted_array[i] = heap.pop()
    return sorted_array


def inplace_heapsort(array):
    """
    Пирамидальная сортировка на месте (без дополнительной памяти).
    
    Временная сложность: O(n log n), 
    Дополнительная память: O(1)
    """

    def _sink(arr, start, end):
        root = start
        while 2 * root + 1 <= end:
            child = 2 * root + 1
            swap = root

            if arr[swap] < arr[child]:
                swap = child

            if child + 1 <= end and arr[swap] < arr[child + 1]:
                swap = child + 1

            if swap == root:
                return
            else:
                arr[root], arr[swap] = arr[swap], arr[root]
                root = swap

    n = len(array)
    if n <= 1:
        return array

    # Построение max-кучи из исходного массива
    for i in range(n // 2 - 1, -1, -1):
        _sink(array, i, n - 1)

    # Последовательное извлечение максимумов в конец массива
    for i in range(n - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        _sink(array, 0, i - 1)

    return array


heapsort = inplace_heapsort