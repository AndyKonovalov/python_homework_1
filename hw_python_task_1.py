# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

day_number = int(input('Введите цифру дня недели '))
if day_number > 7 or day_number < 1:
    print('Ошибка ввода. Введите число от 1 до 7')
else:
    if day_number == 6 or day_number == 7:
        print('Выходной')
    else:
        print('Будний день')