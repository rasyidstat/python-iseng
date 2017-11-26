import random

# game simulation function
def diceroll_play(n, len_road, n_cp, dice, cp):
	# start parameters
	pos = [1] * n 			# starting position
	n_turn = 1				# starting turn
	winner = []				# winner
	player = list(map(lambda x: "player " + str(x), range(1, n + 1)))	# player

	while (pos != [len_road] * n) & (len(winner) != n-1):
		print("turn-" + str(n_turn))
		for i in range(len(pos)):
			if pos[i] < len_road:
				# roll dice
				print("player " + str(i+1) + " turn")
				roll = random.choice(dice)
				print("dice is " + str(roll))

				# move
				if (pos[i] + roll) > len_road:
					print("not move, almost there...")
				elif pos[i] == len_road:
					continue
				else:
					pos[i] = pos[i] + roll

				# win or not
				if pos[i] == len_road:
					print("player " + str(i+1) + " win the game!")
					winner += ["player " + str(i+1)]
					if len(winner) == n-1:
						print(list(set(player) - set(winner))[0] + " lose the game!")
						break
				else: 
					if i == 0:
						if pos[i] == pos[len(pos)-1] & pos[len(pos)-1] not in cp:
							pos[len(pos)-1] = max([cpl for cpl in cp if cpl < pos[len(pos)-1]])
							print("player " + str(i+1) + " kicks player " + str(len(pos)))
					else:
						if pos[i] == pos[i-1] & pos[i-1] not in cp:
							pos[i-1] = max([cpl for cpl in cp if cpl < pos[i-1]])
							print("player " + str(i+1) + " kicks player " + str(i))
		print(pos)
		n_turn += 1

	# print the summary
	print("Number of turns: " + str(n_turn))
	for i in range(len(winner)):
		print("winner " + str(i+1) + ": " + winner[i])

# input parameters
n = 4					# number of players
len_road = 100			# length of roads
n_cp = 10				# number of checkpoints
dice = [1,2,3,4,5,6]	# dice roll
cp = [1] + random.sample(list(map(lambda x: x+1, list(range(len_road))))[1:], n_cp) # random checkpoints

# start the game
print("safe place:")
print(cp)
diceroll_play(n, len_road, n_cp, dice, cp)





