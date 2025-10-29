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
