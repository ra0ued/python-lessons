recipient = str(input())
player_name = recipient.split('@')[0]
player_ships_count = int(input())
reward_ships_count = int(input())
code = player_name[1::2]

endings_one = 'ь'
endings_two = 'я'
endings_many = 'ей'

remainder = player_ships_count % 100

if 4 < remainder < 21:
    player_ending = endings_many
else:
    last = remainder % 10

    if last == 1:
        player_ending = endings_one
    elif last == 2 or last == 3 or last == 4:
        player_ending = endings_two
    else:
        player_ending = endings_many

remainder = reward_ships_count % 100

if 4 < remainder < 21:
    reward_ending = endings_many
else:
    last = remainder % 10

    if last == 1:
        reward_ending = endings_one
    elif last == 2 or last == 3 or last == 4:
        reward_ending = endings_two
    else:
        reward_ending = endings_many

title = f'[Массовая рассылка] Уважаемый игрок Мира кораблей, {player_name}! '
body = f"""\nСпасибо, что любите и играете в нашу игру. \
       \nМы заметили, что у вас всего {player_ships_count} Корабл{player_ending}.  \
       \nПоэтому, мы дарим вам подарок: {reward_ships_count} Корабл{reward_ending}. 
       """

total = title + body + f'\nВаш промокод: {code}!'

print(total)
