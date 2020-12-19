'''
car0 = {
        'model':'lacetti',
        'rang':'oq',
        'yil':2018,
        'narh':13000,
        'km':50000,
        'korobka':'avtomat'
        }

car1 = {
        'model':'nexia 3',
        'rang':'qora',
        'yil':2015,
        'narh':9000,
        'km':89000,
        'korobka':'mexanika'
        }

car2 = {
        'model':'gentra',
        'rang':'qizil',
        'yil':2019,
        'narh':15000,
        'km':20000,
        'korobka':'mexanika'
        }

# car = car0
# print(f"{car['model'].title()},\
#   {car['rang']} rang,\
#   {car['yil']}-yil, {car['narh']}$")
# car = car1
# print(f"{car['model'].title()},\
#   {car['rang']} rang,\
#   {car['yil']}-yil, {car['narh']}$")
# car = car2
# print(f"{car['model'].title()},\
#   {car['rang']} rang,\
#   {car['yil']}-yil, {car['narh']}$")  


cars = [car0, car1, car2]
for car in cars:
    print(f"{car['model'].title()}, " f"{car['rang']} rang, "
          f"{car['yil']}-yil, {car['narh']}$")

print(cars[1])
print(cars[2]["narh"])
print(f"{cars[0]['rang'].title()} "
      f"{cars[0]['model']}")




meva0 = {
    "nomi" : "olma",
    "rangi" : "yashil",
    "narxi" : 5000,
    "soni" : 30,
    "tami" : "nordon"
}
meva1 = {
    "nomi" : "gilos",
    "rangi" : "qizil",
    "narxi" : 20000,
    "soni" : 40,
    "tami" : "shirin"
}
meva2 = {
    "nomi" : "nok",
    "rangi" : "sariq",
    "narxi" : 8000,
    "soni" : 30,
    "tami" : "shirin"
}

mevalar = [meva0, meva1, meva2]
for meva in mevalar:
    print(f"{meva['nomi'].title()} soni {meva['soni']} ta, " f"Narxi {meva['narxi']} so'm")

print(mevalar[1])       # meavalar listidagi 1-indexli dictionaryni chiqarish chiqarish
print(mevalar[2]['narxi'])          # meavalardagi 2-indexli elementni narxini chiqarish    
print(f"Rangi {mevalar[0]['rangi'].upper()}"
    f" ta'mi {mevalar[0]['tami']}." ) # meavalardagi 0-indexli elementni rangini chiqarish
print()
print()


kuchuklar = []
for n in range(10):
    new_animal = { # har bir yangi hayvon uchun lug'at yaratamiz
        'nomi' : 'bobik',
        'turi'  : 'it',
        'rang' : None,
        'oyoq' : 4,
        'yil' : None,    # t_yili belgilanmagan
        'narh' :  None   # narhi belgilanmagan o'zimiz kiritamiz
        }
    kuchuklar.append(new_animal)  # yangi lug'atni(dictionary) ro'yxatga qo'shamiz
for kuchuk in kuchuklar[:3]: # 3-indeksli elementgacha ranglarni kulranga o'zgartirdik
    kuchuk['rang'] = 'kulrang'

for kuchuk in kuchuklar [4:8]:
    kuchuk['yil'] = 2018
    kuchuk['narh'] = 150000

for kuchuk in kuchuklar [8:]:
    kuchuk['nomi'] = 'chapa'

for kuchuk in kuchuklar:
    if kuchuk['yil']==2018:
        kuchuk['narh']=40000
    else:
        kuchuk['narh']=35000

    print(kuchuk)



zargarlar = {
    'jamshid' : ['shtamp', 'uzuk'],
    'axror' : ['pachoq', 'uzuk'],
    'odil'  : ['komplekt', 'arqon'],
    'alisher' : ['komplekt', 'nikoh uzuk']
}

for key, value in zargarlar.items():
    print(f"\n{key.title()} quyidagi buyumlarni yasashni biladi: ")
    for buyum in value:
        print(f'{buyum.upper()} ', end='') # end=''printdan so'ng qator tashamaydi



kursdoshlar = {
    'odil' : {
        'familiya' : 'alimjonov',
        'tyil' : 1990,
        'malumot' : 'orta maxsus',
        'kasbi'  : ['zargarlik', 'sotuvchilik']
    },
    'jamshid' : {
        'familiya' : 'zaynuddinov',
        'tyil' : 1990,
        'malumot' : 'orta maxsus',
        'kasbi'  : ['zargarlik', 'haydovlik']
    },
    'ibrat' : {
        'familiya' : 'alimov',
        'tyil' : 1990,
        'malumot' : 'orta maxsus',
        'kasbi'  : ['zargarlik', 'fermerlik']        
    } 
}
for ism, info in kursdoshlar.items():
    print(f"\n{ism.title()}, {info['familiya'].title()}, "
      f"{info['tyil']}-yilda tug'ilgan. \n"
      f"Ma'lumoti: {info['malumot']}. \n" "Quyidagi kasblarni biladi: ")
for kasb in info['kasbi']:
    print(kasb.upper(), end='')



shaxs1 = {
    'ism' : 'Abu Abdulloh Muhammad ibn Ismoil',
    'tyil': 810,
    'tjoy': 'buxoro',
    'kasbi' : 'hadisshunoslik',
    'mashxur_a' : ['al-jome as-sahih', 'al-adab al-mufrad']
}
shaxs2 = {
    'ism': 'stiv jobs',
    'tyil' : 1955,
    'tjoy' : 'usa',
    'kasbi': 'ixtirochi',
    'mashxur_a' : ['stiv jobs', 'millioner']
}
shaxs3 = {
    'ism' : 'ozodbek nazarbekov',
    'tyil': 1972,
    'tjoy': 'andijon',
    'kasbi': 'vazir',
    'mashxur_a' : ['madaniyat', 'kuchalar']
}
shaxs4 = {
    'ism' : 'alisher navoiy',
    'tyil' : 1441,
    'tjoy' : 'xirot',
    'kasbi': 'adabiyotshunos',
    'mashxur_a' : ['xamsa', 'lison ut-tayr']
}

mashxurlar = [shaxs1, shaxs2, shaxs3, shaxs4]
# for shaxs in mashxurlar:
#     print(f"{shaxs['ism'].title()} {shaxs['tyil']}-yilda {shaxs['tjoy'].upper()}da tug'ilgan. " )

for shaxs in mashxurlar:
    ism = shaxs['ism']
    asarlar = shaxs['mashxur_a']
    print(f"\n{ism.title( )} ning mashxur asarlari")
    for asar in asarlar:
        print(asar.title())
   


kinolar = {
    'ali':['Terminator','Rambo','Titanic'],
    'vali':['Tenet','Inception','Interstellar'],
    'hasan':['Abdullajon','Bomba','Shaytanat'],
    'husan':['Mahallada duv-duv gap','John Wick']
    }

for ism, kinolar in kinolar.items():
    print(f"\n{ism.title()}ning sevimli kinolari: ")
    for kino in kinolar:
        print(kino)

animals = {
    'bobik':['sevginator', 'uyin'],
    'chapa':['bublik', 'bethoven'],
    'pupsik':['miami', 'germany']
    }
for key, value in animals.items():
    print(f"\n{key.title()}ning sevimli filmlari. ")
    for animal in value:
        print(animal)

'''
   
   
   
davlatlar = {
    'uzb' : {
        'nomi' : 'uzbekiston',
        'poytaxt' : 'toshkent',
        'maydoni' : 448978,
        'aholi' : 34500000,
        'pul_birligi' : 'sum'
    },
    'rossiya' : {
        'nomi' : 'rossiya',        
        'poytaxt' : 'moskva',
        'maydoni' : 448978,
        'aholi' : 114500000,
        'pul_birligi' : 'rubl'        
    },
    'usa' : {
        'nomi' : 'united states america',
        'poytaxt' : 'vashington',
        'maydoni' : 12_448_978,
        'aholi' : 254_500_000,
        'pul_birligi' : 'dollar'        
    },
    'malayziya' : {
        'nomi' : 'malayziya',
        'poytaxt' : 'kuala-lumpur',
        'maydoni' : 848_978,
        'aholi' : 250_000_000,
        'pul_birligi' : 'ringit'        
    }
}
for davlat, info in davlatlar.items():
    if davlat.lower() == 'usa':
        davlat = davlat.upper()
    else:
        davlat = davlat.capitalize()
    print(f"\n{davlat}ning poytaxti {info['poytaxt'].title()}"
        f"\nHududi: {info['maydoni']} kv.km."
        f"\nAholisi: {info['aholi']} kishi."
        f"\nPul birligi: {info['pul_birligi']}")

