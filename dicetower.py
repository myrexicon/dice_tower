import random

def dice_tower(num = int(input("How many sides do your dice have? \n> "))):
	i = 0
	end = []
	if num in [4, 6, 8, 10, 12, 20, 100]:
		type = int(input("How many dice do you want to roll? \n> "))
		if num == 4:
			while i<type:
				end.append(random.randint(1, 4))
				i += 1
		elif num == 6:
			while i<type:
				end.append(random.randint(1, 6))
				i += 1
		elif num == 8:
			while i<type:
				end.append(random.randint(1, 8))
				i += 1
		elif num == 10:
			while i<type:
				end.append(random.randint(1, 10))
				i += 1
		elif num == 12:
			while i<type:
				end.append(random.randint(1, 12))
				i += 1
		elif num == 20:
			while i<type:
				end.append(random.randint(1, 20))
				i += 1
		elif num == 100:
			while i<type:
				end.append(random.randint(1, 100))
				i += 1
	else:
		print("Your dice does not exist! Restart!")
		return dice_tower(num = int(input("How many sides do your dice have? \n> ")))

	print(end)

dice_tower()