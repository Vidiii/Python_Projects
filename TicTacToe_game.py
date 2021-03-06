board = [" "]*9
game_still_going = True
winner = None
current_player = "X"

def display_board():
  print(board[0] + " | " + board[1] + " | " + board[2] )
  print("---------")
  print(board[3] + " | " + board[4] + " | " + board[5] )
  print("---------")
  print(board[6] + " | " + board[7] + " | " + board[8] )

def play_game():
  display_board()
  player = input("Player 1, choose your character: X or O : \n")
  global current_player
  current_player = player
  while game_still_going:
    handle_turn(current_player)  
    check_if_gameover()  
    flip_player()

  if winner=="X" or winner == "O":
    print("CONGRATULATION!! " + winner + "won")
  elif winner == None:
    print("Looks like its a TIE!!")
  
def handle_turn(player):
  print(player + "'s turn.")  
  position = input("Choose a position from 1-9 where you want to play: ")
  valid = False
  while not valid:
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Choose position from 1-9: ")
    position = int(position)-1
    if board[position]==" ":
      valid = True
    else:
      print("You cannot go there, choose another position: ")
  board[position] = player
  display_board()

def check_if_gameover():
  check_for_winner()
  check_if_tie()

def check_for_winner():
  global winner
  row = check_rows()
  col = check_columns()
  dia = check_diagonals()
  if row:
    winner = row
  elif col:
    winner = col
  elif dia:
     winner = dia
  else:
    winner = None
  return

def check_rows():
  global game_still_going
  row1 = board[0] == board[1] == board[2] != " "
  row2 = board[3] == board[4] == board[5] != " "
  row3 = board[6] == board[7] == board[8] != " " 
  if row1 or row2 or row3:
    game_still_going = False
  if(row1):
    return board[0]
  elif row2:
    return board[3]
  elif row3:
    return board[6]
  return

def check_columns():
  global game_still_going
  col1 = board[0] == board[3] == board[6] != " "
  col2 = board[1] == board[4] == board[7] != " "
  col3 = board[2] == board[5] == board[8] != " " 
  if col1 or col2 or col3:
    game_still_going = False
  if(col1):
    return board[0]
  elif col2:
    return board[3]
  elif col3:
    return board[6]
  return
    
def check_diagonals():
  global game_still_going
  dia1 = board[0] == board[4] == board[8] != " "
  dia2 = board[2] == board[4] == board[6] != " "
  if dia1 or dia2:
    game_still_going = False
  if(dia1):
    return board[0]
  elif dia2:
    return board[2]
  return

def check_if_tie():
  global game_still_going
  if " " not in board:
    game_still_going = False
  return

def flip_player():
  global current_player
  if current_player == "X":
    current_player = "O"
  elif current_player == "O":
    current_player = "X"
  return

play_game()
