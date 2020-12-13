test_file = open('d:/Python/BotirZiyatov/vstroennieFunc.py', 'w')
test_file.write('Что это– зеленое и крякает? Жабокряк!')
test_file.close()


creature_list = ['единорог', 'циклоп', 'фея', 'эльф', 'дракон', 
'тролль']
print(len(creature_list))


fruit = ['яблоко', 'банан', 'клементин', 'питайя']
length = len(fruit)
for x in range(0, length):
	print('фрукт с индексом%s: %s' % (x, fruit[x]))

strings = 'строкаСТРОКА'
print(max(strings))

guess_this_number = 61
player_guesses = [12, 15, 70, 45]
if max(player_guesses) > guess_this_number:
	print('Бабах! Вы проиграли')

a = abs(10) + abs(-10)
print(a)
b = abs(-10) + -10
print(b)