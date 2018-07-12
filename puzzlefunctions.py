
#check if empty space is on an edge
def isOnEdge(markX, markY):
	if markX > 0 and markX < 3 and markY > 0 and markY < 3:
		return False
	else:
		return True
#find numbers that are eligable to use
def whatCanMove(markX, markY, grid):
	canMoveUp = True
	canMoveDown = True
	canMoveLeft = True
	canMoveRight = True
	numbersThatCanMove = []
	#determine which ways you can move from the empty mark
	if isOnEdge(markX, markY):
		#find out what edge
		if markX == 0:
			canMoveUp = False
		if markX == 3:
			canMoveDown = False
		if markY == 0:
			canMoveLeft = False
		if markY == 3:
			canMoveRight = False

	#check available slots and see what number is in them
	if canMoveUp:
		numbersThatCanMove.append(grid[markX-1][markY])
	if canMoveDown:
		numbersThatCanMove.append(grid[markX+1][markY])
	if canMoveLeft:
		numbersThatCanMove.append(grid[markX][markY-1])
	if canMoveRight:
		numbersThatCanMove.append(grid[markX][markY+1])

	#return the list of numbers that can move
	return numbersThatCanMove


def choiceInWhatCanMove(markX, markY, grid, choice):
	avail = whatCanMove(markX, markY, grid)
	for thing in avail:
		if int(choice) == int(thing):
			return True

#changing the location of the empty space with that of the choice and viceversa
def switch(choiceX, choiceY, markX, markY, grid):
	tempChoice = grid[choiceX][choiceY]
	tempMark = grid[markX][markY]
	grid[choiceX][choiceY] = tempMark
	grid[markX][markY] = tempChoice