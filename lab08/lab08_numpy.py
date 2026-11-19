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


print("\nЗадание 4")
matrix = np.arange(1, 26).reshape(5, 5)
print("Исходная матрица 5x5:\n", matrix)

first_three_rows = matrix[:3, :]
print("\nПервые три строки:\n", first_three_rows, "\nshape:", first_three_rows.shape)

last_two_rows = matrix[-2:, :]
print("\nПоследние две строки:\n", last_two_rows, "\nshape:", last_two_rows.shape)

first_two_cols = matrix[:, :2]
print("\nПервые два столбца:\n", first_two_cols, "\nshape:", first_two_cols.shape)

middle_block = matrix[1:4, 2:5]
print("\nСтроки 1–3 и столбцы 2–4:\n", middle_block, "\nshape:", middle_block.shape)

bottom_right = matrix[-2:, -2:]
print("\nПравый нижний угол 2x2:\n", bottom_right, "\nshape:", bottom_right.shape)

print("\nЗадание 5")
vec_data = [10, 20, 30, 40, 50]
vector = np.array(vec_data)
vector[1:4] = 0

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9

changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[1::2] = -1

print("changed_hours:", changed_hours)
print("Исходный hours:", hours)

changed_matrix = matrix.copy()
changed_matrix[1, :] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 100

print("\nchanged_matrix:\n", changed_matrix)
print("\nИсходная matrix:\n", matrix)

print("\nЗадание 6")
numbers = np.arange(12)
table = numbers.reshape(3, 4)
transposed = table.T

print("Форма numbers:", numbers.shape)
print("Форма table:", table.shape)
print("Форма transposed:", transposed.shape)



