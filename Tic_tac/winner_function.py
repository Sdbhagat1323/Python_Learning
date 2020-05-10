# Winner function


game = [ [0, 0, 1],
         [0, 1, 0],
         [1, 1, 0],]


def win(current_game):

	# Horizontal Winner
	for row in game:
		if row.count(row[0]) == len(row) and row[0] != 0:
			print(f"Player {row[0]} is the winner horizontaly!" )
	
	#Diagonal Winner 
	diags = []
	for col, row in enumerate(reversed(range(len(game)))):
		diags.append(game[row][col])
	if diags.count(diags[0]) == len(diags) and diags[0] != 0:
		print(f"Player {diags[0]} is the winner Diagonally(/)!" )
	
	#Diagonal Winner
	diags = []
	for ix in range(len(game)):
		diags.append(game[ix][ix])
	if diags.count(diags[0]) == len(diags) and diags[0] != 0:
		print(f"Player {diags[0]} is the winner Diagonaly2(\\)!" )	

	#Vertical Winner
	for col in range(len(game)):
		check = []
		for row in game:
			check.append(row[col])
		if check.count(check[0]) == len(check) and check[0] !=0:
			print(f"Player {check[0]} is the winner Vertically!" )


win(game)






