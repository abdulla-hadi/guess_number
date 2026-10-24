import random

secret = random.randint(1, 100)
guess = 0
attempts = 0

while guess != secret:
    try:
        guess = int(input("Угадайте число от 1 до 100: "))
    except ValueError:
        print("Нужно ввести число")
        continue
    attempts = attempts + 1
    if guess < secret:
        print("Загаданное число больше") 
    elif guess > secret:
        print("Загаданное число меньше") 

print(f"Ты угадал с {attempts} попытки")  