import random, sys

digits = '0123456789'
size = 4

while True:

    chosen = ''.join(random.sample(digits, size))
    
    print(chosen)
    guesses = 0
    while True:

        guesses += 1
        while True:
            # спросить пользователя
            guess = input('\nПопытка [%i]: ' % guesses).strip()
            if len(guess) == size and \
                    all(char in digits for char in guess) \
                    and len(set(guess)) == size:
                break
            print ("Попробуй ещё раз. Введи %i неповторяющихся цифр от 0 до 9" % size)
            
        if guess == chosen:
            print ('\nМоё почтенье, угадал с ', guesses, ' раза.\nЕсли желаете сыграть ещё раз, введите 1. Для выхода введите 0')
            is_again = input().strip()
            if is_again != '1':
                sys.exit()
                # exit
            else:
                break
        bulls = 0
        cows = 0

        for i in range(size):
            if guess[i] == chosen[i]:
                bulls += 1
            elif guess[i] in chosen:
                cows += 1

        print ('%i Быка\n  %i Коровы' % (bulls, cows))
