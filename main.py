import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Adivinhe um numento entre 1 e {x}: "))
        if guess < random_number:
            print("Desculpe, adivinhe novamente. Muito baixo")
        if guess > random_number:
            print("Desculpe, adivinhe novamente. Muito alto")
    print(f"Isso ae!!!, PARABENS. Voce conseguiu adinhar o numero {random_number} corretamente!!!")
guess(10)