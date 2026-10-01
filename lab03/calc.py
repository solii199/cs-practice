a = int(input('введите 1ое число: '))
calc =  input("введите  операцию: ")
b = int(input('введите 2ое число: '))
if calc == '+':
    print(a + b)
elif calc == '-':
    print(a - b)
elif calc == '*':
    print(a * b)
elif calc == '/' and b != 0:
    print(a / b)
else:
    print('Ошибка')