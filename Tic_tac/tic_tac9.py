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
'''


import itertools
from colorama import Fore, Back, Style, init
init()


def win(current_game):

   def all_same(l):
      if l.count(l[0]) == len(l) and l[0] != 0:
         return True
      else:
         return False
   # Horizontal Winner
   for row in game:
      if all_same(row):
         print(f"Player {row[0]} is the winner horizontaly!" )
         return True
   #Diagonal Winner 
   diags = []
   for col, row in enumerate(reversed(range(len(game)))):
      diags.append(game[row][col])
   if all_same(diags):
      print(f"Player {diags[0]} is the winner Diagonally(/)!" )
      return True
   #Diagonal Winner
   diags = []
   for ix in range(len(game)):
      diags.append(game[ix][ix])
   if all_same(diags):
      print(f"Player {diags[0]} is the winner Diagonaly2(\\)!" )  
      return True

   #Vertical Winner
   for col in range(len(game)):
      check = []
      for row in game:
         check.append(row[col])
      if all_same(check):
         print(f"Player {check[0]} is the winner Vertically!" )
         return True

   return False


def game_board(game_map,player=0, row=0, column=0, just_display=False):
   try: 
      if game_map[row][column] != 0:
         print("This position is occupited! choose another!")
         return game_map,  False
      print("   0  1  2")
      if not just_display:
         game[row][column] = player   
      for count, row in enumerate(game_map):
         colored_row = ""
         for item in row:
            if item == 0:
               colored_row += "   "
            elif item == 1:
               colored_row += Fore.GREEN + ' X ' + Style.RESET_ALL
            elif item == 2:
               colored_row += Fore.MAGENTA + ' O ' + Style.RESET_ALL

         print(count, colored_row)




      return game_map, True
   except IndexError as e:
      print("Error: Make sure you enter Proper Index 0, 1 & 3.", e)
      return game_map, False
   except Exception as e:
      print("Something went very wrong!", e)
      return game_map, False


play = True
players = [1, 2]
while play:
# display every time while playing game. this is reset the game.

   game =  [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

   game_won = False
   game, _ = game_board(game, just_display = True)
   player_choice = itertools.cycle([1, 2])
   while not game_won:# loop through the game of sepecific tik_tac game.unit the game won.
      current_player = next(player_choice)
      played = False
      while not played:
         print("current_player :", current_player)
         column_choice = int(input("What column do you want to play: "))
         row_choice = int(input("What row do you want to play: "))
         game, played = game_board(game, current_player, row_choice, column_choice)


      if win(game):
         game_won = True
         again = input("The game is over, would you like to play again? (y/n)")
         if again.lower() == "y":
            print("restarting")
         elif again.lower() == "n":
            print("Byeee")
            play = False
         else:
            print("Not a valid answers")
            play = False 
   #game_board(game_map=game, just_display=True)
   #print("move of player 1")

   #game_board(game_map=game_board, player=1, row=2, column=2,)

















