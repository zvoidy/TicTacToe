class xo:
  #for marking inside table
  def __init__(self):
  
    self.board = [' '] * 10
  
  #skull of board
  def display_board(self):
    print("-------------")
    print("|",self.board[7],"|",self.board[8],"|",self.board[9],"|")
    print("-------------")
    print("|",self.board[4],"|",self.board[5],"|",self.board[6],"|")
    print("-------------")
    print("|",self.board[1],"|",self.board[2],"|",self.board[3],"|")
    print("-------------")

  #for empty position
  def checkposition(self,value):
    if self.board[value]==" ":
      return True
    else:
      print("Choosen already!")

  #winning check
  def check(self):    
      global Game
  
      #Horizontal winning condition    
      if(self.board[1] == self.board[2] and self.board[2] == self.board[3] and self.board[1] != ' '):    
          Game="win"   
      elif(self.board[4] == self.board[5] and self.board[5] == self.board[6] and self.board[4] != ' '):    
          Game="win"   
      elif(self.board[7] == self.board[8] and self.board[8] == self.board[9] and self.board[7] != ' '):    
          Game="win"   
      #Vertical Winning Condition    
      elif(self.board[1] == self.board[4] and self.board[4] == self.board[7] and self.board[1] != ' '):    
          Game="win"  
      elif(self.board[2] == self.board[5] and self.board[5] == self.board[8] and self.board[2] != ' '):    
          Game="win"     
      elif(self.board[3] == self.board[6] and self.board[6] == self.board[9] and self.board[3] != ' '):    
          Game="win"   
      #Diagonal Winning Condition    
      elif(self.board[1] == self.board[5] and self.board[5] == self.board[9] and self.board[5] != ' '):    
          Game="win"     
      elif(self.board[3] == self.board[5] and self.board[5] == self.board[7] and self.board[5] != ' '):    
          Game="win"

      #to check for draw
      elif(self.board[1]!=" " and self.board[2]!=" " and self.board[3]!=" " and self.board[4]!=" " and self.board[5]!=" " and self.board[6]!=" " and self.board[7]!=" " and self.board[8]!=" " and self.board[9]!=" "):
        Game="draw"


game=xo()
#main game code
Game="running"
player=1
while Game=="running":
  game.display_board()
  if (player%2==0):
    print("Player 2's chance!")
    mark="O"
  else:
    print("Player 1's chance!")
    mark="X"

  value=int(input("Enter a position from 1 to 9: "))
  print()
  if (game.checkposition(value)):
    game.board[value]=mark
    player+=1
    game.check()

#code after win
game.display_board()
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
