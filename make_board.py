def make_board(size):
	board = [None] * size
	for index in range(len(board)):
		board[index] = [' '] * size

	return board
