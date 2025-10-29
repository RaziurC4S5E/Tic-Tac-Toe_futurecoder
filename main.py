def assert_equal(actual, expected):
	if actual == expected:
	    print("OK")
	else:
	    print(f"Error! {repr(actual)} != {repr(expected)}")
		
def row_winner(board):
    result = False
    for index in range(len(board)):
        result = each_row_check(board[index])
        if result == True:
            return result
    return result

def each_row_check(row):
    result = False
    for index in range(len(row)-1):
        if row[index] == '' or row[index] == " ":
            return False
        else:
            if row[index] == row[index+1]:
                result = True
            else:
                return False
    return result

def column_winner(board):
    result = False
    column = ""
    for r in range(len(board)):
        for c in range(len(board)):
            column += board[c][r]
        result = each_column_check(column)
        if result == True:
            return result
        column = ""
    return result

def each_column_check(column):
    result = False
    for index in range(len(column)-1):
        if column[index] == '' or column[index] == " ":
            return False
        else:
            if column[index] == column[index+1]:
                result = True
            else:
                return False
    return result

assert_equal(
    row_winner(
        [
            ['A', 'A', 'B', 'A'],
            [' ', ' ', ' ', ' '],
            ['A', ' ', ' ', 'A'],
            ['B', ' ', 'B', 'A']
        ]
    ),
    False
)

assert_equal(
    row_winner(
        [
            ['X', ' ', 'X'],
            ['O', 'X', 'X'],
            ['O', 'O', 'O']
        ]
    ),
    True
)

assert_equal(
    column_winner(
        [
            ['X', 'O', ' '],
            ['X', 'O', ' '],
            ['O', 'X', ' ']
        ]
    ),
    False
)

assert_equal(
    column_winner(
        [
            ['X', 'O', ' ', 'X'],
            [' ', 'O', 'X', 'O'],
            ['O', 'O', 'X', 'X'],
            ['O', 'O', 'X', ' ']
        ]
    ),
    True
)
