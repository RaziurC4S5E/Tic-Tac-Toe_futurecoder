def assert_equal(actual, expected): #function to check the result if actual matches with expected
	if actual == expected:
	    print("OK")
	else:
	    print(f"Error! {repr(actual)} != {repr(expected)}")

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
