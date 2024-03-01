from random import randint

def generate_number(min_num, max_num):
    return randint(min_num, max_num)

def is_valid(num, min_num, max_num):
    return num.isdigit() and min_num <= int(num) <= max_num

def play_game():
    min_num = 1
    max_num = 1000
    x = generate_number(min_num, max_num)
    count = 0

    print('Привет, я хочу сыграть с тобой в игру!')
    print('Чтобы выжить, ты должен угадать задуманное мною число от', min_num, 'до', max_num)
    print('Но не спеши волноваться, я буду давать тебе подсказки.')

    while True:
        n = input('Введи число:')
        
        if not is_valid(n, min_num, max_num):
            print('Так не пойдёт! Введи числа от', min_num, 'до', max_num)
        else:
            n = int(n)
            break

    while True:
        if n < x:
            print('Твоё число МЕНЬШЕ загаданного, попробуй ещё раз.')
        elif n > x:
            print('Твоё число БОЛЬШЕ загаданного, попробуй ещё раз.')
        else:
            if count == 0:
                print('У тебя получилось угадать с первого раза, невозможно!')
            else:
                print('У тебя получилось угадать с', count, 'попытки, поздравляю!')
            break

        n = int(input('Введи число:'))
        count += 1

play_game()