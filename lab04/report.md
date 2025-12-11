# Лабораторная работа № 4
# Алгоритмы сортировки

**Дата:** 30.11.2025
**Семестр:** 3 курс 5 семестр
**Группа:** ПИЖ-б-о-23-2-2
**Дисциплина:** Анализ сложности алгоритмов
**Студент:** Зволибовская Екатерина Валерьевна

## Характеристики ПК для тестирования
- Процессор: 11th Gen Intel(R) Core(TM) i5-11400F CPU @ 2.60 GHz
- GPU: NVIDEA GeForce RTX 4060
- Оперативная память: 16 GB
- ОС: Windows 10
- Python: 3.11 (64-bit)

## Цель работы
Изучить и реализовать основные алгоритмы сортировки. Провести их теоретический и
практический сравнительный анализ по временной и пространственной сложности. Исследовать
влияние начальной упорядоченности данных на эффективность алгоритмов. Получить навыки
эмпирического анализа производительности алгоритмов.

## Практическая часть

### Выполненные задачи

- [x] Реализовать 5 алгоритмов сортировки (Bubble Sort, Insertion Sort, Merge Sort, Quick Sort, Heap Sort).
- [x] Провести теоретический анализ времени и памяти каждого алгоритма.
- [x] Экспериментально сравнить время выполнения алгоритмов на различных наборах данных.
- [x] Проанализировать влияние начальной упорядоченности данных на эффективность сортировок.


## Результаты выполнения

### Пример работы программы

```bash
Generating datasets...
Running performance tests (this may take a while for large sizes)...
Testing size=100, kind=random ...
  bubble_sort: 0.001255s (avg over 3)
  insertion_sort: 0.000745s (avg over 3)
  merge_sort: 0.000626s (avg over 3)
  quick_sort: 0.000538s (avg over 3)
  heap_sort: 0.000411s (avg over 3)
Testing size=100, kind=sorted ...
  bubble_sort: 0.000337s (avg over 3)
  insertion_sort: 0.000338s (avg over 3)
  merge_sort: 0.000663s (avg over 3)
  quick_sort: 0.000421s (avg over 3)
  heap_sort: 0.000374s (avg over 3)
Testing size=100, kind=reversed ...
  bubble_sort: 0.001477s (avg over 3)
  insertion_sort: 0.001351s (avg over 3)
  merge_sort: 0.000591s (avg over 3)
  quick_sort: 0.000427s (avg over 3)
  heap_sort: 0.000205s (avg over 3)
Testing size=100, kind=almost_sorted ...
  bubble_sort: 0.000586s (avg over 3)
  insertion_sort: 0.000414s (avg over 3)
  merge_sort: 0.000782s (avg over 3)
  quick_sort: 0.000418s (avg over 3)
  heap_sort: 0.000382s (avg over 3)
...
Saved summary table to results/summary.csv
Saved results/time_vs_size_random.png
Saved results/time_vs_kind_n5000.png
Done. Results directory: /home/renoir/ChekalinEU/lab4/results
```


## Сводная таблица результатов

Таблица содержится в `results/summary.csv`.


## Визуализация

### Зависимость времени выполнения от размера массива (Тип данных — random)

![time\_vs\_size\_random](results/time_vs_size_random.png)


### Зависимость времени выполнения от типа данных (n = 5000)

![time\_vs\_kind\_n5000](results/time_vs_kind_n5000.png)

## Выводы

В результате лабораторной работы Bubble Sort и Insertion Sort (O(n²)) быстро деградируют при росте размера данных. Выясняется, что Merge Sort, Quick Sort и Heap Sort (O(n log n)) существенно быстрее на больших объёмах, а Insertion Sort и Bubble Sort наиболее эффективны на почти отсортированных данных, что подтверждает теорию.


## Ответы на контрольные вопросы

1. O(n²) в худшем случае: Bubble Sort, Insertion Sort, Quick Sort (при плохом выборе опоры). O(n log n) во всех случаях: Merge Sort, Heap Sort. Quick Sort — O(n log n) в среднем.

2. Потому что она делает мало сравнений и перестановок, если элементы уже близки к нужной позиции. В лучшем случае её сложность — O(n).

3. Устойчивая сортировка сохраняет относительный порядок равных элементов, неустойчивая — нет.

4. Quick Sort рекурсивно разделяет массив относительно опорного элемента: элементы меньше — влево, больше — вправо. При неудачном выборе (например, крайний элемент в отсортированном массиве) разделение становится несбалансированным, и сложность достигает O(n²).

5. Когда требуется гарантированное время O(n log n), устойчивость или работа с данными, не помещающимися в оперативную память (внешняя сортировка).
