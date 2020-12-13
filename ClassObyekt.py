class Animate():
	pass

class Animals(Animate):
	def breath(self):
		print('Nafas olmoq')
	def move(self):
		print('Harakatlanmoq')
	def eat_food(self):
		print('Ovqat yemoq')
class Mammals(Animals):
	def feed_young_with_milk(self):
		print('Sut emizish')
class Giraffes(Mammals):
	def eat_leaves_from_trees(self):
		print('Barglarni yemoq')

reginald = Giraffes()
harold = Giraffes()
reginald.move()
harold.eat_leaves_from_trees()

'''Функции, вызывающие другие функции'''
class Giraffes(Mammals):
	def find_food(self):
		self.move()
		print("Men ovqat topdim!")
		self.eat_food()
	def eat_leaves_from_trees(self):
		self.eat_food()
	def dance_a_jig(self):
		self.move()
		self.move()
		self.move()
reginald = Giraffes()
reginald.dance_a_jig()

class Giraffes(Mammals):
	def __init__(self, spots):
		self.giraffe_spots = spots
ozwald = Giraffes(100)
print(ozwald.giraffe_spots)

'''
import turtle
avery = turtle.Pen()
kate = turtle.Pen()
avery.forward(50)
avery.right(90)
avery.forward(20)
kate.left(90)
kate.forward(100)
jacob = turtle.Pen()
jacob.left(180)
jacob.forward(80)
Не забывайте, что каждый раз при создании черепашки с помощью 
turtle.Pen()в программе возникает новый самостоятельный объ-ект. Каждый из таких объектов принадлежит к классу Pen, и для каж-дого из них мы можем вызывать одни и те же функции.
'''
'''
your_age = input('Введите ваш возраст: ')
age = float(your_age)
if age > 13:
	print('Вы на %s лет старше, чем положено' % (age - 13))
'''
creature_list = ['единорог', 'циклоп', 'фея', 'эльф', 'дракон', 
'тролль']
print(len(creature_list))


fruit = ['яблоко', 'банан', 'клементин', 'питайя']
length = len(fruit)
for x in range(0, length):
	print('фрукт с индексом%s: %s' % (x, fruit[x]))

strings = 'строкаСТРОКА'
print(max(strings))

guess_this_number = 561
player_guesses = [12, 15, 70, 45]
if max(player_guesses) > guess_this_number:
	print('Бабах! Вы проиграли')
else:
	print('Вы победили')

a = abs(10) + abs(-10)
print(a)
b = abs(-10) + -10
print(b)
print()

harry = Animal('гиппогриф', 6, 'розовый')
class Animal:
	def __init__ (self, species, number_of_legs, color):
		self.species = species
		self.number_of_legs = number_of_legs
		self.color = color
import copy
harry = Animal('gippogrif', 6, 'pushti')
harriet = copy.copy(harry)
		print(harry.species)
		print(harry.species)

