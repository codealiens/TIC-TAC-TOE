def print_board(board):
	board_size = len(board)
	for count in range(board_size):
		print('+---' * board_size + '+')
		for count2 in range(board_size):
			print('| ' + board[count][count2] + ' ', end='')
		print('|')
	print('+---' * board_size + '+')
