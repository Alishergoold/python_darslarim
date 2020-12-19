# ism = input("Ismingizni kiriting? ")
# yosh = input(f"Salom {ism.title()}! Yoshingiz nechchida? ")
# t_joy = input(f"{int(yosh)} yoshli {ism.title()} tug'ilgan joyingiz? ")


'''
kitob = input("Yaxshi ko'rgan kitoblaringiz nomini kiriting? ")
kitob += "\n Dasturdan chiqish uchun 'stop' deb yozing"
qiymat = ''
while qiymat != 'stop':
    qiymat = input(kitob)
    if qiymat != 'exit':
        print(qiymat)

son = 1
while son<=5:
    print(son, end=' ')
    son+=1

sonlar = 20
while sonlar<=30:
    print(sonlar, end='_')
    sonlar+=1

print("Sonni kvadratini hisoblash.")
savol = "Istalgan sonni kiriting: "
savol += f"\n(Dasturdan chiqish uchun 'exit' deb yozing.) "
qiymat = ''
while qiymat != 'exit':
    qiymat=input(savol)
    if qiymat != 'exit':
       natija = float(qiymat)**2
       print(f"{qiymat} ning kvadrati {natija} ga teng")
    elif qiymat == 'exit':
        print("Dastur tugadi.")
    else:
       qiymat == 0
       print(f"{qiymat} ning kvadrati 0")

# FLAG = ISHORA
print("Sonni kvadratini hisoblash.")
savol = "Istalgan sonni kiriting "
savol += f"(Dasturdan chiqish uchun 'exit' deb yozing.) : "
ishora = True   # ishora = flag
while ishora:
    qiymat = input(savol)
    if qiymat == 'exit':
        ishora = False
    else:
        print(float(qiymat)**2)

# BREAK = TO'XTATISH, BO'LISH
print("Sonni kvadratini hisoblash.")
savol = "Istalgan sonni kiriting "
savol += f"(Dasturdan chiqish uchun 'exit' deb yozing.) : "
while True:  # abadiy tsikl
    qiymat = input(savol)
    if qiymat == 'exit':
        break  # tdiklni to'xtatish
    else:
        print(float(qiymat)**2)




sonlar = list(range(1,11))
for son in sonlar:
    if son == 5:
        break
        
    print(f"{son} ning kvadrati {son**2} ga teng.")

sonlar = list(range(1,11))
for son in sonlar:
    if son == 5:
        continue  # qadam tashlaydi natijada 5 ning kvadrati natijasi yo'q
        
    print(f"{son} ning kvadrati {son**2} ga teng.")


son = 0
while son<10:
    son+=1
    if son%2 != 0:  # konsolga juft sonlarni chiqarish
    #if son%2 == 0:  # konsolga toq sonlarni chiqarish
        continue
    else:
        print(son)
'''

'''
#ABADIY TSIKLLAR INFINITY LOOP. 
son = 0
while son < 10:
    if son%2 != 0:
        continue
    else:
        print(son) # abadiy tsikldan chiqish ctrl+c

son = 0
while son < 10:
    if son%2 != 0:
        continue
    else:
        print(son)
    son+=1  #ctrl+c

son = 1
while son>0:
    if son%2 != 0:
        continue
    else:
        print(son)   #ABADIY TSIKLLAR INFINITY LOOP. 
'''



#AMALIYOT
'''
kitob = input("Yaxshi ko'rgan kitoblaringiz nomini kiriting? ")
kitob += "\n Dasturdan chiqish uchun 'stop' deb yozing"
qiymat = ''
while qiymat != 'stop':
    qiymat = input(kitob)
    if qiymat != 'exit':
        print(qiymat)


yosh = "Yoshingiz nechchida? "
yosh += "(Dasturdan chiqish uchun 'stop' yoki 'exit' deb yozing.) "
narx = ''
while narx != 'exit' and 'stop':
    narx = input(yosh)
    narx = int(narx)
    if narx < 7:
        print("7 yoshdan yoshlarga 2000 so'm.")
    elif narx <= 17:
        print("7-18 yoshgacha 3000 so'm")
    elif narx <= 65:
        print("18-65 yoshgacha 10000 so'm")
    else:
        print("65 yoshdan kattalarga bepul")



print("Kiritilgan sonning ildizini qaytaruvchi dastur.\n")
savol = "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
while True:
    qiymat = input(savol)
    qiymat = int(qiymat)
    if qiymat<0:
        continue
    elif qiymat=='Exit':
        break
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
'''

'''
#18 while ro'yxatlar bilan ishlash

print("Yaqin do'stlaringizni ro'yxatini tuzamiz.")
ismlar = []
n = 1
while True:
    savol = f"{n}-do'stingiz ismini kiriting: "
    ism = input(savol)
    ismlar.append(ism)
    takrorlash = input("Yana ism qo'shsangiz 'ha' aks holda 'yo\'q' deb yozing. ")
    n+=1
    if takrorlash != 'ha':
        break
print("Do'stlaringiz ro'yxati:")
for ism in ismlar:
    print(f"Sizning {ism.title()}ismli do'stingiz bor.")




print("Do'stlaringiz yoshini saqlaymiz.")
dostlar = {}
ishora = True
while ishora:
    ism = input("Do'stingizni ismini kiriting: ")
    yosh = input(f"{ism.title()}ning yoshini kiriting.")
    dostlar[ism] = int(yosh) # ism kalit (key), yosh qiymat(value)
    javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q) ")
    if javob == "yo'q":
        ishora = False
for ism, yosh in dostlar.items():
    print(f"{ism.title()} {yosh} yoshda")


cars = ['lacetti', 'nexia', 'tico', 'nexia', 'damas', 'lacetti', 'nexia']
while 'nexia' in cars: # toki nexia cars ro'yxati ichida ekan...
    cars.remove('nexia')  # nexiani ro'yxatdan o'chirgin
print(cars)



mevalar = ['olma', 'banan', 'nok', 'xurmo']
narxli_mevalar = {}
while mevalar:
    meva = mevalar.pop()
    narx = input(f"{meva.title()} ning narxini kiriting: ")
    print(f"{meva.title()} {narx} so'mga narxlandi.")
    narxli_mevalar[meva] = narx 
print(narxli_mevalar)


print("Buyurtma berishingiz mumkin: "
) 
buyurtmalar = []
n = 1
while True:
    f_buyurtma = f"{n}-buyurtmangizni bering: "  
    buyurtma = input(f_buyurtma)
    buyurtmalar.append(buyurtma)
    qoshimcha_b = input("Yana buyurtmaga qo'shsangiz 'ha' qo'shmasangiz yo'q deb yozing. ")
    n+=1
    if qoshimcha_b != 'ha':
        break
print("Buyurtmalaringiz ro'yxati: ")
for buyurtma in buyurtmalar:
    print(f"Siz {buyurtma}ni buyurtma qildingiz.") 




print("Do'kondan xarid qiladigan maxsulotlaringiz ro'yxati. ")
maxsulotlar = {}
while True:
    maxsulot = input("Maxsulot nomini kiriting: ")
    narx = input(f"{maxsulot.title()}ning narxini kiriting: ")
    maxsulotlar[maxsulot] = narx
    javob = input("Yana maxsulot qo'shasizmi? (ha/yo'q) ")
    if javob != "ha":
        break


buyurtmalar = ['olma', 'banan', 'nok', 'xurmo']
maxsulotlar = {
    'olma' : 10000,
    'piyoz' : 4000,
    'banan' : 20000,
    'kartoshka' : 5000
}

while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in maxsulotlar.keys():
        narx = maxsulotlar[buyurtma]
        print(f"{buyurtma.title()} - {narx} so'm")
    else:
        print(f"Bizda {buyurtma} yo'q.")

'''


