#print("Operator + ", 25+5)
#print("Operator - ", 25-5)
#print("Operator / ", 25/5)
#print("Operator * ", 25*5)

#print("Operator % ", 25%6)    #qoldiq chiqarish
#print("Operator // ", 25//6)  #Bo'linganda butun sonni chiqaradi
#print("Operator ** ", 2**3)   #sonni darajaga ko'taradi 2ni 3chi darajasi

#a = 25
#a = a+5
#print("a = ", a)

#b = 25
#b +=5
#print("b = ", b)

#DASTUR
# 1kg Limon a so'm b tiyin
#a = int(input("so'm: "))
#b = int(input("tiyin: "))
#n = int(input("Kg: "))
#c = n * ((a*100) + b)
#print("Umumiy so'm: ", c // 100)
#print("Umumiy tiyin: ", c % 100)

#Dastur
#a = 935
#b = 930
#c = int(a) - int(b)
#print(c)

# limon 1kg a so'm b tiyin. 5kg necha so'm necha tiyin
#a=3000.20
#b=int(input("Necha kg limon olmoqchisiz " ))
#c=a*b
#print(c)

#a = int(input("Tug'ilgan yilingiz "))
#b = int(input("Tug'ilgan kuningiz "))
#c = int(input("Hozirgi yilni kiriting "))
#d = int(input("Hozirgi kunni kiriting "))
#natija = ("Sizning yoshingiz ", int(c)-int(a)," yosh ", int(b)-int(d), " kun.")
#print(natija)

#format()
#len

"""
x = 45j
y = "35"
print(type(x))
print(type(y))
"""

found_coins = 20
magic_coins = 10
stolen_coins = 3
print(found_coins + magic_coins * 365 - stolen_coins * 52)
stolen_coins = 2
print(found_coins + magic_coins * 365 - stolen_coins * 52)

myscore = 1000
message = "Mening xisobim %s ochko"
print(message % myscore)

nums = 'Что сказало число %s числу %s? Славный поясок!'
print(nums % (0, 8))

print(10 * 'a')