from random import choice

_answers_counts = {}


def results(question, count):
    _answers_counts[question] = count


def print_results():
    print(*(f'Загадка: {key} отгадана за {value} попыток.' for key, value in _answers_counts.items()),
          sep='\n')


def quest(question, answers, attempts):
    count = 0
    while attempts > 0:
        count += 1
        print(question)
        answer = input('Ваш ответ: ')
        if answer in answers:
            results(question, count)
            print(f'Победа! Угадал за {count} попыток.')
            break
        else:
            print('Ответ неверный...')
        attempts -= 1
    else:
        print('Не угадал, попытки исчерпаны.')


def many_quests(iters):
    quests = {'Сколько мне лет?': ['99', 'много'],
              'Какого цвета огнетушитель?': ['красный', 'жёлтый'],
              'Что пьют коровы?': ['воду'],
              'Идут два крокодила, один зелёный, другой направо. Зачем мне холодильник, если я не курю?':
              ['да', 'пежо', 'гладиолус']}

    for i in range(iters):
        question = choice(list(quests.keys()))
        quest(question, quests[question], 3)
