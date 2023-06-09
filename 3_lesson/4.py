"""
4. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""

# используя функцию sort()

def func_sum(arg1, arg2, arg3):
    list_arg = [arg1, arg2, arg3]
    list_arg.sort()
    print(f'Сумма двух наибольших аргументов равна: {list_arg[1] + list_arg[2]}')


func_sum(
    int(input('Аргумент 1:')),
    int(input('Аргумент 2:')),
    int(input('Аргумент 3:')),
)

# без функции sort()

"""
def func_sum(arg1, arg2, arg3):
    print(f'Сумма двух наибольших аргументов равна: {arg1 + arg2 + arg3 - min([arg1, arg2, arg3])}')


func_sum(
    int(input('Аргумент 1:')),
    int(input('Аргумент 2:')),
    int(input('Аргумент 3:')),
)
"""
