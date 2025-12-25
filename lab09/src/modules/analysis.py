import time
import sys
import psutil
import os
from typing import List, Tuple, Dict
import matplotlib.pyplot as plt
from datetime import datetime

from modules.dynamic_programming import (
    FibSeries,
    Knapsack01,
    LCS,
    Levenshtein,
    CoinExchange,
    LIS
)

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
report_dir = os.path.join(base_dir, 'report')

os.makedirs(report_dir, exist_ok=True)

fibonacci_output_path = os.path.join(report_dir, 'fibonacci_comparison.png')
knapsack_output_path = os.path.join(report_dir, 'knapsack_scalability.png')

class PerfWatcher:
    """Инструмент для измерения времени выполнения и потребления памяти."""

    def __init__(self):
        self.process = psutil.Process(os.getpid())
        self.start_time = None
        self.start_memory = None

    def start(self):
        """Начать отслеживание ресурсов."""
        self.start_time = time.perf_counter()
        self.start_memory = self.process.memory_info().rss / 1024 / 1024  # MB

    def stop(self) -> Tuple[float, float]:
        """
        Завершить отслеживание и вернуть затраченное время и прирост памяти.
        Время — в секундах, память — в мегабайтах.
        """
        elapsed_time = time.perf_counter() - self.start_time
        end_memory = self.process.memory_info().rss / 1024 / 1024
        used_memory = end_memory - self.start_memory
        return elapsed_time, max(used_memory, 0)

def compare_fib_methods(max_n: int = 35) -> Dict:
    """
    Сравнение различных методов вычисления чисел Фибоначчи по времени и памяти.
    """
    print("\n" + "="*70)
    print("СРАВНЕНИЕ МЕТОДОВ: ЧИСЛА ФИБОНАЧЧИ")
    print("="*70)
    
    results = {
        'n': [],
        'naive': [],
        'memo': [],
        'iterative': []
    }
    
    for n in range(5, max_n + 1, 2):
        print(f"\nТест для n = {n}:")
        
        if n <= 30:
            monitor = PerfWatcher()
            monitor.start()
            result_naive = FibSeries.naive_recursive(n)
            time_naive, mem_naive = monitor.stop()
            print(f"  Наивная рекурсия: {time_naive:.6f} с, память: {mem_naive:.2f} МБ")
            results['naive'].append(time_naive)
        else:
            print(f"  Наивная рекурсия: пропущена (экспоненциальное время)")
            results['naive'].append(None)
        
        monitor = PerfWatcher()
        monitor.start()
        result_memo = FibSeries.memoized(n)
        time_memo, mem_memo = monitor.stop()
        print(f"  С мемоизацией: {time_memo:.6f} с, память: {mem_memo:.2f} МБ")
        results['memo'].append(time_memo)
        
        monitor = PerfWatcher()
        monitor.start()
        result_iter = FibSeries.bottom_up(n)
        time_iter, mem_iter = monitor.stop()
        print(f"  Восходящий метод: {time_iter:.6f} с, память: {mem_iter:.2f} МБ")
        results['iterative'].append(time_iter)
        
        results['n'].append(n)
        
        assert result_memo == result_iter, f"Разные результаты для n={n}"
        print(f"  Итог: F({n}) = {result_iter}")
    
    return results

def compare_knapsack_dp_vs_greedy():
    """
    Сравнение точного решения 0-1 рюкзака и жадного приближения для дробного случая.
    """
    print("\n" + "="*70)
    print("СРАВНЕНИЕ: ТОЧНОЕ РЕШЕНИЕ VS ЖАДНЫЙ АЛГОРИТМ")
    print("="*70)
    
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 8
    
    print(f"\nНабор предметов: {list(zip(range(len(weights)), weights, values))}")
    print(f"Максимальный вес: {capacity}")
    
    dp_value, dp_items = Knapsack01.compute_with_items(weights, values, capacity)
    dp_weight = sum(weights[i] for i in dp_items)
    
    print(f"\nДинамическое программирование (0-1): ценность={dp_value}, вес={dp_weight}, предметы={dp_items}")
    
    items_by_ratio = sorted(
        enumerate(zip(weights, values)),
        key=lambda x: x[1][1] / x[1][0],
        reverse=True
    )
    
    greedy_value = 0
    greedy_weight = 0
    greedy_items = []
    
    for idx, (w, v) in items_by_ratio:
        if greedy_weight + w <= capacity:
            greedy_items.append(idx)
            greedy_weight += w
            greedy_value += v
    
    print(f"\nЖадный метод (дробный): ценность={greedy_value}, вес={greedy_weight}, предметы={greedy_items}")
    print(f"\nВывод: DP даёт оптимум ({dp_value}), жадный — лишь приближение ({greedy_value})")
    
    print("\n" + "-"*70)
    print("\nПример, где жадный алгоритм не оптимален:")
    
    weights2 = [10, 20, 30]
    values2 = [60, 100, 120]
    capacity2 = 50
    
    print(f"Набор: {list(zip(range(len(weights2)), weights2, values2))}")
    print(f"Вместимость: {capacity2}")
    
    dp_value2, dp_items2 = Knapsack01.compute_with_items(weights2, values2, capacity2)
    dp_weight2 = sum(weights2[i] for i in dp_items2)
    
    print(f"\nDP: ценность={dp_value2}, вес={dp_weight2}, предметы={dp_items2}")
    
    items_by_ratio2 = sorted(
        enumerate(zip(weights2, values2)),
        key=lambda x: x[1][1] / x[1][0],
        reverse=True
    )
    
    greedy_value2 = 0
    greedy_weight2 = 0
    greedy_items2 = []
    
    for idx, (w, v) in items_by_ratio2:
        if greedy_weight2 + w <= capacity2:
            greedy_items2.append(idx)
            greedy_weight2 += w
            greedy_value2 += v
    
    print(f"\nЖадный: ценность={greedy_value2}, вес={greedy_weight2}, предметы={greedy_items2}")

def test_knapsack_scalability():
    """Оценка производительности и потребления памяти при росте размера задачи о рюкзаке."""
    print("\n" + "="*70)
    print("МАСШТАБИРУЕМОСТЬ: ЗАДАЧА О РЮКЗАКЕ 0-1")
    print("="*70)
    
    results = {
        'n_items': [],
        'capacity': [],
        'time_full': [],
        'time_optimized': [],
        'memory_full': [],
        'memory_optimized': []
    }
    
    test_cases = [
        (10, 50),
        (20, 100),
        (30, 150),
        (40, 200),
        (50, 250),
        (75, 375),
        (100, 500),
    ]
    
    for n_items, capacity in test_cases:
        print(f"\nТест: кол-во предметов={n_items}, вместимость={capacity}")
        
        import random
        random.seed(42)
        weights = [random.randint(5, 50) for _ in range(n_items)]
        values = [random.randint(10, 100) for _ in range(n_items)]
        
        monitor = PerfWatcher()
        monitor.start()
        result_full = Knapsack01.compute(weights, values, capacity)
        time_full, mem_full = monitor.stop()
        print(f"  Полный DP: {time_full:.6f} с, память: {mem_full:.2f} МБ")
        
        monitor = PerfWatcher()
        monitor.start()
        result_opt = Knapsack01.compute_optimized(weights, values, capacity)
        time_opt, mem_opt = monitor.stop()
        print(f"  Оптимизированный DP: {time_opt:.6f} с, память: {mem_opt:.2f} МБ")
        
        assert result_full == result_opt, f"Результаты не совпадают при n_items={n_items}!"
        print(f"  Ответ: {result_full}")
        
        results['n_items'].append(n_items)
        results['capacity'].append(capacity)
        results['time_full'].append(time_full)
        results['time_optimized'].append(time_opt)
        results['memory_full'].append(mem_full)
        results['memory_optimized'].append(mem_opt)
    
    return results

def test_levenshtein_opt():
    """Сравнение полного и память-оптимизированного вариантов вычисления расстояния Левенштейна."""
    print("\n" + "="*70)
    print("СРАВНЕНИЕ МЕТОДОВ: РАССТОЯНИЕ ЛЕВЕНШТЕЙНА")
    print("="*70)
    
    test_strings = [
        ("kitten", "sitting"),
        ("saturday", "sunday"),
        ("abc", "def"),
        ("pneumonoultramicroscopicsilicovolcanoconiosis", "pneumonoultramicroscopicsilicovoxalternateconiosis"),
    ]
    
    results = {
        'strings': [],
        'full': [],
        'optimized': []
    }
    
    for s1, s2 in test_strings:
        print(f"\nПара строк: '{s1}' и '{s2}':")
        
        monitor = PerfWatcher()
        monitor.start()
        dist_full = Levenshtein.compute_distance(s1, s2)
        time_full, mem_full = monitor.stop()
        print(f"  Полный DP: расстояние={dist_full}, время={time_full:.6f} с, память={mem_full:.2f} МБ")
        
        monitor = PerfWatcher()
        monitor.start()
        dist_opt = Levenshtein.compute_distance_optimized(s1, s2)
        time_opt, mem_opt = monitor.stop()
        print(f"  Оптимизированный: расстояние={dist_opt}, время={time_opt:.6f} с, память={mem_opt:.2f} МБ")
        
        assert dist_full == dist_opt, "Разные результаты!"
        
        results['strings'].append(f"'{s1[:10]}...'-'{s2[:10]}...'")
        results['full'].append(time_full)
        results['optimized'].append(time_opt)
    
    return results

def test_real_tasks():
    """Проверка корректности на типовых задачах динамического программирования."""
    print("\n" + "="*70)
    print("ПРАКТИЧЕСКИЕ ЗАДАЧИ: КОРРЕКТНОСТЬ И РЕЗУЛЬТАТЫ")
    print("="*70)
    
    print("\n1) РАЗМЕН МОНЕТ")
    coins = [1, 2, 5, 10]
    amount = 27
    
    min_count, used_coins = CoinExchange.min_coins_with_change(coins, amount)
    print(f"Номиналы: {coins}, сумма: {amount}")
    print(f"Мин. количество монет: {min_count}, выбранные монеты: {used_coins}")
    print(f"Проверка: сумма монет = {sum(used_coins)}")
    
    combinations = CoinExchange.count_ways(coins, amount)
    print(f"Число способов размена: {combinations}")
    
    print("\n2) САМАЯ ДЛИННАЯ ВОЗРАСТАЮЩАЯ ПОДПОСЛЕДОВАТЕЛЬНОСТЬ (LIS)")
    test_arrays = [
        [11, 9, 2, 5, 3, 7, 101, 18],
        [0, 1, 0, 4, 4, 4, 3, 6, 1],
        [1, 3, 6, 7, 9, 4, 10, 5, 5],
    ]
    
    for arr in test_arrays:
        lis = LIS.reconstruct(arr)
        length = LIS.lis_length(arr)
        length_opt = LIS.length_optimized(arr)
        
        print(f"\nМассив: {arr}")
        print(f"Найденная LIS: {lis} (длина = {length})")
        print(f"Длина (O(n log n)): {length_opt}")
        assert length == length_opt, "Несовпадение длин!"
    
    print("\n3) НАИБОЛЬШАЯ ОБЩАЯ ПОДПОСЛЕДОВАТЕЛЬНОСТЬ (LCS)")
    pairs = [
        ("abcde", "ace"),
        ("oxcpqrsvwf", "sxyspmqo"),
        ("AGGTAB", "GXTXAYB"),
    ]
    
    for s1, s2 in pairs:
        lcs = LCS.lcs_find(s1, s2)
        length = LCS.lcs_length(s1, s2)
        print(f"\nСтроки: '{s1}' и '{s2}'")
        print(f"LCS: '{lcs}' (длина = {length})")

def visualize_tables():
    """Вывод DP-таблиц для наглядного понимания работы алгоритмов."""
    print("\n" + "="*70)
    print("ВИЗУАЛИЗАЦИЯ DP-ТАБЛИЦ")
    print("="*70)
    
    print("\n1) Таблица LCS")
    text1, text2 = "AGGTAB", "GXTXAYB"
    
    table = LCS.get_matrix(text1, text2)
    print(f"\nСтроки: '{text1}' и '{text2}'")
    print("\nDP-таблица:")
    print(f"      {'':>3}", end="")
    for j, c in enumerate(text2):
        print(f"{c:>3}", end="")
    print()
    
    for i, c in enumerate(text1):
        print(f"{c:>3}:", end="")
        for j in range(len(text2) + 1):
            print(f"{table[i][j]:>3}", end="")
        print()
    
    print("\n2) Таблица расстояния Левенштейна")
    word1, word2 = "kitten", "sitting"
    
    table = Levenshtein.get_matrix(word1, word2)
    print(f"\nСлова: '{word1}' и '{word2}'")
    print("\nDP-таблица:")
    print(f"      {'':>3}", end="")
    for j, c in enumerate(word2):
        print(f"{c:>3}", end="")
    print()
    
    for i, c in enumerate(word1):
        print(f"{c:>3}:", end="")
        for j in range(len(word2) + 1):
            print(f"{table[i][j]:>3}", end="")
        print()

def plot_fib(results: Dict):
    """Построение графика производительности методов вычисления Фибоначчи."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    ax = axes[0]
    ax.plot(results['n'], results['memo'], 'o-', label='Мемоизация', linewidth=2)
    ax.plot(results['n'], results['iterative'], 's-', label='Восходящий', linewidth=2)
    
    naive_data = [(n, t) for n, t in zip(results['n'], results['naive']) if t is not None]
    if naive_data:
        ns, ts = zip(*naive_data)
        ax.plot(ns, ts, '^-', label='Наивная рекурсия', linewidth=2)
    
    ax.set_xlabel('n', fontsize=12)
    ax.set_ylabel('Время (с)', fontsize=12)
    ax.set_title('Производительность методов Фибоначчи', fontsize=12, fontweight='bold')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_yscale('log')
    
    ax = axes[1]
    ax.text(0.5, 0.5, 'Измерения памяти проводились через мониторинг процесса\n(данные представлены в консоли)', 
            ha='center', va='center', transform=ax.transAxes, fontsize=11)
    ax.set_title('Анализ потребления памяти', fontsize=12, fontweight='bold')
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig(fibonacci_output_path, dpi=300, bbox_inches='tight')
    print("\nГрафик сохранён: fibonacci_comparison.png")
    plt.close()

def plot_knapsack(results: Dict):
    """Построение графиков времени и памяти для задачи о рюкзаке."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    ax = axes[0]
    x = range(len(results['n_items']))
    width = 0.35
    ax.bar([i - width/2 for i in x], results['time_full'], width, label='Полный DP O(n·W)', alpha=0.8)
    ax.bar([i + width/2 for i in x], results['time_optimized'], width, label='Опт. DP O(W)', alpha=0.8)
    
    ax.set_xlabel('Размер задачи (n, W)', fontsize=12)
    ax.set_ylabel('Время (с)', fontsize=12)
    ax.set_title('Масштабируемость: время выполнения', fontsize=12, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels([f"{n},{w}" for n, w in zip(results['n_items'], results['capacity'])], rotation=45)
    ax.legend()
    ax.grid(True, alpha=0.3, axis='y')
    
    ax = axes[1]
    ax.bar([i - width/2 for i in x], results['memory_full'], width, label='Полный DP', alpha=0.8)
    ax.bar([i + width/2 for i in x], results['memory_optimized'], width, label='Оптимизированный DP', alpha=0.8)
    
    ax.set_xlabel('Размер задачи (n, W)', fontsize=12)
    ax.set_ylabel('Память (МБ)', fontsize=12)
    ax.set_title('Масштабируемость: потребление памяти', fontsize=12, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels([f"{n},{w}" for n, w in zip(results['n_items'], results['capacity'])], rotation=45)
    ax.legend()
    ax.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.savefig(knapsack_output_path, dpi=300, bbox_inches='tight')
    print("График сохранён: knapsack_scalability.png")
    plt.close()

def main():
    """Основная точка входа для выполнения всех тестов и генерации отчётов."""
    print("=" * 70)
    print("КОМПЛЕКСНЫЙ АНАЛИЗ: ДИНАМИЧЕСКОЕ ПРОГРАММИРОВАНИЕ")
    print("=" * 70)
    print(f"Дата выполнения: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    fib_results = compare_fib_methods()
    compare_knapsack_dp_vs_greedy()
    knapsack_results = test_knapsack_scalability()
    edit_results = test_levenshtein_opt()
    test_real_tasks()
    visualize_tables()
    
    try:
        plot_fib(fib_results)
        plot_knapsack(knapsack_results)
    except Exception as e:
        print(f"\nНе удалось построить графики: {e}")
    
    print("\n" + "="*70)
    print("АНАЛИЗ УСПЕШНО ЗАВЕРШЁН")
    print("="*70)

if __name__ == "__main__":
    main()