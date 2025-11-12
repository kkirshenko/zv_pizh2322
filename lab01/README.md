# Лабораторная работа 1

## Анализ сложности алгоритмов 

Выполнил:

Студент: Зволибовская Екатерина Валерьевна

Группа: ПИЖ-б-о-23-2(2)

Цель работы: Освоить понятие вычислительной сложности алгоритма. Получить практические навыки реализации и анализа линейного и бинарного поиска. Научиться экспериментально подтверждать теоретические оценки сложности O(n) и O(log n).

Задание:
1. Реализовать функцию линейного поиска элемента в массиве.
2. Реализовать функцию бинарного поиска элемента в отсортированном массиве.
3. Провести теоретический анализ сложности обоих алгоритмов.
4. Экспериментально сравнить время выполнения алгоритмов на массивах разного размера.
5. Визуализировать результаты, подтвердив асимптотику O(n) и O(log n).

```PYTHON
# Импорт необходимых библиотек
import time
import random
import matplotlib.pyplot as plt
import math


def linear_search(arr, target):
    """
    Линейный поиск элемента в массиве.
    Возвращает индекс target или -1, если не найден.
    Сложность: O(n), где n - длина массива.
    """
    # O(1) - инициализация индекса
    index = 0
    n = len(arr)
    while index < n:
        if arr[index] == target:
            return index
        index += 1
    # O(1) - возврат -1, если элемент не найден
    return -1
    # Общая сложность: O(n)


def binary_search(arr, target):
    """
    Бинарный поиск элемента в отсортированном массиве.
    Возвращает индекс target или -1, если не найден.
    Сложность: O(log n), где n - длина массива.
    """
    # O(log n) - цикл выполняется log(n) раз, сужая область поиска
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            # O(1) - сужение области поиска влево
            right = mid - 1
        else:
            # O(1) - сужение области поиска вправо
            left = mid + 1
    # O(1) - возврат -1, если элемент не найден
    return -1
    # Общая сложность: O(log n)


def measure_time(search_func, arr, target, number_of_calls=10):
    """
    Замеряет среднее время выполнения функции поиска.
    Возвращает: float - среднее время выполнения (в секундах).
    """
    # O(k * C) - где k - number_of_calls, C - сложность search_func
    start_time = time.perf_counter()
    for _ in range(number_of_calls):
        search_func(arr, target)
    end_time = time.perf_counter()
    # O(1) - вычисление общего затраченного времени
    elapsed_time = end_time - start_time
    # O(1) - вычисление и возврат среднего времени
    avg_time = elapsed_time / number_of_calls
    return avg_time


def run_comparison():
    """
    Основная функция для проведения сравнительного анализа.
    """
    # Определение размеров массивов для тестирования
    sizes = [1000, 2000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000]
    
    # Списки для хранения результатов
    linear_times_best = []
    binary_times_best = []
    linear_times_worst = []
    binary_times_worst = []
    
    # Цикл по каждому размеру массива
    for size in sizes:
        # O(n)
        arr = list(range(size))
        
        # Определение целевых элементов для лучшего и худшего случая
        target_best = arr[size // 2]  # Средний элемент
        target_worst = size + 1       # Элемент, которого нет в массиве
        
        # Измерение времени для линейного поиска (худший случай)
        # O(n) - сложность linear_search
        avg_time_linear_worst = measure_time(linear_search, arr, target_worst)
        linear_times_worst.append(avg_time_linear_worst)
        
        # Измерение времени для бинарного поиска (худший случай)
        # O(log n) - сложность binary_search
        avg_time_binary_worst = measure_time(binary_search, arr, target_worst)
        binary_times_worst.append(avg_time_binary_worst)

        # Измерение времени для линейного поиска (лучший случай - первый элемент)
        # O(1) - сложность, если элемент на первом месте
        avg_time_linear_best = measure_time(linear_search, arr, arr[0])
        linear_times_best.append(avg_time_linear_best)
        
        # Измерение времени для бинарного поиска (лучший случай - средний элемент)
        # O(1) - сложность, если элемент сразу в середине
        avg_time_binary_best = measure_time(binary_search, arr, arr[size//2])
        binary_times_best.append(avg_time_binary_best)

    # Построение графиков
    plt.figure(figsize=(12, 8))

    # График 1: Линейная шкала
    plt.subplot(2, 1, 1)
    plt.plot(sizes, linear_times_worst, 'o-', label='Linear Search (Worst Case O(n))', color='red')
    plt.plot(sizes, binary_times_worst, 's-', label='Binary Search (Worst Case O(log n))', color='blue')
    plt.xlabel('Array Size (n)')
    plt.ylabel('Average Execution Time (seconds)')
    plt.title('Algorithm Comparison: Time vs. Array Size (Linear Scale)')
    plt.legend()
    plt.grid(True)

    # График 2: Логарифмическая шкала по оси Y
    plt.subplot(2, 1, 2)
    plt.plot(sizes, linear_times_worst, 'o-', label='Linear Search O(n)', color='red')
    plt.plot(sizes, binary_times_worst, 's-', label='Binary Search O(log n)', color='blue')
    
    # Создание теоретических кривых для сравнения
    theoretical_log_n = [math.log2(max(n, 1)) * linear_times_worst[0] / max(math.log2(max(sizes[0], 1)), 1) for n in sizes]
    theoretical_n = [n * linear_times_worst[0] / sizes[0] for n in sizes]
    
    plt.loglog(sizes, theoretical_n, ':', label='Theoretical O(n)', color='darkred')
    plt.loglog(sizes, theoretical_log_n, ':', label='Theoretical O(log n)', color='darkblue')

    plt.xlabel('Array Size (n)')
    plt.ylabel('Average Execution Time (seconds)')
    plt.title('Algorithm Comparison: Time vs. Array Size (Log-Log Scale)')
    plt.legend()
    plt.grid(True, which="both", ls="-")

    plt.tight_layout()
    plt.savefig('search_complexity_analysis.png')
    plt.show()


if __name__ == "__main__":
    run_comparison()

# Характеристики ПК для тестирования
pcinf = """
Характеристики ПК для тестирования:
- Процессор: Intel(R) Core(TM) i3-10105 CPU @ 3.70 GHz
- Оперативная память: 16 GB
- ОС: Windows 11
- Python: 3.11 (64-bit)
"""
print(pcinf)
```