from modules.greedy_algorithms import GreedyMethods, PackSolver, TimeInterval, PackItem
import random

def show_interval_demo():
    """Пример выбора максимального числа непересекающихся интервалов (занятий)."""
    print("=== ПРИМЕР: ВЫБОР НЕПЕРЕСЕКАЮЩИХСЯ ЗАНЯТИЙ ===\n")

    # Расписание семинаров
    seminars = [
        TimeInterval(8, 9, "Алгебра"),
        TimeInterval(8, 10, "Физ-лаборатория"),
        TimeInterval(9, 11, "Геометрия"),
        TimeInterval(10, 12, "Биохимия"),
        TimeInterval(11, 13, "Программирование"),
        TimeInterval(12, 14, "Литература"),
    ]

    print("Доступные занятия:")
    for s in seminars:
        print(f"  {s.name}: {s.start}:00–{s.end}:00")

    chosen = GreedyMethods.schedule_intervals(seminars)

    print("\nВыбранные занятия (максимум без пересечений):")
    for s in chosen:
        print(f"  {s.name}: {s.start}:00–{s.end}:00")

    print(f"\nИз {len(seminars)} вариантов выбрано {len(chosen)}")

def show_fractional_pack():
    """Пример решения задачи о дробном (непрерывном) рюкзаке."""
    print("\n=== ПРИМЕР: ДРОБНЫЙ РЮКЗАК ===\n")

    supplies = [
        PackItem(320, 3, "Колбаса"),
        PackItem(210, 2, "Сырок"),
        PackItem(160, 1, "Булка"),
        PackItem(390, 5, "Консервы"),
    ]
    capacity = 6

    print("Доступные продукты:")
    for p in supplies:
        unit = p.value / p.weight
        print(f"  {p.name}: ценность={p.value}, вес={p.weight}, удельная ценность={unit:.1f}")

    total, sel = GreedyMethods.fractional_pack(capacity, supplies)

    print(f"\nЁмкость рюкзака: {capacity} кг")
    print(f"Максимальная суммарная ценность: {total:.2f}")
    print("Отобрано:")
    for it, frac in sel:
        amount = it.weight * frac
        cost = it.value * frac
        print(f"  {it.name}: {amount:.1f} кг на сумму {cost:.1f} руб ({frac:.1%} от упаковки)")

def show_huffman_demo():
    """Пример построения оптимального префиксного кода по Хаффману."""
    print("\n=== ПРИМЕР: КОД ХАФФМАНА ===\n")

    text = "zzzzzzzzzyyyyyxxwww"

    print(f"Исходная строка: '{text}'")
    from collections import Counter
    freq = Counter(text)
    print("Частота символов:")
    for ch, cnt in sorted(freq.items()):
        print(f"  '{ch}': {cnt} вхождений")

    codes, encoded, tree = GreedyMethods.huffman_encode(text)

    print("\nСгенерированные коды:")
    for ch, code in sorted(codes.items()):
        print(f"  '{ch}': {code}")

    print(f"\nЗакодированная строка: {encoded}")
    print(f"Длина в ASCII: {len(text) * 8} бит")
    print(f"Длина сжатия по Хаффману: {len(encoded)} бит")
    print(f"Экономия: {len(text) * 8 - len(encoded)} бит")

def show_coin_demo():
    """Пример выдачи сдачи жадным методом в разных системах монет."""
    print("\n=== ПРИМЕР: ЖАДНАЯ ВЫДАЧА СДАЧИ ===\n")

    systems = {
        "Американская": [25, 10, 5, 1],
        "Европейская": [50, 20, 10, 5, 2, 1],
        "Нестандартная": [25, 10, 1]
    }

    amounts = [68, 95, 43]

    for name, coins in systems.items():
        print(f"\nСистема монет: {name} -> {coins}")
        for amt in amounts:
            try:
                res = GreedyMethods.make_change(amt, coins)
                total_coins = sum(res.values())
                print(f"  Сумма {amt}: {res} (всего монет: {total_coins})")
            except ValueError as e:
                print(f"  Сумма {amt}: {e}")

def show_prim_demo():
    """Пример построения минимального остовного дерева алгоритмом Прима."""
    print("\n=== ПРИМЕР: АЛГОРИТМ ПРИМА ===\n")

    cities = ['Москва', 'Питер', 'Казань', 'Н.Новгород', 'Екат']
    roads = [
        ('Москва', 'Питер', 700),
        ('Москва', 'Казань', 820),
        ('Москва', 'Н.Новгород', 410),
        ('Питер', 'Казань', 1190),
        ('Питер', 'Екат', 1990),
        ('Казань', 'Н.Новгород', 390),
        ('Казань', 'Екат', 910),
        ('Н.Новгород', 'Екат', 1210),
    ]

    print("Дороги между городами:")
    for u, v, w in roads:
        print(f"  {u} — {v}: {w} км")

    mst = GreedyMethods.prim_mst(cities, roads)

    print("\nМинимальная дорожная сеть (MST):")
    total = 0
    for e in mst:
        print(f"  {e.u} — {e.v}: {e.weight} км")
        total += e.weight

    print(f"Общая протяжённость: {total} км")

def show_knapsack_comparison():
    """Сравнение жадного и оптимального подходов для дискретного рюкзака."""
    print("\n=== ПРИМЕР: ЖАДНЫЙ МЕТОД В 0-1 РЮКЗАКЕ (НЕОПТИМАЛЬНО) ===\n")

    items = [
        PackItem(31, 10, "Золото"),
        PackItem(21, 10, "Серебро"),
        PackItem(21, 10, "Бронза"),
    ]
    cap = 20

    print("Набор предметов:")
    for it in items:
        unit = it.value / it.weight
        print(f"  {it.name}: ценность={it.value}, вес={it.weight}, удельная={unit:.1f}")

    PackSolver.compare_pack_methods(cap, items)

if __name__ == "__main__":
    random.seed(42)

    show_interval_demo()
    show_fractional_pack()
    show_huffman_demo()
    show_coin_demo()
    show_prim_demo()
    show_knapsack_comparison()