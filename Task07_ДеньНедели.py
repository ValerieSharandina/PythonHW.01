'''
Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

Пример:

- 6 -> да
- 7 -> да
- 1 -> нет
'''
week_days = {1: "Понедельник", 2: "Вторник", 3: "Среда", 4: "Четверг", 5: "Пятница", 6: "Суббота", 7: "Воскресенье"} #создали словарь

int_test = True
while int_test: #проверка на правильность ввода
    week_day_number = input("Введите день недели : ")
    if week_day_number.isdigit():
        week_day_number = int(week_day_number)
        if week_day_number >= 1 and week_day_number <= 7:
            int_test = False
        else:
            print("Это не день недели")
    else:
        print("Это не число")

if week_day_number == 6 or week_day_number == 7:
    print(f"{week_day_number} это {week_days[week_day_number]} -> Выходной")
else:
    print(f"{week_day_number} это {week_days[week_day_number]} -> надо на работу")

