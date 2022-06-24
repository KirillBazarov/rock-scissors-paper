# Импорт для def computer_choice
from random import randint

RPS = {
    1: "Камень",
    2: "Ножницы",
    3: "Бумага"
}
hello_and_question = '''
Приветствую в КМН! Ты помнишь правила или тебе их напомнить? (Если нужно напомнить напиши 1) 
'''
# choosing_how_many_rounds = "Теперь нужно определить сколько раундов будем играть(1 или 3)."
rules = '''Победитель определяется по следующим правилам:
1. Бумага побеждает камень («бумага обёртывает камень»).
2. Камень побеждает ножницы («камень затупляет или ломает ножницы»).
3. Ножницы побеждают бумагу («ножницы разрезают бумагу»).
Если игроки показали одинаковый знак, то засчитывается ничья и игра или раунд переигрывается.'''


# Выбор игрока
def players_choice() -> int:
    player_chose = int(input('''
Введи свой выбор:
1 -- Камень
2 -- Ножницы
3 -- Бумага
    '''))  # Значения от пользователя
    if player_chose in [1, 2, 3]:  # Проверка на нужные числа
        print(f"Ты выбрал {RPS.get(player_chose)}")
        return player_chose
    else:
        print("Ты ввел не то число)))")


# Дает случайное число от 1 до 3. Которое обозначает камень, ножницы или бумагу.
def computer_choice() -> int:
    computer_chose = randint(1, 3)
    if computer_chose == 3:
        print(f"А твой противник выбрал Бумагу")  # Правильное склонение
    else:
        print(f"А твой противник выбрал {RPS.get(computer_chose)}")
    return computer_chose


# Функция находит победителя
# Просто огромное кол-во иф(другой способ слишком сложно искать)
def search_winner(vibor_igroka, vibor_pc) -> None:
    if vibor_igroka == vibor_pc:
        print("Ничья")
    elif vibor_igroka == 1 and vibor_pc == 2:
        print("""Ты победил!!!
        \nКамень затупляет или ломает ножницы
        """)
    elif vibor_igroka == 1 and vibor_pc == 3:
        print("""Ты проиграл(((
        \nБумага обёртывает камень
        """)
    elif vibor_igroka  == 2 and vibor_pc == 1:
        print("""Ты проиграл(((
        \nКамень затупляет или ломает ножницы
        """)
    elif vibor_igroka == 2 and vibor_pc == 3:
        print("""Ты победил!!!
        \nНожницы разрезают бумагу
        """)
    elif vibor_igroka == 3 and vibor_pc == 1:
        print("""Ты победил!!!
        \nБумага обёртывает камень
        """)
    elif vibor_igroka == 3 and vibor_pc == 2:
        print("""Ты проиграл(((
        \nНожницы разрезают бумагу
        """)


def play() -> None:
    search_winner(vibor_igroka, vibor_pc)


def main() -> None:
    play_again = ''  # Что бы запустить игру. Потом его изменить и выйти.
    while play_again.lower() != '-':  # проверка на выход из игры работает после 2-го раза
        play()  # запуск игры
        play_again = input("Хочешь сыграть еще раз (если нет то введи - ) ")
    else:
        print("\nудачи!")


class Player:
    def __init__(self, name):
        self.name = name
        self.vibor_igroka = players_choice()

class PC:
    def __init__(self):
        self.vibor_pc = computer_choice()



print(hello_and_question)  # Приветствие
if input("") == "1":
    print(rules)
Mi = Player(input('Введи свои имя или никнейм(Это нужно для статистики)\n'))
p = PC()
vibor_igroka = Mi.vibor_igroka
vibor_pc = p.vibor_pc
main()
