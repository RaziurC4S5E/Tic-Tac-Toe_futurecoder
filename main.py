def assert_equal(actual, expected):
	if actual == expected:
	    print("OK")
	else:
	    print(f"Error! {repr(actual)} != {repr(expected)}")

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
