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


game = [ [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0],]


def game_board():
	print("   a  b  c")
	for count, row in enumerate(game):
 		print(count, row)

game[1][0] = 1

 update  game_board function to display the plan game board
without adding 0 0  position in game.

game = [ [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0],]


def game_board(player=0, row=0, column=0, just_display=False):
   print("   0  1  2")
   if not just_display:
      game[row][column] = player   
   for count, row in enumerate(game):
      print(count, row)

game_board(just_display=True)
#game[1][0] = 1
game_board(player=1,row=1,column=2)

# mutebility


game = [ [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0],]


def game_board(player=0, row=0, column=0, just_display=False):
   print("   0  1  2")
   if not just_display:
      game[row][column] = player   
   for count, row in enumerate(game):
      print(count, row)

game_board 








game = [ [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0],]


def game_board(player=0, row=0, column=0, just_display=False):
   print("   0  1  2")
   if not just_display:
      game[row][column] = player   
   for count, row in enumerate(game):
      print(count, row)

game_board(just_display=True)
#game[1][0] = 1
game_board(player=1,row=1,column=2)



Error Handling for python




game = [ [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0],]


def game_board(game_map,player=0, row=0, column=0, just_display=False):
   try: 
      print("   0  1  2")
      if not just_display:
         game[row][column] = player   
      for count, row in enumerate(game_map):
         print(count, row)
      return game_map
   except IndexError as e:
      print("Error: Make sure you enter Proper Index.", e)

   except Exception as e:
      print("Something went very wrong!", e)


game_board(game_map=game, just_display=True)
print("move of player 1")

game_board(game_map=game_board, player=1, row=2, column=2,)

Determine winner 
horizontaly
verticaly
diagonaly
'''



game = [ [0, 0, 0],
         [0, 0, 0],
         [0, 0, 0],]


def game_board(game_map,player=0, row=0, column=0, just_display=False):
   try: 
      print("   0  1  2")
      if not just_display:
         game[row][column] = player   
      for count, row in enumerate(game_map):
         print(count, row)
      return game_map
   except IndexError as e:
      print("Error: Make sure you enter Proper Index.", e)

   except Exception as e:
      print("Something went very wrong!", e)


def win(current_game):
   for row in game:
      print(row)
      
















