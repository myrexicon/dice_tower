import random

def dice_tower(type = int(input("How many sides do your dice have? \n> "))):
	i = 0
	end = []
	if type in [4, 6, 8, 10, 12, 20, 100]:
		num = int(input("How many dice do you want to roll? \n> "))
		if type == 4:
			while i<num:
				end.append(random.randint(1, 4))
				i += 1
		elif type == 6:
			while i<num:
				end.append(random.randint(1, 6))
				i += 1
		elif type == 8:
			while i<num:
				end.append(random.randint(1, 8))
				i += 1
		elif type == 10:
			while i<num:
				end.append(random.randint(1, 10))
				i += 1
		elif type == 12:
			while i<num:
				end.append(random.randint(1, 12))
				i += 1
		elif type == 20:
			while i<num:
				end.append(random.randint(1, 20))
				i += 1
		elif type == 100:
			while i<num:
				end.append(random.randint(1, 100))
				i += 1
	else:
		print("Your dice does not exist! Restart!")
		return dice_tower(type = int(input("How many sides do your dice have? \n> ")))

	print(end)

dice_tower()