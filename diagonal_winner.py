def assert_equal(actual, expected): #function to check the result if actual matches with expected
	if actual == expected:
	    print("OK")
	else:
	    print(f"Error! {repr(actual)} != {repr(expected)}")

def diagonal_winner(board): #diagonal_winner function to check if any diagonal matches either with X or O
    result = False
    diagonal = ""
    for r in range(len(board)):
        diagonal += board[r][r]
    result = check_diagonal(diagonal)
    if result == True:
        return result
    diagonal = ""
    c = 0
    for r in range(len(board)-1,-1,-1):
        diagonal += board[r][c]
        c += 1
    result = check_diagonal(diagonal)
    if result == True:
        return result
    return result
    
def check_diagonal(diagonal): #function to check each diagonal and return True if every value of the diagonal matches or return False if it doesnt
    result = False
    for index in range(len(diagonal)-1):
        if diagonal[index] == '' or diagonal[index] == " ":
            return False
        else:
            if diagonal[index] == diagonal[index+1]:
                result = True
            else:
                return False
    return result



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