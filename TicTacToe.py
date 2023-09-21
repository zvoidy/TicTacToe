#for marking inside table
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']    

#skull of board
def display_board():
  print("-------------")
  print("|",board[7],"|",board[8],"|",board[9],"|")
  print("-------------")
  print("|",board[4],"|",board[5],"|",board[6],"|")
  print("-------------")
  print("|",board[1],"|",board[2],"|",board[3],"|")
  print("-------------")

#for empty position
def checkposition(value):
  if board[value]==" ":
    return True
  else:
    print("Choosen already!")

#winning check
def check():    
    global Game
  
    #Horizontal winning condition    
    if(board[1] == board[2] and board[2] == board[3] and board[1] != ' '):    
        Game="win"   
    elif(board[4] == board[5] and board[5] == board[6] and board[4] != ' '):    
        Game="win"   
    elif(board[7] == board[8] and board[8] == board[9] and board[7] != ' '):    
        Game="win"   
    #Vertical Winning Condition    
    elif(board[1] == board[4] and board[4] == board[7] and board[1] != ' '):    
        Game="win"  
    elif(board[2] == board[5] and board[5] == board[8] and board[2] != ' '):    
        Game="win"     
    elif(board[3] == board[6] and board[6] == board[9] and board[3] != ' '):    
        Game="win"   
    #Diagonal Winning Condition    
    elif(board[1] == board[5] and board[5] == board[9] and board[5] != ' '):    
        Game="win"     
    elif(board[3] == board[5] and board[5] == board[7] and board[5] != ' '):    
        Game="win"

    #to check for draw
    elif(board[1]!=" " and board[2]!=" " and board[3]!=" " and board[4]!=" " and board[5]!=" " and board[6]!=" " and board[7]!=" " and board[8]!=" " and board[9]!=" "):
      Game="draw"



#main game code
Game="running"
player=1
while Game=="running":
  display_board()
  if (player%2==0):
    print("Player 2's chance!")
    mark="O"
  else:
    print("Player 1's chance!")
    mark="X"

  value=int(input("Enter a position from 1 to 9: "))
  print()
  if (checkposition(value)):
    board[value]=mark
    player+=1
    check()

#code after win
display_board()
player-+1
while (Game=="win"):
  if(player%2==0):
    print("Game won by player 1")
    break
  else:
    print("Game won by player 2")
    break

#code after draw
while (Game=='draw'):
  print("Game Draw!")
  break
















