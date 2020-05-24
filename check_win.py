def check_win(board, mark):
	# check horizontally for win
	for row in range(len(board)):
		for col in range(len(board)):
			if board[row][col] != mark:
				break

		if board[row][col] == mark:
			return True

	# check vertically for win
	for col in range(len(board)):
		for row in range(len(board)):
			if board[row][col] != mark:
				break

		if board[row][col] == mark:
			return True

	# check positively sided diagonal for win
	for row in range(len(board)):
		col = row
		if board[row][col] != mark:
			break

	if board[row][col] == mark:
		return True

	# check negetively sided diagonals for win
	row = 0
	column = len(board) - 1
	for row in range(len(board)):
		for col in range(len(board) - 1, 0, -1):
			if board[row][column] != mark:
				break

	if board[row][col] == mark:
		return True

	return False
