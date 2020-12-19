'''
ukam = {
    'ism' : 'Rasul',
    'yosh': 24,
    'qayerda':'Riga'
}
print(f"Ukamning ismi {ukam['ism']} u hozirda {ukam['qayerda']}da, u talaba.")

otam = {'ismi':'mavlutdin', 'tyil':1954,'viloyat':'samarqand'}
tyil = otam['tyil']
vil = otam['viloyat']
print(f"Otamning ismi {otam['ismi'].title()}, {tyil}-yilda, {vil.title()} viloyatida tug'ilgan")


sevimli_taom = {
    'otam' : 'osh',
    'onam' : 'karam sho\'rva',
    'ayolim' : 'sho\'urma',
    'ukam' : 'qozon kabob',
    'singlim' : 'norin'
}
print(f"Otamning sevimli taomlari {sevimli_taom['otam']}.")
print(f"Onamning sevimli taomlari {sevimli_taom['onam']}.")
print(f"Ukamning sevimli taomi {sevimli_taom['ukam']}.")


python_izohli_lugati = {
    'variable' : 'o\'zgaruvchi',
    'list' : "ro'yxat",
    'tuple' : "o'zgarmas ro'yxat",
    'dictionary' : "lug'at",
    'if' : 'agar',
    'else' : 'aks holda',
    'integer' : 'butun son',
    'string' : 'qator',
    'float' : 'suzish',
    'true' : 'rost'
}
# print(python_izohli_lugati['tuple'])

kalit = input("Kalit so'z kiriting:").lower()
print(python_izohli_lugati.get(kalit,"Bunday so'z mavjud emas"))

kalit = input("Kalit so'z kiriting:").lower()
tarjima = python_izohli_lugati.get(kalit)
if tarjima==None:
    print("Bunday so'z mavjud emas")
else:
    print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")

# Lug'at bilan ishlash

talaba_0 = {
    'ism' : 'Bobur',
    'familiya' : 'Mamajonov',
    'kurs' : 3,
    'fakultet' : 'Suniy intelekt'
}
print(talaba_0.items())
for kalit, qiymat in talaba_0.items():
    print(f"Kalit: {kalit}")
    print(f"Qiymat: {qiymat} \n")
# for key, value in talaba_0.items():
#     print(f"Kalit: {key}")
#     print(f"Qiymat: {value} \n")



mashinalar = {
    'axror' : 'lacetti',
    'odil' : 'spark',
    'mirolim' : 'cobalt',
    "alisher" : 'malibu 2'
}
for k, v in mashinalar.items():
    print(f"{k.title()}ning mashinasi {v}.")




kitoblar = {
    "o'yla va boy bo'l" : 10000,
    "odamiylik mulki" : 20000,
    "iymon" : 100000
}
# for kitob in kitoblar.keys():  # == for kitob in kitoblar: keyni ikki xil usulda chiqarsak bo'ladi
#     print(kitob)
k_olish = ["vavilon", "stiv jobs", "durrotun nosixiyn"]
for kito in kitoblar:
    if kito in k_olish:
        print(f"{kito.title()} {kitoblar[kito]} so'm.")
for jovon in kitoblar:
    if jovon not in kitoblar:
        print(f"Iltimos {jovon} ham olib krling")



python_izoh_lug = {
    "Boolean" : "Mantiqiy qiymat",
    "Float" : "o'nlik son",
    "For" : "Tsikl",
    "Integer" : "Butun son",
    "If" : "Shart tekshirish",
    "List" : "Ro'yxat",
    "Dictionary" : "Lug'at",
    "Tuple" : "O'zgarmas ro'yxat"
}
for k, v in sorted(python_izoh_lug.items()):
    print(k, v)



dav_poytaxti = {
    "o'zbekiston" : "toshkent",
    "argentina" : "boynes-ayres",
    "rossiya" : "moskva",
    "latviya" : "riga",
    "germaniya" : "brussel",
    "afg'oniston" : "qobul",
    "turkiya" : "istanbul",
    "suriya" : "quddus",
    "polsha" : "varshava",
    "tojikiston" : "dushanbe",
}
for k, v in sorted(dav_poytaxti.items()):
    print(f"{k.title()}ning poytaxti {v.title()} shahri.")

poytaxt = input("Qaysi davlatning poytaxtini bilishni xoxlaysiz?: ")
capital = dav_poytaxti.get(poytaxt)
if capital == None:
    print("Bizda bu haqda ma'lumot yo'q")
else:
    print(f"{poytaxt.upper()}ning poytaxti {capital.title()} shahri.")




menu = {
    "somsa" : 5000,
    "osh" : 20000,
    "norin" : 21000,
    "frikadelki" : 18000,
    "qozon kabob" : 30000,
    "kabob" : 11000
}
print("3ta taom buyurtma bering: ")
buyurtmalar = []
for n in range(3):
    buyurtmalar.append(input(f"{n+1}-taomni nomini kiriting: ").lower())
for buyurtma in buyurtmalar:
    if buyurtma in menu:
        print(f"{buyurtma.title()} {menu[buyurtma]} so'm")
    else:
        print(f"Kechirasiz, bizda {buyurtma} yo'q.")   
    '''

malibus=[] # Malibu mashinalari uchun bo'sh ro'yxat yaratdik
for n in range(10):
    new_car = { # har bir yangi mashina uchun lug'at yaratamiz
        'model':'malibu',
        'rang':None, # rangi noaniq
        'yil':2020,
        'narh':None, # narhi belgilanmagan
        'km':0,
        'korobka':'avto'
        }
    malibus.append(new_car) # yangi lug'atni ro'yxatga qo'shamiz
for malibu in malibus[:3]:
    malibu['rang']='qizil'

for malibu in malibus[6:]: # ohirgi 4 ta mashinani
    malibu['rang']='qora'  # rangi qora
    malibu['korobka']='mexanika' # korobkasi mexanika
for malibu in malibus:
    if malibu['korobka']=='avto':
        malibu['narh']=40000
    else:
        malibu['narh']=35000
    print(malibu)


dasturchilar = {
    'ali':['python','c++'],
    'vali':['html','css','js'],
    'hasan':['php','sql'],
    'husan':['python','php'],
    'maryam':['c++','c#']
    }

for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
    for til in tillar:
        print(til.upper())


hamkasblar = {
    'ali':{'familiya':'valiyev',
           'tyil':1995,
           'malumot':'oliy',
           'tillar':['python','c++']
           },
    'vali':{'familiya':'aliyev',
            'tyil':2001,
            'malumot':"o'rta-maxsus",
            'tillar':['html', 'css', 'js']},
    'hasan':{'familiya':'husanov',
             'tyil':1999,
             'malumot':'maxsus',
             'tillar':['python','php']}
    }

    for ism, info in hamkasblar.items():
        print(f"\n{ism.title()} {info['familiya'].title()}, "
          f"{info['tyil']}-yilda tug'ilgan. "
          f"Ma'lumoti: {info['malumot']}. \n"
          "Quyidagi dasturlash tillarini biladi:")
    for til in info['tillar']:
        print(til.upper())