def print_board(board):
	board_size = len(board)
	for row in range(board_size):
		print('+---' * board_size + '+')
		for col in range(board_size):
			print('| ' + board[row][col] + ' ', end='')
		print('|')
	print('+---' * board_size + '+')
