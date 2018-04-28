board = []
for i in range(3):
	board.append(["*"] * 3)
#a function that creats the board
def print_board(board):
	for row in board:
		print (" ".join(row))
print("Let\'s play Tic Tac Toe! the rules are simple. you, the players, is given two choices: the row and column of your symbol. note that the numbers are between 0 and 2 and not 1 and 3. have fun!")
print(print_board(board))

#tg=he game itself
for turn in range(1,10):
	print("turn number: " + str(turn))
	#for every odd turn there will be x turn and for every even there will be o turn. thats because the X player alwayes start
	if turn == 1 or turn % 2 == 1:
		print ("X turn")
		X_col = int(input("choose row: "))
		X_row = int(input("choose column: "))
		# if given a number bigger than 2 or smaller than 0, you will lose a turn
		if (X_col > 2 or X_col < 0 or X_row > 2 or X_row < 0):
			print("oops, that not even on the board")
			print(print_board(board))
			turn = turn + 1
		# same goes for picking the same spot or someone else's same spot again
		
		elif board[X_row][X_col] == "X" or board[X_row][X_col] == "O":
			print("you have already played that spot or someone else did. try again")
			print(print_board(board))
		else:
			board[X_row][X_col] = "X"
			
			print(print_board(board))
		turn = turn + 1
	else:
		print("O turn")
		O_col = int(input("choose row: "))
		O_row = int(input("choose column: "))
		if (O_col > 2 or O_col < 0 or O_row > 2 or O_row < 0):
			print("oops, that not even on the board")
			print(print_board(board))
			turn = turn + 1
		elif board[O_row][O_col] == "X" or board[O_row][O_col] == "O":
			print("you have already played that spot or someone else did. try again")
			print(print_board(board))
		else:
			board[O_row][O_col] = "O"
			print(print_board(board))
		turn = turn + 1
		#win conditions
		#left row winner
	if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X":
			x = "winner"
			print("the winner is X")
			break;
		#middle row winner
	elif board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X":
			x = "winner"
			print("the winner is X")
			break;
		#right row winner
	elif board[2][0] == "X" and board[2][1] == "X" and board[2][2]=="X":
			x = "winner"
			print("the winner is X")
			break;
		#top column winner
	elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
			x = "winner"
			print("the winner is X")
			break;
		#middle column winner
	elif board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
			x = "winner"
			print("the winner is X")
			break;
		#bottom line winner
	elif board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
			x = "winner"
			print("the winner is X")
			break;
		#left crossover winner
	elif board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
			x = "winner"
			print("the winner is X")
			break;
			
	elif board[2][0] == "X" and board[1][1] == "X" and board[0][2] == "X":
			x = "winner"
			print("the winner is X")
			break;
			
		#middle row winner	
	if board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O":
			o = "winner"
			print("the winner is O")
			break;
		#right row winner
	elif board[2][0] == "O" and board[2][1] == "O" and board[2][2]=="O":
			o = "winner"
			print("the winner is O")
			break;
		#top column winner
	elif board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":
			o = "winner"
			print("the winner is O")
			break;
		#middle column winner
	elif board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O":
			o = "winner"
			print("the winner is O")
			break;
		#bottom column winner
	elif board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O":
			o = "winner"
			print("the winner is O")
			break;
		#left crossover winner
	elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
			o = "winner"
			print("the winner is O")
			break;
		#right crossover winner
	elif board[2][0] == "O" and board[1][1] == "O" and board[0][2] == "O":
			o = "winner"
			print("the winner is O")
			break;
	#the most logical condition - a tie
	if turn == 9:
		print("It\'s a Tie!")
		break;

