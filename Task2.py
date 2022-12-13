# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print('Введите X :');
x = int(input())

print('Введите Y :');
y = int(input())

print('Введите Z :');
z = int(input())

left = not (x or y or z)
right = not x and not y and not z
result = left == right

if result == True:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")