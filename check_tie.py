def check_tie(board):
	board_size = len(board)
	for row in range(board_size):
		for col in range(board_size):
			if board[row][col] == ' ':
				return True

	return False
