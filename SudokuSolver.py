def printing(matx):
	for i in range(9):
		for j in range(9):
			print(matx[i][j], end=" ")
		print()

def isSafe(matx, row, col, num):
	for x in range(9):
		if matx[row][x] == num:
			return False
	for x in range(9):
		if matx[x][col] == num:
			return False
	startRow = row - row % 3
	startCol = col - col % 3
	for i in range(3):
		for j in range(3):
			if matx[i + startRow][j + startCol] == num:
				return False
	return True

def solveSudoku(matx, row, col):
	if (row == 8 and col == 9):
		return True
	if col == 9:
		row += 1
		col = 0
	if matx[row][col] > 0:
		return solveSudoku(matx, row, col + 1)
	for num in range(1, 10, 1):
		if isSafe(matx, row, col, num):
			matx[row][col] = num
			if solveSudoku(matx, row, col + 1):
				return True
		matx[row][col] = 0
	return False

