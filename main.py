import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Adivinhe um numero entre 1 e {x}: "))
        if guess < random_number:
            print("Desculpe, adivinhe novamente. Muito baixo")
        if guess > random_number:
            print("Desculpe, adivinhe novamente. Muito alto")
    print(f"Isso ae!!!, PARABENS. Voce conseguiu adinhar o numero {random_number} corretamente!!!")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # Pode tambem ser alto b/c baixo = alto

        feedback = input(f'É {guess} muito alto (A), muito baixo(B), ou correto(C)??? ').lower()
        if feedback == 'a':
            high = guess -1

        elif feedback == 'b':
            low = guess + 1
    print(f'Wow!! O computador adivinhou o seu numero, {guess}, corretamente !!! ')

guess(10)


