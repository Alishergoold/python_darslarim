"""
age = 25
if age > 20:
	print('Siz hali juda yoshsiz')

ag = 25
if ag > 20:
	print('Как-то вы староваты!')
	print('Что вы здесь делаете?')
	print('Почему не стрижете газон или не перекладываете бумажки?')

ages = 10
if ages >= 10:
	print('Вы слишком стары для моих шуток!')

agse = 10
if agse == 10:
	print('Что нельзя съесть на завтрак? Обед и ужин!')
	print()
	print("Хотите услышать грязную шутку?")

aged = 8
if aged == 12:
	print("Свинья шлепнулась в грязь!")
else:
	print("Тсс! Это секрет.")
	print()

svetafor = 3
if svetafor >= 5:
	print("Bu xato!")
elif svetafor == 3:
	print("To'g'ri javob")
elif svetafor < 2:
	print("No'to'g'ri javob")
else:
	print("Siz ikkiga o'qigansiz shekl No'to'g'ri")


ager = 12
if ager == 10:
 print("Что выйдет, если клюква наденет штаны?")
 print("Брюква!")
elif ager == 11:
 print("Что сказала зеленая виноградина синей виноградине?")
 print("Дыши! Дыши!")
elif ager == 12:
 print("Что сказал0 числу 8?")
 print("Привет, ребята!")
elif ager == 13:
 print("Что такое: на потолке сидит и хохочет?")
 print("Муха-хохотуха!")
else:
 print("Что-что?")

myval = None
if myval == None:
	print("В переменной myval ничего нет")

money = 2000
if money > 1000:
	print("Я богат!")
else:
	print("Я не богат!")
	print("Может, когда-нибудь потом…")


twinkies = 10
if twinkies >= 100:
	print("Slishkom mnogo")
elif twinkies <= 500:
	print("Slishkom malo")


print("Их слишком мно-го")
ninjas = 139
if ninjas >= 50 or ninjas >= 30:
	print("Будет непросто, но я с ними разделаюсь")
elif ninjas < 10:
	print("Это просто!")
elif ninjas < 30 or ninjas >= 10:
	print("Я одолею этих ниндзя!")

for m in range(1,5):
	print("Salom")

money = 999
if money > 3000:
	print("Juda qimmat")
elif money >= 2000 or money >= 1000:
	print("Arzon")
else:
	print("Zo'r")
print()

while n range()


b = 0
j = 0
d = 0

for number in range(100):
        import random
        Player1 = random.randint(1, 6)
        Player2 = random.randint(1, 6)

        if (Player1<Player2):
                b=b+1

        elif (Player1>Player2):
                j=j+1
        else:
                d=d+1

print("ALISHER", b)
print("SARVAR", j)
print("DURRANG", d)
"""
'''
import math, re  # re raqamlarni chiroyli ko'rsatadigan biblioteka

credit = 1100			 #kredit miqdori
percent = 1.04 			 # 4 %
ourmounthlypayment = 150 #oylik to'lanadigan summa
comission = 45			 #bankning uslugaga oladigan puli
totalpayment = 0
time = 0

for number in range(100):
	time += 1
	credit = (credit * percent) + comission - ourmounthlypayment
	totalpayment = totalpayment + ourmounthlypayment
	print('Cherez', time, '-mesyatsov my otdali banku', "{:,}".format(totalpayment), 
		'- dollarov. Dolga ostalos eshyo,', math.floor(credit), '- dollarov')
	if (credit * percent) + comission < ourmounthlypayment:
		print("Cherez", time + 1, '- mesyatsev my otdali banku', 
			"{:,}".format(math.floor((credit * percent) + comission + totalpayment)), '- dollarov, dolgo ostalos yeshyo 0', '- dollarov')
		break
'''









'''
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
	if car == 'gm':
		print(car.upper())
	else:
		print(car.title())

login = input("Loginni kiriting? ")
if login == 'admin':
	print("Xayr " + login + "!")
else:
	print("Xush kelibsiz, " + login + "!")


ism = input('Ismingiz nima?\n>>>') # Foydalanuvchi ismini so'raymiz
if ism.lower() != 'ali': # Agar ism Aliga teng bo'lmasa ...
    print(f"Uzr, {ism.title()} biz Alini kutayapmiz.") # quyidagi xabar chiqadi
else:
    print("Salom, Ali")

b_son = input("1-sonni kiriting")
i_son = input("2-sonni kiriting")
if b_son == i_son:
	print("Ikki son teng")
'''


"""
19/11/2020

Dasturlash asoslari

#10-dars: if/else

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""
'''
#Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
  if car=='gm':
    print(car.upper())
  else:
    print(car.title())

#Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring.
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
  if car!='gm':
    print(car.title())
  else:
    print(car.upper()) 

#Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. Aks xolda, "Xush kelibsiz, {foydalanuvchi_ismi}!" matnini konsolga chiqaring.
login = input("Login kiriting: ")
if login.lower() == 'admin':
  print("Xush kelibsiz Admin, foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
  print(f"Xush kelibsiz {login.title()}!")

#Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.
x = float(input("Birinchi sonni kiriting: "))
y = float(input("Ikkinchi sonni kiriting:"))
if x==y: print(f"Sonlar teng: {x}={y}")

#Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring.
son = float(input("Istalgan son kiriting:"))
print("Son manfiy") if son<0 else print("Son musbat")


#Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring. 
son = float(input('Istalgan son kiriting: '))
print(son**(1/2)) if son>0 else print('Musbat son kiriting')


yosh = int(input("Yoshingiz nechchida? "))
if yosh <= 4:
	print("Sizga kirish bepul")
elif yosh <= 12:
	print("Sizga kirish 5000 so'm")
elif yosh <= 18:
	print("Sizga kirish 8000 so'm")
else:
	print("Sizga kirish 15000 so'm")
# quyidagi qatorda yuqoridagi kodning kodning sodda ko'rinishi
yosh = int(input("Yoshingiz nechchida? "))
if yosh <= 4:
	narh = 0
elif yosh <= 12:
	narh = 5000
elif yosh <= 18:
	narh = 8000
else:
	narh = 10000
print(f"Sizhga kirish {narh} so'm")


kun = input("Bugun qaysi kun?>>> ")
if kun.lower()=='shanba' or kun.lower()=='yakshanba':
	print("Bugun dam olish kuni.")
else:
	print("Bugun ish kuni.")

# and operatorida ikkitomon TRUE qaytarishi kerak
kun = input("Bugun qaysi kun?>>> ")
harorat = float(input("Havo harorati qnaday? "))
if kun.lower()=='yakshanba' and harorat>=30:
	print("Cho'milgani ketdik")
elif kun.lower()=='yakshanba' and harorat<30:
	print("Uyda dam olamiz!!!")


# SODDA KOD
kun = input("Bugun qaysi kun?>>> ")
harorat = float(input("Havo harorati qanday? "))
if (kun.lower()=='yakshanba' or kun.lower()=='shanba') and harorat>=30:
	print("Cho'milgani ketdik")
elif (kun.lower()=='yakshanba' or kun.lower()=='shanba') and harorat<30:
	print("Uyda dam olamiz!!!") 


narh = 15000
choy = True
salat = False

if choy and salat:
	narh = narh + 10000
elif choy or salat:
	narh = narh + 5000
print(f"Jami: {narh} so'm")


narh = 10000 # nexianing narxi
balon = 0		# 0 == False
tuning = 1		# 1 == True
diska = True
signal = 1
tanirovka = False
if balon:
	print("Mijoz balon oldi.")
	narh = narh + 200
if tuning:
	print("Mijoz tuning qildiri.")
	narh = narh + 1000
if diska:
	print("Mijoz diska oldi.")
	narh = narh + 500
if signal:
	print("Mijoz signal oldi.")
	narh = narh + 50
if tanirovka:
	print("Mijoz tanirovka qidirdi.")
	narh = narh + 100
print("Jami "+str(narh)+" so'm bo'ldi.")


print("Sonni juft yoki toqligini tekshiramiz?")
son = float(input("Sonni kiriting: "))
if son%2:
	print("Bu son juft emas")
else:
	print("Rahmat!")
'''
'''
yosh = int(input("Yoshingiz nechchida: "))
if yosh < 4 or yosh >= 60:
	print("Sizga kirish bepul.")
elif yosh <= 18:
	print("Sizga kirish 10000 so'm.")
elif yosh > 18:
	print("Sizga kirish 20000 so'm.")



b_son = float(input("Birinchi sonni kiriting: "))
i_son = float(input("Ikkinchi sonni kiriting: "))
if b_son == i_son:
	print(f"{b_son} = {i_son}")
elif b_son > i_son:
	print(f"{b_son} > {i_son}")
else:
	print(f"{b_son} < {i_son}")

x = float(input("Birinchi sonni kiriting: "))
y = float(input("Ikkinchi sonni kiriting: "))
if x==y:
    print(f"{x}={y}")
elif x<y:
    print(f"{x}<{y}")
else:
    print(f"{x}>{y}")


mahsulotlar = ["non", "sut", "suv", "asal", "sariq yog'", "shokolad", "pechenya", 
"gugurt", "shag'am", "yog'"]
savat = []
for n in range(5):		
	savat.append(input(f"Savatga {n+1}-mahsulotni kiriting: "))
for savat in mahsulotlar:
	if savat in mahsulotlar:
		print(f"Do'konimizda {savat} bor")
	else:
		print(f"Do'konimizda {savat} yo'q")



mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)

if mavjud_emas:
  print(f"Do'konimizda quyidagi mahsulotlar yo'q:")
  for mahsulot in mavjud_emas:
    print(mahsulot)
else:
  print("Siz so'ragan barcha mahsulotlar do'konimizda bor")




son = float(input("Juft son kiriting: "))
if son%2!=0:
    print('Bu son juft emas.')
else:
    print("Rahmat!")


yosh = int(input("Yoshingiz nechida?"))
if yosh<=4 or yosh>=60:
    narh = 0
elif yosh < 18:
    narh = 10000
else:
    narh = 20000
print(f"Chipta {narh} so'm")


x = float(input("Birinchi sonni kiriting: "))
y = float(input("Ikkinchi sonni kiriting: "))
if x==y:
    print(f"{x}={y}")
elif x<y:
    print(f"{x}<{y}")
else:
    print(f"{x}>{y}")


mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)

if mavjud_emas:
  print("Do'konimizda quyidagi mahsulotlar yo'q:")
  for mahsulot in mavjud_emas:
    print(mahsulot)
else:
  print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
         
'''

users = ['alisher1983','aziza','yasina', 'umar']

login = input("Yangi login tanlang: ")

if login in users:
    print('Login band, yangi login tanalng!')
else: 
    print("Xush kelibsiz!")

son = int(input("Istalgan butun son kiriting: "))

for n in range(2,11):
    if not (son%n):
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")
