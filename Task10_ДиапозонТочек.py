'''
Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат
точек в этой четверти (x и y).
'''
print('Введите номер четверти: ')
a = int(input())
if a ==1:
    print('Все возможные Х > 0, все возможные Y > 0')
if a == 2:
    print('Все возможные Х < 0, все возможные Y > 0')
if a == 3:
    print('Все возможные Х < 0, все возможные Y < 0')
if a == 4:
    print('Все возможные Х > 0, все возможные Y < 0')
if a > 4:
    print('В координатной плоскости всего четыре четверти, попробуй еще раз')