import random

num = random.randint(1, 100)
fin = int(input('Введи число: '))
tries = 1


while fin != num:
    if fin < num:
        print(f"Загаданное число больше: {fin}")
        fin = int(input('Введи число: '))
        tries += 1

    elif fin > num:
        print(f"Загаданное число меньше: {fin}")
        fin = int(input('Введи число: '))
        tries += 1

print(f"Победа! Количестово попыток: {tries}")
