from modules.heap import SmallHeap

class QueueItem:
    """
    Объект задачи в приоритетной очереди: содержит приоритет и связанное значение.
    """

    def __init__(self, priority, value):
        self.priority = priority
        self.value = value

    def __lt__(self, other):
        return self.priority < other.priority

    def __eq__(self, other):
        return self.priority == other.priority and self.value == other.value

    def __str__(self):
        return f"({self.priority}: {self.value})"

    def __repr__(self):
        return f"QueueItem({self.priority}, {self.value})"


class TaskQueue:
    """
    Приоритетная очередь, реализованная на основе min-кучи.
    Более низкое числовое значение приоритета означает более высокий приоритет.
    """

    def __init__(self):
        self.heap = SmallHeap()

    def __len__(self):
        return len(self.heap)

    def __str__(self):
        return f"TaskQueue({[str(item) for item in self.heap.heap]})"

    def push_with_priority(self, value, priority=0):
        """Добавить задачу с указанным приоритетом. Временная сложность: O(log n)"""
        item = QueueItem(priority, value)
        self.heap.push(item)

    def pop_priority(self):
        """Извлечь и вернуть задачу с наивысшим приоритетом. Временная сложность: O(log n)"""
        item = self.heap.pop()
        return item.value if item else None

    def peek_priority(self):
        """Посмотреть задачу с наивысшим приоритетом без её удаления. Временная сложность: O(1)"""
        item = self.heap.top()
        return item.value if item else None

    def empty(self):
        return len(self.heap) == 0

    def update_priority(self, value, new_priority):
        """
        Обновить приоритет существующей задачи. Реализовано линейным поиском — сложность O(n).
        После изменения приоритета элемент перемещается в нужную позицию с помощью всплытия или погружения.
        """
        for i, item in enumerate(self.heap.heap):
            if item.value == value:
                old_priority = item.priority
                item.priority = new_priority

                if new_priority < old_priority:
                    self.heap._bubble_up(i)
                elif new_priority > old_priority:
                    self.heap._sink_down(i)
                return True

        return False