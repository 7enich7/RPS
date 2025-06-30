import random

step_bot_list = ['камень', 'ножницы', 'бумага']
z, x = 0, 0


print('Игра началась')


def go():
    global z
    global x

    if z != 3 and x != 3:
        def step_me():
            print('Ваш ход:')
            s_me = input('')
            return s_me

        def step_bot():
            random_bot = random.choice(step_bot_list)
            return random_bot

        def game(g_s_m, g_s_b):
            global z
            global x
            if g_s_b == g_s_m:
                print('ничья')
                print(f'Счёт: {z}:{x}')
                go()
            elif (g_s_b == 'камень' and g_s_m == 'ножницы') or (g_s_b == 'ножницы' and g_s_m == 'бумага') \
                    or (g_s_b == 'бумага' and g_s_m == 'камень'):
                print(f'Бот выиграл, выбрав {g_s_b}')
                x += 1
                print(f'Счёт: {z}:{x}')
                go()
            elif (g_s_b == 'камень' and g_s_m == 'бумага') or (g_s_b == 'ножницы' and g_s_m == 'камень') \
                    or (g_s_b == 'бумага' and g_s_m == 'ножницы'):
                print(f'Вы выиграли, бот выбрал {g_s_b}')
                z += 1
                print(f'Счёт: {z}:{x}')
                go()
            elif g_s_m == 'выход':
                print('Игра закончилась')
                print(f'Счёт: {z}:{x}')
                exit()
            elif g_s_m == 'хуй':
                print('ТЫСОВСЕМ ДАУН??')
                go()
            else:
                print('Слово не найдено')
                go()

        go_step_me = step_me()
        go_step_bot = step_bot()
        game(go_step_me, go_step_bot)
    else:
        if z == 3:
            print('ХОРОШ, ВЫЕБАЛ ЭТОГО БОТА КОНЧЕНОГО')
            exit()
        else:
            print('НУ ТЫ И ЛОХ ПОДЗАЛУПНЫЙ')
            exit()


go()
