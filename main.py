recipient = input()
player_name = recipient.split('@')[0]
player_ships_count = input()
reward_ships_count = input()

title = f'[Массовая рассылка] Уважаемый игрок Мира кораблей, {player_name}!'
body = 'Спасибо, что любите и играете в нашу игру.' \
       '\nМы заметили, что у вас всего %s' % player_ships_count + ' Корабл<подставь руками>. ' \
                                                                  "\nПоэтому, мы дарим вам подарок:%s" % reward_ships_count + 'Корабл<подставь руками>!'

total = title + body + 'Ваш промокод: {<вставь промокод>}'

print(total)