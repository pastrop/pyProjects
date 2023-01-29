import sys

class TicTac:
	def __init__(self,tocken):
		self.tocken=tocken

	def print_gameboard(self, board):
		for row in board:
			pr_row='|'.join(row)
			print(pr_row)

	def create_board(self):
		game_board=[['-'] * 3 for i in range(3)]
		self.print_gameboard(game_board)
		return game_board

	def add_tocken(self,row, column, tocken, board):
		# print('row-{},column-{},tocken-{}'.format(row, column,tocken))
		board[row][column]=self.tocken
		self.print_gameboard(board)
		return board


if __name__ == "__main__":

	row = int(sys.argv[1])
	column = int(sys.argv[2])
	tocken = sys.argv[3]
	
	myclass=TicTac(tocken)
	my_board=myclass.create_board()
	myclass.add_tocken(row,column,tocken,my_board)

			
