def assert_equal(actual, expected): #function to check the result if actual matches with expected
	if actual == expected:
	    print("OK")
	else:
	    print(f"Error! {repr(actual)} != {repr(expected)}")

def winner(board):
    return row_winner(board) or column_winner(board) or diagonal_winner(board)

def winning_line(strings):
    piece = strings[0]
    if piece == ' ':
        return False
    for entry in strings:
        if piece != entry:
            return False
    return True

def row_winner(board):
    for row in board:
        if winning_line(row):
            return True
    return False

def column_winner(board):
    for col in range(len(board[0])):
        column = []
        for row in board:
            column.append(row[col])
        if winning_line(column):
            return True
    return False

def diagonal_winner(board):
    diagonal1 = []
    diagonal2 = []
    for i in range(len(board)):
        diagonal1.append(board[i][i])
        diagonal2.append(board[i][-i-1])
    return winning_line(diagonal1) or winning_line(diagonal2)

assert_equal(
    winner(
        [
            ['X', 'X', 'X', ' '],
            ['X', 'X', ' ', ' '],
            ['X', ' ', 'O', 'X'],
            [' ', ' ', 'O', 'X']
        ]
    ),
    False
)
assert_equal(
    winner(
        [
            ['X', ' ', 'X'],
            ['O', 'X', 'O'],
            ['O', 'O', 'O']
        ]
    ),
    True
)
assert_equal(
    winner(
        [
            ['X', ' '],
            ['X', 'O']
        ]
    ),
    True
)