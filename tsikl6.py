'''
for x in range(0, 6):
	print("Salom")

for a in range(0, 4):
	print("Что")

for z in range(1, 3):
	print("uchta")

for d in range(0, 5):
	print("Что eto")			# 5 marta "Что eto" chiqadi
	print(list(range(10,15)))

print(list(range(10,15))) #natija [10, 11, 12, 13, 14]


for x in range(0, 5):
	print('привет %s' % x) #index bilan chiqadi привет 1, привет 2 ...
'''
'''
wizard_list = ['паучьи лапки', 'жабий палец', 'язык улитки',
'крыло летучей мыши', 'жир слизня', 'медвежий коготь']
for i in wizard_list:
	print(i) 				# spiskadagi hammamalumotni chiqarib berdi
'''
'''

wizard_list = ['паучьи лапки', 'жабий палец', 'язык улитки','крыло летучей мыши', 'жир слизня', 'медвежий коготь']
print(wizard_list[0])
print(wizard_list[1])
print(wizard_list[2])
print(wizard_list[3]) 
print(wizard_list[4])
print(wizard_list[5])  # for tsiklisiz kodimizni shunday yozgan bo'lardik


hugehairypants = ['огромные', 'волосатые', 'штаны']
for i in hugehairypants:
	print(i)
for j in hugehairypants:
	print(j)
	print()

car = ['nexia', 'matiz', 'damas']
for i in car:
	print(i)
	for j in car:
		print(j)
'''
'''
found_coins = 20
magic_coins = 70
stolen_coins = 3
coins = found_coins
for week in range(1, 53):
	coins = coins + magic_coins - stolen_coins
	print('Неделя %s = %s' % (week, coins))  
'''
'''
for x in range(1, 4):
	print("alam")

for x in range(1,10):
	print("hi")
print()
print()
'''
'''
from random import randint

for number in range(100000):
	x = randint(0, 10000)
	y = randint(1, 10000)
	if (x+1) / y + x == y:
		print('## found evolution')
		print('x =', x)
		print('y =', y)
		break
'''


# TSIKL WHILE
'''
for step in range(0,20):
	print(step)
	print()'''
'''step = 0
while step < 10000:
		print(step)
		if tired == True:
			break
		elif badwather == True:
			break
		else:
			step = step + 1

Итак, цикл while выполняет следующие действия:
1. Проверяет условие.
2. Выполняет код в блоке.
3. Повторяет все сначала. '''

x = 25
y = 55
while x<30 and y<60:
 	x = x+1
 	y = y+1
 	print(x, y) # x = 30 y=60 bo'lganda shartimiz yakunlanadi 
 					# unga qadar 25 va 55 sonlarimizga 1 qo'shilib boradi
print()

g = 48
b = 65
while g<45 and b<55:
	g = g-1
	b = b-1
	print(g,b)

for x in range(0, 20):
	print('привет%s'% x)
	if x < 9:
		break

a = 20
b = 30
while a < 25 and b < 35:
	a = a+1
	b = b+1
	print(a,b)
print()

c = 50
l = 80
while c < 60 and l < 88:
	c = c+1
	l = l+1
	print(c,l)
print()

p = 50
while p<55:
	p = p+1
	print(p)

print()

ingredients = ['слизни', 'пиявки', 'катышки из пупка гориллы', 'брови гусеницы', 'пальцы многоножки']
for i in ingredients:
	print(i)

print()

vazn = 60
oydagiVazn = vazn / 100 * 16.5
for i in range(0, 15):
	i = oydagiVazn + 1
	print(i)

import turtle
t = turtle.Pen()
