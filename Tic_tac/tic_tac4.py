# tic tac game
# for loop in python
#first ask question.

# create game map 
# use 0 as spaces 
# 1 and 2 as x and o 
# grid of game
# case 1 
'''
game = [ [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0],]

print(" 0  1  2")

count = 0
for row in game:
	print(count, row)
	count += 1

# second stage of game


game = [ [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0],]

print("   a  b  c")


for count, row in enumerate(game):
	print(count, row)

# In this part we make a slice throgh the game to input the values.




game = [ [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0],]

game[0][1] = 3



print("   a  b  c")
for count, row in enumerate(game):
 	print(count, row)

# build function to print the game every time to display game map.


'''


game = [ [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0],]


def game_board():
	print("   a  b  c")
	for count, row in enumerate(game):
 		print(count, row)

game[1][0] = 1
 
