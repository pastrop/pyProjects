import sys
from random import randint

ROW = int(sys.argv[1])
COLUMN = int(sys.argv[2])
squares_with_bombs = 7
play_board = [[0] * COLUMN for i in range(ROW)]

print('I got {} rows, {} columns'.format(ROW, COLUMN) )

def my_game(size_row,size_column):
	game_board=[[0] * size_column for i in range(size_row)]
	for k in range(squares_with_bombs):
		row = randint(0,size_row-1)
		column = randint(0,size_column-1)
		game_board[row][column]='b'
	for r in range(size_row):
		for c in range(size_column):
			if game_board[r][c] == 'b' and r+1<size_row and c+1<size_column:
				print(game_board[r-1][c])
				if game_board[r-1][c] != 'b' and r-1>=0:
					game_board[r-1][c] += 1
				if game_board[r][c-1] != 'b' and c-1>=0:
					game_board[r][c-1] += 1
				if game_board[r][c+1] != 'b':
					game_board[r][c+1] += 1
				if game_board[r+1][c] != 'b':
					game_board[r+1][c] += 1
				if game_board[r+1][c+1] != 'b':
					game_board[r+1][c+1] += 1

	for row in game_board:
		print(row)
	return game_board

def my_play():
	row=ROW
	column=COLUMN
	while True:
		pass
		input = raw_input('enter coordinate pls:').split(',')
		print('your input', input)
		input_row=int(input[0])
		input_column=int(input[1])
		if input_row > row or input_column > column:
			print('out of bound')
			break
		if loaded_board[input_row][input_column] == 'b':
			print ('you are dead')
			break
		if loaded_board[input_row][input_column] != 0:
			play_board[input_row][input_column] = loaded_board[input_row][input_column]
			for row in play_board:
				print(row)




loaded_board = my_game(ROW,COLUMN)
my_play()