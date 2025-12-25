import unittest
from typing import List
from modules.dynamic_programming import (
    FibSeries,
    Knapsack01,
    LCS,
    Levenshtein,
    CoinExchange,
    LIS,
    pretty_print_table
)

def demo_fib():
    """Демонстрация различных методов вычисления чисел Фибоначчи."""
    print("\n" + "="*70)
    print("ПРИМЕР 1: ЧИСЛА ФИБОНАЧЧИ")
    print("="*70)
    
    n = 10
    print(f"\nВычисление F({n}):")
    
    # Наивная рекурсия
    result_naive = FibSeries.naive_recursive(n)
    print(f"1) Наивная рекурсия: F({n}) = {result_naive}")
    
    # Рекурсия с мемоизацией
    result_memo = FibSeries.memoized(n)
    print(f"2) С кэшированием:   F({n}) = {result_memo}")
    
    # Восходящий табличный метод
    result_tabular = FibSeries.bottom_up(n)
    print(f"3) Табличный метод:  F({n}) = {result_tabular}")
    
    # Оптимизированный по памяти вариант
    result_opt = FibSeries.bottom_up_optimized(n)
    print(f"4) Память-оптим.:    F({n}) = {result_opt}")
    
    print(f"\nПервые 15 чисел Фибоначчи:")
    fibs = [FibSeries.bottom_up(i) for i in range(15)]
    print(fibs)


def demo_knapsack():
    """Решение задачи о рюкзаке 0-1 разными способами."""
    print("\n" + "="*70)
    print("ПРИМЕР 2: ЗАДАЧА О РЮКЗАКЕ 0-1")
    print("="*70)
    
    # Первый набор данных
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 8
    
    print(f"\nВходные данные:")
    print(f"Предметы: {list(zip(range(len(weights)), weights, values))}")
    print(f"Максимальная вместимость: {capacity}")
    
    # Только значение
    max_value = Knapsack01.compute(weights, values, capacity)
    print(f"\nМаксимальная суммарная ценность: {max_value}")
    
    # Со списком выбранных предметов
    max_value, items = Knapsack01.compute_with_items(weights, values, capacity)
    print(f"\nОптимальный набор:")
    print(f"Макс. ценность: {max_value}")
    print(f"Индексы выбранных предметов: {items}")
    print(f"Подробности:")
    total_weight = 0
    total_value = 0
    for i in items:
        print(f"  Предмет {i}: вес={weights[i]}, ценность={values[i]}")
        total_weight += weights[i]
        total_value += values[i]
    print(f"Итого: вес={total_weight}, ценность={total_value}")
    
    # Второй пример
    print("\n" + "-"*70)
    print("\nДругой пример:")
    weights2 = [6, 3, 4, 2]
    values2 = [30, 14, 16, 9]
    capacity2 = 10
    
    print(f"Предметы: {list(zip(range(len(weights2)), weights2, values2))}")
    print(f"Вместимость: {capacity2}")
    
    max_value2, items2 = Knapsack01.compute_with_items(weights2, values2, capacity2)
    print(f"Максимальная ценность: {max_value2}")
    print(f"Выбранные предметы: {items2}")


def demo_lcs():
    """Поиск наибольшей общей подпоследовательности (LCS)."""
    print("\n" + "="*70)
    print("ПРИМЕР 3: НАИБОЛЬШАЯ ОБЩАЯ ПОДПОСЛЕДОВАТЕЛЬНОСТЬ (LCS)")
    print("="*70)
    
    test_cases = [
        ("abcde", "ace"),
        ("AGGTAB", "GXTXAYB"),
        ("greetings", "growing"),
    ]
    
    for text1, text2 in test_cases:
        print(f"\nСтроки: '{text1}' и '{text2}'")
        
        length = LCS.lcs_length(text1, text2)
        print(f"Длина LCS: {length}")
        
        lcs = LCS.lcs_find(text1, text2)
        print(f"Сама LCS: '{lcs}'")


def demo_levenshtein():
    """Вычисление минимального числа операций редактирования."""
    print("\n" + "="*70)
    print("ПРИМЕР 4: РАССТОЯНИЕ РЕДАКТИРОВАНИЯ (ЛЕВЕНШТЕЙНА)")
    print("="*70)
    
    test_cases = [
        ("kitten", "sitting"),
        ("saturday", "sunday"),
        ("", "b"),
        ("b", ""),
    ]
    
    for word1, word2 in test_cases:
        print(f"\nПреобразуем '{word1}' → '{word2}':")
        
        distance = Levenshtein.compute_distance(word1, word2)
        print(f"Минимум операций: {distance}")


def demo_coin_change():
    """Динамическое программирование в задачах с монетами."""
    print("\n" + "="*70)
    print("ПРИМЕР 5: РАЗМЕН МОНЕТ")
    print("="*70)
    
    coins = [1, 2, 5, 10]
    amount = 17
    
    print(f"Доступные номиналы: {coins}")
    print(f"Целевая сумма: {amount}")
    
    # Минимальное число монет
    min_count = CoinExchange.min_coins_count(coins, amount)
    print(f"\nМин. количество монет: {min_count}")
    
    # Конкретный набор монет
    min_count, used_coins = CoinExchange.min_coins_with_change(coins, amount)
    print(f"Использованные монеты: {used_coins}")
    print(f"Проверка: {' + '.join(map(str, used_coins))} = {sum(used_coins)}")
    
    # Число возможных комбинаций
    print(f"\nКоличество способов получить сумму {amount}:")
    combinations = CoinExchange.count_ways(coins, amount)
    print(f"{combinations} вариантов")


def demo_lis():
    """Поиск самой длинной возрастающей подпоследовательности."""
    print("\n" + "="*70)
    print("ПРИМЕР 6: САМАЯ ДЛИННАЯ ВОЗРАСТАЮЩАЯ ПОДПОСЛЕДОВАТЕЛЬНОСТЬ (LIS)")
    print("="*70)
    
    test_arrays = [
        [11, 9, 2, 5, 3, 7, 101, 18],
        [0, 1, 0, 4, 4, 4, 3, 6, 1],
        [6, 5, 4, 3, 2],
    ]
    
    for arr in test_arrays:
        print(f"\nИсходный массив: {arr}")
        
        length = LIS.lis_length(arr)
        print(f"Длина LIS: {length}")
        
        lis = LIS.reconstruct(arr)
        print(f"Сама LIS: {lis}")
        
        length_opt = LIS.length_optimized(arr)
        print(f"Длина (за O(n log n)): {length_opt}")

def main():
    """Запуск всех демонстраций по динамическому программированию."""
    print("\n" + "="*70)
    print("ДЕМОНСТРАЦИИ: ДИНАМИЧЕСКОЕ ПРОГРАММИРОВАНИЕ")
    print("="*70)
    
    demo_fib()
    demo_knapsack()
    demo_lcs()
    demo_levenshtein()
    demo_coin_change()
    demo_lis()

if __name__ == "__main__":
    main()