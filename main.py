import random, sys

digits = '0123456789'
size = 4

while True:
    chosen = ''.join(random.sample(digits, size))
    print ('Я выбрал число, состоящее из цифр от 0 до 9, расположенных в случайном порядке.\nПредположи, какие %s цифры я выбрал и введи их. Я отвечу, сколько из них угаданы на неверных позициях (коровы), а какие угаданы вплоть до позиции (быки).\nУдачи!' % (size))
    # print(chosen)
    guesses = 0
    while True:
        guesses += 1
        while True:
            # спросить пользователя
            guess = input('\nПопытка [%i]: ' % guesses).strip()
            # проверка на неправильный ввод
            if len(guess) == size and \
                    all(char in digits for char in guess) \
                    and len(set(guess)) == size:
                break
            print ("Попробуй ещё раз. Введи %i неповторяющихся цифр от 0 до 9" % size)
        if guess == chosen:
            print ('\nМоё почтенье, угадал с ', guesses, ' раза.\nЕсли желаете сыграть ещё раз, введите 1. Для выхода введите 0')
            again = input('Ещё раз?').strip()
            if again != '1':
                sys.exit()
            else:
                break
        bulls = cows = 0
        for i in range(size):
            if guess[i] == chosen[i]:
                bulls += 1
            elif guess[i] in chosen:
                cows += 1
        print ('  %i Быка\n  %i Коровы' % (bulls, cows))
