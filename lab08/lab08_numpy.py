import numpy as np

print("Задание 1")
hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3)

print("hours:", hours)
print("shape:", hours.shape)
print("ndim:", hours.ndim)
print("size:", hours.size)
print("dtype:", hours.dtype)

print("\nline:", line)
print("zeros:", zeros, "| dtype:", zeros.dtype)
print("unknown_table:\n", unknown_table)
print("identity:\n", identity)

print("\nЗадание 2")
print("Третий элемент:", hours[2])
print("Последний элемент:", hours[-1])
print("Элементы с индексами 2–5:", hours[2:6])
print("Каждый второй элемент:", hours[::2])
print("В обратном порядке:", hours[::-1])

print("\nЗадание 3")
row0 = [12, 14, 13, 15]
row1 = [11, 13, 16, 17]
row2 = [10, 12, 15, 18]
temperatures = np.array([row0, row1, row2])

print("Форма:", temperatures.shape)
print("Число измерений:", temperatures.ndim)
print("Число элементов:", temperatures.size)
print("Вторая строка, третий столбец:", temperatures[1, 2])
print("Первая строка:", temperatures[0])
print("Последний столбец:", temperatures[:, -1])
print("Первые две строки без первого столбца:\n", temperatures[:2, 1:])

center_fragment = temperatures[0:2, 1:3]
print("Центральный фрагмент 2x2:\n", center_fragment)
print("Форма центрального фрагмента:", center_fragment.shape)


