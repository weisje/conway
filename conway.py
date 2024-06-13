# IMPORT BLOCK BEGIN
import copy
import random
import time

# IMPORT BLOCK END


# FUNCTION BLOCK BEGIN
def main():
    WIDTH = 60
    HEIGHT = 20

    # Create a list of lists for the cells
    nextCells = []

    for xCell in range(WIDTH):
        column = []
        for yCell in range(HEIGHT):
            if random.randint(0, 1) == 0:
                column.append('#') # Add a living cell to the column list
            else:
                column.append(' ') # Add a dead cell
        nextCells.append(column) # Append the cells to the board after they have been populated

    while True:
        print("\n\n\n\n\n") # Separate each step with newlines
        currentCells = copy.deepcopy(nextCells) # Grab the current board set as a new, separate instance

        # Print the current cells on screen
        for yCoord in range(HEIGHT):
            for xCoord in range(WIDTH):
                print(currentCells[xCoord][yCoord], end="")
            print()


# FUNCTION BLOCK END


if __name__ == '__main__':
    main()
