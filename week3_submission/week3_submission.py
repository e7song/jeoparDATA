def display_grid(grid):
    print("+--------+")
    print("  ", end = "")
    for i in range(3):
        print(f' {i}', end = "")
    print("")
    for r in range(3):
        print(f' {r} ', end = "")
        for c in range(3):
            print(grid[r][c], end = " ")
        print("")
    print("+--------+")

def victory_checker(grid, player):
	# check rows
	for r in range(3):
		if grid[r][0] == player and grid[r][1] == player and grid[r][2] == player:
			return f"Player {player} wins!"
	# check columns
	for c in range(3):
		if grid[0][c] == player and grid[1][c] == player and grid[2][c] == player:
			return f"Player {player} wins!"
	# check diagonals
	if grid[0][0] == player and grid[1][1] == player and grid[2][2] == player:
		return f"Player {player} wins!"
	if grid[-1][0] == player and grid[-2][1] == player and grid[-3][2] == player:
		return f"Player {player} wins!"

	return "Continue"

def make_move(grid, player):
	move_made = False
	print(f'Player {player} to move:')
	while not move_made:
		try:
			r, c = input().split(" ")
			r, c= int(r), int(c)
		except:
			print("Invalid Move: Try Again")
			continue
		if r in [0, 1, 2] and c in [0, 1, 2]:
			if grid[r][c] == '-':
				grid[r][c] = player
				move_made = True
			else:
				print("Invalid Move: Try Again")
		else:
			print("Invalid Move: Try Again")



def run_game():
	print("Welcome to tic-tac-toe!")
	print("The input format is: r c")
	print("This represents a coordinate for each player to place their piece on")

	# backend
	grid = [["-"] * 3 for _ in range(3)]
	move_count = 0
	game_end = False

	x_win = False

	while move_count < 9:
		display_grid(grid)
		if move_count % 2 == 0: # player x to move
			make_move(grid, 'x')
			status = victory_checker(grid, 'x')
			if status == 'Continue':
				move_count += 1
			else:
				display_grid(grid)
				print(status)
				game_end = True
				x_win = True
				break
		else: # player y to move
			make_move(grid, 'y')
			status = victory_checker(grid, 'y')
			if status == 'Continue':
				move_count += 1
			else:
				display_grid(grid)
				print(status)
				game_end = True
				break
	if game_end == False:
		display_grid(grid)
		if input("It's a tie. Try again? [y/n] ") == 'y':
			run_game()

	if game_end and x_win:
		f = open('scoreboard.csv', 'r+')
		curr = f.read()
		if curr == '': # empty, no header
			f.write('player_win\n')
		f.write('x\n')
		f.close()

	else:
		f = open('scoreboard.csv', 'r+')
		curr = f.read()
		if curr == '': # empty, no header
			f.write('player_win\n')
		f.write('y\n')
		f.close()

if __name__ == "__main__":
	run_game()