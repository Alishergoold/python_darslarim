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