# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for x in 0,1:
    for y in 0,1:
        for z in 0,1:

            left = not (x or y or z)
            right = not x and not y and not z
            result = left == right

            if result == True:
                print(f"Утверждение истинно")
            else:
                print(f"Утверждение ложно")