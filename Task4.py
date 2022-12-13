# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат
# точек в этой четверти (x и y).

print('Введите номер координатной четверти')
quart = int(input())

if quart == 1:
    print('x > 0 and y > 0')
elif quart == 2:
    print('x < 0 and y > 0')
elif quart == 3:
    print('x < 0 and y < 0')
elif quart == 4:
    print('x > 0 and y < 0')
