'''import random
Player1 = random.randint(1, 6)
Player2 = random.randint(1, 6)
print("Alisher", Player1)
print("Sarvar", Player2)

if (Player1<Player2):
    print("Player2 WIN!!!")
elif (Player1>Player2):
    print("Player1 WIN!!!")
else:
    print("DRAW")
'''
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