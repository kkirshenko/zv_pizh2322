import heapq
from collections import Counter, namedtuple
import math

# Структуры данных
TimeInterval = namedtuple('TimeInterval', ['start', 'end', 'name'])
PackItem = namedtuple('PackItem', ['value', 'weight', 'name'])
HNode = namedtuple('HNode', ['char', 'freq', 'left', 'right'])
GraphEdge = namedtuple('GraphEdge', ['u', 'v', 'weight'])

class GreedyMethods:
    """
    Набор реализаций классических жадных алгоритмов.
    """

    @staticmethod
    def schedule_intervals(intervals):
        """
        Поиск наибольшего количества непересекающихся интервалов.
        Сложность: O(n log n) из-за сортировки, далее — линейный проход.
        """
        if not intervals:
            return []

        # Поддержка входных данных как пар (start, end) или как именованных кортежей
        if len(intervals[0]) == 2:
            intervals = [TimeInterval(start, end, f"Task_{i}")
                         for i, (start, end) in enumerate(intervals)]

        intervals_sorted = sorted(intervals, key=lambda x: x.end)

        selected = []
        last_end = -float('inf')

        for inter in intervals_sorted:
            if inter.start >= last_end:
                selected.append(inter)
                last_end = inter.end

        return selected

    @staticmethod
    def fractional_pack(capacity, items):
        """
        Решение задачи о дробном рюкзаке: можно брать доли предметов.
        Сложность: O(n log n) — сортировка по удельной ценности.
        """
        if not items or capacity <= 0:
            return 0, []

        # Приведение к именованным элементам, если переданы кортежи
        if len(items[0]) == 2:
            items = [PackItem(value, weight, f"Item_{i}")
                     for i, (value, weight) in enumerate(items)]

        items_sorted = sorted(items, key=lambda x: x.value / x.weight, reverse=True)

        total_value = 0
        remaining = capacity
        chosen = []

        for it in items_sorted:
            if remaining >= it.weight:
                total_value += it.value
                remaining -= it.weight
                chosen.append((it, 1.0))
            else:
                frac = remaining / it.weight
                total_value += it.value * frac
                chosen.append((it, frac))
                break

        return total_value, chosen

    @staticmethod
    def huffman_encode(text):
        """
        Построение оптимального префиксного кода Хаффмана для заданной строки.
        Сложность: O(n log n) — из-за операций с приоритетной очередью.
        """
        if not text:
            return {}, "", None

        freq = Counter(text)

        # Особый случай: один уникальный символ
        if len(freq) == 1:
            ch = next(iter(freq))
            return {ch: '0'}, '0' * len(text), HNode(ch, freq[ch], None, None)

        heap = []
        for ch, cnt in freq.items():
            heapq.heappush(heap, (cnt, id(ch), HNode(ch, cnt, None, None)))

        while len(heap) > 1:
            f1, id1, n1 = heapq.heappop(heap)
            f2, id2, n2 = heapq.heappop(heap)
            merged = HNode(None, f1 + f2, n1, n2)
            heapq.heappush(heap, (f1 + f2, id(merged), merged))

        _, _, root = heap[0]

        codes = {}
        def build_codes(node, code):
            if node is None:
                return
            if node.char is not None:
                codes[node.char] = code
                return
            build_codes(node.left, code + '0')
            build_codes(node.right, code + '1')

        build_codes(root, "")
        encoded_text = ''.join(codes[ch] for ch in text)

        return codes, encoded_text, root

    @staticmethod
    def make_change(amount, coins):
        """
        Жадный алгоритм выдачи сдачи минимальным числом монет (корректен только для канонических систем).
        Сложность: O(n) — один проход по отсортированным номиналам.
        """
        coins_sorted = sorted(coins, reverse=True)
        res = {}
        rem = amount

        for coin in coins_sorted:
            if rem == 0:
                break
            cnt = rem // coin
            if cnt > 0:
                res[coin] = cnt
                rem -= coin * cnt

        if rem > 0:
            raise ValueError(f"Невозможно собрать сумму {amount} доступными номиналами")

        return res

    @staticmethod
    def prim_mst(vertices, edges):
        """
        Построение минимального остовного дерева с помощью алгоритма Прима.
        Сложность: O(E log V) — за счёт использования кучи для выбора рёбер.
        """
        if not vertices:
            return []

        # Построение списка смежности
        graph = {v: [] for v in vertices}
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        visited = set()
        mst = []
        start = vertices[0]

        heap = []
        visited.add(start)

        for neigh, w in graph[start]:
            heapq.heappush(heap, (w, start, neigh))

        while heap and len(visited) < len(vertices):
            w, u, v = heapq.heappop(heap)
            if v in visited:
                continue
            visited.add(v)
            mst.append(GraphEdge(u, v, w))
            for neigh, nw in graph[v]:
                if neigh not in visited:
                    heapq.heappush(heap, (nw, v, neigh))

        return mst

class PackSolver:
    """
    Реализации точных (не жадных) методов для дискретной задачи о рюкзаке.
    """

    @staticmethod
    def brute_force_0_1_pack(capacity, items):
        """
        Полный перебор всех подмножеств предметов для решения 0-1 рюкзака.
        Сложность: O(2^n) — экспоненциальное время.
        """
        n = len(items)
        max_val = 0
        best = []

        for mask in range(1 << n):
            cur_w = 0
            cur_v = 0
            sel = []
            for j in range(n):
                if mask & (1 << j):
                    cur_w += items[j].weight
                    cur_v += items[j].value
                    sel.append(items[j])
            if cur_w <= capacity and cur_v > max_val:
                max_val = cur_v
                best = sel

        return max_val, best

    @staticmethod
    def compare_pack_methods(capacity, items):
        """
        Сравнение жадного (дробного) и точного (0-1) подходов к задаче о рюкзаке.
        """
        print("Сравнение двух подходов к решению рюкзака:")
        print(f"Ёмкость рюкзака: {capacity}")
        print("Доступные предметы:")
        for it in items:
            print(f"  {it.name}: ценность={it.value}, вес={it.weight}, удельная={it.value / it.weight:.2f}")

        greedy_val, greedy_sel = GreedyMethods.fractional_pack(capacity, items)
        print(f"\nЖадный (дробный): {greedy_val:.2f}")
        print("Отобрано (в % от предмета):")
        for it, frac in greedy_sel:
            print(f"  {it.name}: {frac * 100:.1f}%")

        exact_val = None
        if len(items) <= 20:
            exact_val, exact_sel = PackSolver.brute_force_0_1_pack(capacity, items)
            print(f"\nТочное решение (0-1): {exact_val}")
            print("Выбранные предметы:")
            for it in exact_sel:
                print(f"  {it.name}")
            print(f"\nРазница в ценности: {greedy_val - exact_val:.2f}")
        else:
            print("\nТочный перебор не выполнен: количество предметов превышает 20")

        return greedy_val, exact_val