from random import randint


def get_attack(char_name, char_class):
    char_classes = {
        'warrior': (3, 5),
        'mage': (5, 10),
        'healer': (-3, -1)
        }

    if char_class in char_classes:
        damage_range = char_classes[char_class]
        damage = 5 + randint(*damage_range)

        return (f'{char_name} нанёс урон противнику равный {damage}')


def get_defence(char_name, char_class):
    char_classes = {
        'warrior': (5, 10),
        'mage': (-2, 2),
        'healer': (2, 5)
    }

    if char_class in char_classes:
        defense_range = char_classes[char_class]
        defence = 10 + randint(*defense_range)

        return f'{char_name} блокировал {defence} урона'


def get_special(char_name, char_class):
    char_classes = {
        'warrior': f'Выносливость {80 + 25}',
        'mage': f'Атака {5 + 40}',
        'healer': f'Защита {10 + 30}'
    }

    if char_class in char_classes:
        skill_message = char_classes[char_class]

        return f'{char_name} применил специальное умение «{skill_message}»'


def start_training(char_name, char_class):
    char_classes = {
        'warrior': 'ты Воитель — отличный боец ближнего боя.',
        'mage': 'ты Маг — превосходный укротитель стихий.',
        'healer': 'ты Лекарь — чародей, способный исцелять раны.'
    }

    if char_class in char_classes:
        print(f'{char_name}, {char_classes[char_class]}')
        print('Потренируйся управлять своими навыками.')
        description = [
            'Введи одну из команд: attack — чтобы атаковать противника,',
            'defence — чтобы блокировать атаку противника',
            'или special — чтобы использовать свою суперсилу.'
        ]
        print(*description)
        print('Если не хочешь тренироваться, введи команду skip.')

    cmd = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(get_attack(char_name, char_class))
        if cmd == 'defence':
            print(get_defence(char_name, char_class))
        if cmd == 'special':
            print(get_special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class():
    approve_choice = None
    char_class = None

    hint_list = [
        'Введи название персонажа, за которого хочешь играть:',
        'Воитель — warrior, Маг — mage, Лекарь — healer: '
    ]

    hint = ' '.join(hint_list)

    char_classes = {
        'warrior': [
            'Воитель — дерзкий воин ближнего боя.',
            'Сильный, выносливый и отважный.'
        ],
        'mage': [
            'Маг — находчивый воин дальнего боя.',
            'Обладает высоким интеллектом.'
        ],
        'healer': [
            'Лекарь — могущественный заклинатель.',
            'Черпает силы из природы, веры и духов.'
        ]
    }

    while approve_choice != 'y':
        char_class = input(hint)

        if char_class in char_classes:
            print(*char_classes[char_class])

        input_message = [
            'Нажми (Y), чтобы подтвердить выбор, или любую другую',
            'кнопку, чтобы выбрать другого персонажа '
        ]
        approve_choice = input(*input_message).lower()

    return char_class


def main():
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class = choice_char_class()
    print(start_training(char_name, char_class))


main()
