# IMPORT BLOCK BEGIN
import copy
import random
import time

# IMPORT BLOCK END


# FUNCTION BLOCK BEGIN
def main():
    WIDTH = 60
    HEIGHT = 20
    LIVINGCELL = "#"
    DEADCELL = " "

    # Create a list of lists for the cells
    nextCells = []

    for xCell in range(WIDTH):
        column = []
        for yCell in range(HEIGHT):
            if random.randint(0, 1) == 0:
                column.append(LIVINGCELL) # Add a living cell to the column list
            else:
                column.append(DEADCELL) # Add a dead cell
        nextCells.append(column) # Append the cells to the board after they have been populated

    while True:
        print("\n\n\n\n\n") # Separate each step with newlines
        currentCells = copy.deepcopy(nextCells) # Grab the current board set as a new, separate instance

        # Print the current cells on screen
        for yCoord in range(HEIGHT):
            for xCoord in range(WIDTH):
                print(currentCells[xCoord][yCoord], end="")
            print()

        # Calculate the next step's cells based on the current step's cells
        for xCoord in range(WIDTH):
            for yCoord in range(HEIGHT):
                # Get neighboring coordinates
                leftCoord = (xCoord - 1) % WIDTH
                rightCoord = (xCoord + 1) % WIDTH
                aboveCoord = (yCoord - 1) % HEIGHT
                belowCoord = (yCoord + 1) % HEIGHT

                # Count the number of living neighbors
                numNeighbors = 0

                # CLEANUP: Figure out a way to better organize this block; the iteration of the IFs feels chunky
                if currentCells[leftCoord][aboveCoord] == LIVINGCELL:
                    numNeighbors += 1 # Top left neighbor is alive
                if currentCells[xCoord][aboveCoord] == LIVINGCELL:
                    numNeighbors += 1 # Top neighbor is alive
                if currentCells[rightCoord][aboveCoord] == LIVINGCELL:
                    numNeighbors += 1 # Top right neighbor is alive
                if currentCells[leftCoord][yCoord] == LIVINGCELL:
                    numNeighbors += 1 # Left neighbor is alive
                if currentCells[rightCoord][yCoord] == LIVINGCELL:
                    numNeighbors += 1 # Right neighbor is alive
                if currentCells[leftCoord][belowCoord] == LIVINGCELL:
                    numNeighbors += 1 # Bottom left neighbor is alive
                if currentCells[xCoord][belowCoord] == LIVINGCELL:
                    numNeighbors += 1 # Bottom neighbor is alive
                if currentCells[rightCoord][belowCoord] == LIVINGCELL:
                    numNeighbors += 1 # Bottom right neighbor is alive

                # Set cell based on Conway's Game of Life rules:
                if currentCells[xCoord][yCoord] == LIVINGCELL and (numNeighbors == 2 or numNeighbors == 3):
                    nextCells[xCoord][yCoord] = LIVINGCELL # Living cells with 2 or 3 neighbors stay alive ('Survive')
                elif currentCells[xCoord][yCoord] == DEADCELL and numNeighbors == 3:
                    nextCells[xCoord][yCoord] = LIVINGCELL # Dead cells with exactly 3 neighbors becomes alive ('Thrive')
                else:
                    nextCells[xCoord][yCoord] = DEADCELL # All other situations lead to a cell dying ('Die')
        time.sleep(1)
# FUNCTION BLOCK END


if __name__ == '__main__':
    main()
