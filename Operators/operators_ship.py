ship_count = int(input('Введите количество кораблей: '))

one = 'корабль'
two = 'корабля'
many = 'кораблей'

remainder = ship_count % 100

if 4 < remainder < 21:
    word = many
else:
    last = remainder % 10

    if last == 1:
        word = one
    elif last == 2 or last == 3 or last == 4:
        word = two
    else:
        word = many

result = str(ship_count) + ' ' + word

print(result)
