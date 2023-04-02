from random import randint


def attack(char_name, char_class):
    pattern = {'warrior': (8, 10), 'mage': (10, 15), 'healer': (2, 4)}
    return (f'{char_name} нанёс урон противнику равный ' +
            f'{randint(*pattern[char_class])}')


def defence(char_name, char_class):
    pattern = {'warrior': (15, 20), 'mage': (8, 12), 'healer': (12, 15)}
    return f'{char_name} блокировал {randint(*pattern[char_class])} урона'


def special(char_name, char_class):
    pattern = {'warrior': 105, 'mage': 45, 'healer': 40}
    return (f'{char_name} применил специальное умение «Защита ' +
            f'{pattern[char_class]}»')


def start_training(char_name, char_class):
    pattern = {
                'warrior': ', ты Воитель — отличный боец ближнего боя.',
                'mage': ', ты Маг — превосходный укротитель стихий.',
                'healer': ', ты Лекарь — чародей, способный исцелять раны.'
                }

    print(char_name + pattern[char_class])
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника,'
          ' defence — чтобы блокировать атаку противника или'
          ' special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')

    cmd = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'skip':
            break
        function_reference = globals()[cmd]
        print(function_reference(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class():
    approve_choice = None
    char_class = None
    while approve_choice != 'y':
        char_class = input(
            'Введи название персонажа, за которого хочешь играть:'
            ' Воитель — warrior, Маг — mage, Лекарь — healer: ')
        pattern = {
                'warrior': 'Воитель — дерзкий воин ближнего боя.'
                           ' Сильный, выносливый и отважный.',
                'mage': 'Маг — находчивый воин дальнего боя. '
                        ' Обладает высоким интеллектом.',
                'healer': 'Лекарь — могущественный заклинатель.'
                          ' Черпает силы из природы, веры и духов.'
                }
        print(pattern.get(char_class))
        approve_choice = input(
            'Нажми (Y), чтобы подтвердить выбор, или любую другую кнопку,'
            ' чтобы выбрать другого персонажа ').lower()
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
