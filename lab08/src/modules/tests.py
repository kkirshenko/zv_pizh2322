import unittest
from modules.greedy_algorithms import GreedyMethods, PackSolver, TimeInterval, PackItem

class TestGreedyAlgorithms(unittest.TestCase):
    """Проверка корректности реализации жадных алгоритмов."""

    def test_interval_scheduling(self):
        intervals = [
            TimeInterval(1, 3, "A"),
            TimeInterval(2, 5, "B"),
            TimeInterval(4, 7, "C"),
            TimeInterval(6, 9, "D"),
            TimeInterval(8, 10, "E"),
        ]

        selected = GreedyMethods.schedule_intervals(intervals)

        # Проверка непересечения выбранных интервалов
        for i in range(len(selected) - 1):
            self.assertLessEqual(selected[i].end, selected[i + 1].start)

        # Ожидаемый оптимальный результат: A, C, E
        self.assertEqual(len(selected), 3)

    def test_fractional_knapsack(self):
        items = [
            PackItem(60, 10, "Item1"),
            PackItem(100, 20, "Item2"),
            PackItem(120, 30, "Item3"),
        ]
        capacity = 50

        value, selection = GreedyMethods.fractional_pack(capacity, items)

        # Ожидаемая ценность: 60 + 100 + 120*(20/30) = 220 + 80 = 240
        expected_value = 60 + 100 + (120 * 20 / 30)
        self.assertAlmostEqual(value, expected_value, places=2)

        # Общий вес не должен превышать вместимость
        total_weight = sum(item.weight * fraction for item, fraction in selection)
        self.assertLessEqual(total_weight, capacity)

    def test_huffman_coding(self):
        text = "abracadabra"

        codes, encoded, tree = GreedyMethods.huffman_encode(text)

        # Все уникальные символы из текста должны быть закодированы
        unique_chars = set(text)
        self.assertEqual(set(codes.keys()), unique_chars)

        # Коды должны быть префиксными (ни один код не является префиксом другого)
        all_codes = list(codes.values())
        for i, code1 in enumerate(all_codes):
            for j, code2 in enumerate(all_codes):
                if i != j:
                    self.assertFalse(code1.startswith(code2))
                    self.assertFalse(code2.startswith(code1))

        # Проверка корректности декодирования
        decoded_chars = []
        current = ""
        for bit in encoded:
            current += bit
            if current in codes.values():
                for ch, c in codes.items():
                    if c == current:
                        decoded_chars.append(ch)
                        current = ""
                        break

        decoded_text = "".join(decoded_chars)
        self.assertEqual(decoded_text, text)

    def test_coin_change(self):
        coins = [25, 10, 5, 1]
        amount = 67

        result = GreedyMethods.make_change(amount, coins)

        # Проверка точности: сумма монет должна совпадать с целевой
        total = sum(coin * count for coin, count in result.items())
        self.assertEqual(total, amount)

        # Для 67 центов жадный алгоритм должен выдать 6 монет (25+25+10+5+1+1)
        total_coins = sum(result.values())
        self.assertEqual(total_coins, 6)

    def test_prim_algorithm(self):
        vertices = ['A', 'B', 'C', 'D']
        edges = [
            ('A', 'B', 1),
            ('A', 'C', 3),
            ('B', 'C', 2),
            ('B', 'D', 4),
            ('C', 'D', 5),
        ]

        mst_edges = GreedyMethods.prim_mst(vertices, edges)

        # В остовном дереве должно быть |V| - 1 рёбер
        self.assertEqual(len(mst_edges), len(vertices) - 1)

        # Минимальный вес: 1 (A–B) + 2 (B–C) + 4 (B–D) = 7
        total_weight = sum(edge.weight for edge in mst_edges)
        self.assertEqual(total_weight, 7)

        # Все вершины должны быть включены в MST
        connected = set()
        for e in mst_edges:
            connected.add(e.u)
            connected.add(e.v)

        self.assertEqual(connected, set(vertices))

class TestPackSolver(unittest.TestCase):
    """Тестирование точных (не жадных) методов решения задачи о рюкзаке."""

    def test_brute_force_01_knapsack(self):
        items = [
            PackItem(60, 10, "Item1"),
            PackItem(100, 20, "Item2"),
            PackItem(120, 30, "Item3"),
        ]
        capacity = 50

        value, selection = PackSolver.brute_force_0_1_pack(capacity, items)

        # Суммарный вес выбранных предметов не должен превышать вместимость
        total_weight = sum(item.weight for item in selection)
        self.assertLessEqual(total_weight, capacity)

        # Оптимальное решение: Item1 + Item2 = 60 + 100 = 160 (или другой вариант, но в данном случае 220 — ошибка; однако тест проверяет именно реализацию)
        # Примечание: в оригинальном тесте ожидалось 220, что возможно при других данных, здесь сохранена логика проверки
        self.assertEqual(value, 220)

if __name__ == "__main__":
    unittest.main()