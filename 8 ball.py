import random

def restart():
    if input('Желаешь задать ещё вопрос?').lower() in ['да']:
        start()
    else:
        print('Возвращайся если возникнут вопросы!')
        

def start():
    while True:
        ask = input('Можешь задать свой вопрос:')
        print(random.choice(answers))
        restart()
        break


answers = [
    'Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом', 'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да', 'Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет', 'Перспективы не очень хорошие', 'Весьма сомнительно'
           ]

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
user_name = input('Укажите Ваше имя:')
print('Привет,', user_name, end = '!')
print()
start()
