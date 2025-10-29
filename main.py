def assert_equal(actual, expected): #function to check the result if actual matches with expected
	if actual == expected:
	    print("OK")
	else:
	    print(f"Error! {repr(actual)} != {repr(expected)}")
		
def row_winner(board): #row_winner function to check if any row matches either with X or O
    result = False
    for index in range(len(board)):
        result = each_row_check(board[index])
        if result == True:
            return result
    return result

def each_row_check(row): #function to check each row and return True if every value of the row matches or return False if it doesnt
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

def column_winner(board): #column_winner function to check if any column matches either with X or O
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

def each_column_check(column): #function to check each column and return True if every value of the column matches or return False if it doesnt
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

#below are some outputs to check if my code is correct or not using assert_equal() function

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

assert_equal(
    diagonal_winner(
        [
            ['O', 'X', 'O', 'X'],
            [' ', 'O', 'X', ' '],
            ['X', 'X', ' ', 'X'],
            ['X', ' ', 'O', 'O']
        ]
    ),
    True
)
assert_equal(
    diagonal_winner(
        [
            ['X', 'X', ' '],
            ['X', ' ', 'O'],
            [' ', 'O', 'O']
        ]
    ),
    False
)