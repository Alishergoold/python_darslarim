'''def testfunc(myname):
	print('salom, %s' % myname)
	testfunc('Ali')

def testfunc(fname, lname):
	print('Привет, %s %s' % (fname, lname))
	testfunc('Мэри', 'Смит')

def silly_age_joke():
	print('Сколько вам лет?')
age = int(sys.stdin.readline())
if age >= 10 and age <= 13:
	print('13 + 49 + 84 + 155 + 97: что получится?', 'Головная боль!')
else:
	print('Что-что?')'''
'''
def my_vars():
	print('Global Variable:')
my_vars()

def greet_user():
	"""Выводит простое приветствие."""
	print("Hello!")
greet_user()

def greet_user(username):
	"""Выводит простое приветствие."""
	print("Hello, " + username.title() + "!")
greet_user('jesse')

def display_message():
	print("Message")
display_message()

def favorite_book():
	print("One of my favorite books is Alice in Wonderland")
favorite_book()

def describe_pet(pet_name, animal_type='dog'):
	"""Выводит информацию о животном."""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name='willie')

def spaceship_building(cans):
	total_cans = 0
	for week in range(1, 5):
		total_cans = total_cans + cans
		print('Неделя%s, банок: %s' % (week, total_cans))
spaceship_building(2)
print()

def car(coins):
	total_coins = 0
	for weeks in range(1, 10):
		total_coins = total_coins + coins
		print('Hafta%s, banka: %s' % (weeks, total_coins))
car(4)
print()

def olma(meva):
	meva_miqd = 0
	for hafta in range(1, 10):
		meva_miqd = meva_miqd + meva
		print('Hafta kuni %s, bonka kerak: %s' % (hafta, meva_miqd))
olma(2)
print()

def telefon(phone):
	colors_phone = 0
	for year in range(1, 50):
		colors_phone = colors_phone + phone
		print('haftada %s, ranglari: %s' % (year, colors_phone))
telefon(3)
print()

def myfunc():
	print("salom")
myfunc()
'''
'''
#COPY and deepopy MODUL
class Animal:
	def __init__(self, species, number_of_legs, color):
		self.species = species
		self.number_of_legs = number_of_legs
		self.color = color
import copy
harry = Animal('гиппогриф', 6, 'розовый')
harriet = copy.copy(harry)
print(harry.species)
print(harriet.species)
harry = Animal('гиппогриф', 6, 'розовый')
carrie = Animal('химера', 4, 'в зеленый горошек')
billy = Animal('богл', 0, 'узорчатый')
my_animals = [harry, carrie, billy]
more_animals = copy.copy(my_animals)
print(more_animals[0].species)
print(more_animals[1].species)
more_animals = copy.deepcopy(my_animals)
my_animals[0].species = 'дракон'
print()
print(my_animals[0].species)
print(more_animals[0].species)
'''
'''
class Car:
	def __init__(self, name, number_balon, colors):
		self.name = name
		self.number_balon = number_balon
		self.colors = colors
import copy
gm = Car('nexia', 4, 'pink')
gm_motors = copy.copy(gm)
print(gm.name)
print(gm_motors.colors)

gm = Car('nexia', 4, 'pink')
mers = Car('sclass', 2, 'black')
bmw = Car('X7', 0, 'skyblue')
my_cars = [gm, mers, bmw]
more_cars = copy.copy(my_cars)
print()
print(more_cars[0].name)
print(more_cars[1].name)
print(more_cars[2].colors)
print(more_cars[0].number_balon)

class Fruit:
	def __init__(self, names, colors, quantity):
		self.names = names
		self.colors = colors
		self.quantity = quantity
import copy
aple = Fruit('apple', 'green', 8)
peach = Fruit('peache', 'orange', 10)
chery = Fruit('cherry', 'red', 100) 
my_fruits = [aple, peach, chery]
more_fruit = copy.copy(my_fruits)
print(more_fruit[0].names)
print(more_fruit[1].colors)
print(more_fruit[2].quantity)
'''

'''#MODUL keyword
import keyword
print(keyword.iskeyword('if'))
print(keyword.iskeyword('ozwald'))
print(keyword.kwlist)'''

'''#RANDOM
import random
num = random.randint(1, 100)
while True:
    print('1 dan 100 gacha bo\'lgan sonni top')
    guess = input()
    i = int(guess)
    if i == num:
        print('To\'g\'ri')
        break
    elif i < num:
        print('Berilgaon son katta')
    elif i > num:
        print('Berilgan son kichik')'''

'''
#import sys
#sys.exit()

import sys
v = sys.stdin.readline(3)
#malumotni obyektga kiritamiz qo'shamiz
print(v)

import sys
sys.stdout.write('Shaxmat olamiz') #malumotni obyektdan chiqarish

import sys
print(sys.version)

import time
print(time.time())
'''
'''
import time
def lots_of_numbers(max):
	t1 = time.time()
	for x in range(0, max):
		print(x)
	t2 = time.time()
	print('%s sekund o\'tdi' % (t2-t1))
lots_of_numbers(1000)
'''
'''
import time
t = (2020, 2, 23, 10, 30, 48, 6, 0, 0)
print(time.asctime(t))
#Sun Feb 23 10:30:48 2020
'''

'''
import time
print(time.localtime()) #Hozirgi vaqtni o'zgaruvchilar bilan birga chiqarish

import time
t = time.localtime()
year = t[0]
month = t[1]
print(year)
#2020
print(month)
#2
'''

'''
import time
for x in range(1, 21):
	print(x)
	time.sleep(1) #sleep() har bir sekundda 1 sekund dam oladi
'''

import copy
class Car:
	pass
car1 = Car()
car1.wheels = 4
car2 = car1
car2.wheels = 3
print(car1.wheels)
car3 = copy.copy(car1)
car3.wheels = 6
print(car1.wheels)


