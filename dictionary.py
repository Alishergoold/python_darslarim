
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
    