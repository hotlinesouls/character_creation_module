from random import randint
from graphic_arts.start_game_banner import run_screensaver


def attack(char_name: str, char_class: str) -> str:
    """Запускает атаку."""
    if char_class == 'warrior':
        damage = randint(8, 13)
        return f'{char_name} нанёс урон противнику равный {damage}'
    if char_class == 'mage':
        damage = randint(10, 15)
        return f'{char_name} нанёс урон противнику равный {damage}'
    if char_class == 'healer':
        damage = randint(2, 4)
        return f'{char_name} нанёс урон противнику равный {damage}'


def defence(char_name: str, char_class: str) -> str:
    """Запускает защиту."""
    if char_class == 'warrior':
        damage = randint(15, 20)
        return f'{char_name} блокировал {damage}'
    if char_class == 'mage':
        damage = randint(8, 12)
        return f'{char_name} блокировал {damage}'
    if char_class == 'healer':
        damage = randint(12, 15)
        return f'{char_name} блокировал {damage}'


def special(char_name: str, char_class: str) -> str:
    """Запускает примениние специального умения."""
    if char_class == 'warrior':
        return f'{char_name} применил специальное умение «Выносливость 105»'
    if char_class == 'mage':
        return f'{char_name} применил специальное умение «Атака 45»'
    if char_class == 'healer':
        return f'{char_name} применил специальное умение «Защита 40»'


def start_training(char_name: str, char_class: str) -> str:
    """Запускает тренировку с различными возможностями.
    Атаковать, защититься, применить
    специальное умение или
    вовсе пропустить её.
    """
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')

    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника,'
          'defence — чтобы блокировать атаку противника'
          'или special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    """Запускает выбор класса."""
    approve_choice: str = None
    char_class: str = None
    while approve_choice != 'y':
        input_message = 'Введи название персонажа, за которого хочешь играть:'
        ' Воитель — warrior, Маг — mage, Лекарь — healer:'
        char_class = input(input_message)
        if char_class == 'warrior':
            print('Воитель — дерзкий воин ближнего боя.'
                  'Сильный, выносливый и отважный.')
        if char_class == 'mage':
            print('Маг — находчивый воин дальнего боя.'
                  'Обладает высоким интеллектом.')
        if char_class == 'healer':
            print('Лекарь — могущественный заклинатель.'
                  'Черпает силы из природы, веры и духов.')
        input_message = ('Нажми (Y), чтобы подтвердить выбор,'
                         'или любую другую кнопку,'
                         'чтобы выбрать другого персонажа ')
        approve_choice = input(input_message).lower()
    return char_class


def main() -> None:
    """Запускает анимацию, создание персонажа и тренировку."""
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))
 
  
if __name__ == '__main__':
    main()
