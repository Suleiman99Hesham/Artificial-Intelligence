from config import EMPTYCELL
from config import BLACKCELL
from config import WHITECELL
from state import State


class MovesGenerator:
    def getNextStates(self, state):
        states = []
        r = -1

        # we work on the empty cell we move from the empty cells and check if we can go through it
        # to right or to left or up or bottom or either the way is
        for row in state.board:
            r += 1
            c = -1
            for cell in row:
                c += 1

                if(cell != EMPTYCELL):
                    continue

                # to right
                stateTemp = self.movesRight(state, r, c, state.whoDidThis)
                if(stateTemp == None):
                    stateTemp = state

                # to left
                stateTemp1 = self.movesLeft(stateTemp, r, c, state.whoDidThis)
                if(stateTemp1 == None):
                    stateTemp1 = stateTemp

                # to bottom
                stateTemp = self.movesBottom(
                    stateTemp1, r, c, state.whoDidThis)
                if(stateTemp == None):
                    stateTemp = stateTemp1

                # to top
                stateTemp1 = self.movesTop(stateTemp, r, c, state.whoDidThis)
                if(stateTemp1 == None):
                    stateTemp1 = stateTemp

                # to top left
                stateTemp = self.movesTopLeft(
                    stateTemp1, r, c, state.whoDidThis)
                if(stateTemp == None):
                    stateTemp = stateTemp1

                # to top right
                stateTemp1 = self.movesTopRight(
                    stateTemp, r, c, state.whoDidThis)
                if(stateTemp1 == None):
                    stateTemp1 = stateTemp

                # to bottom left
                stateTemp = self.movesBottomLeft(
                    stateTemp1, r, c, state.whoDidThis)
                if(stateTemp == None):
                    stateTemp = stateTemp1

                # to bottom right
                stateTemp1 = self.movesBottomRight(
                    stateTemp, r, c, state.whoDidThis)
                if(stateTemp1 == None):
                    stateTemp1 = stateTemp

                # append the next state
                if(stateTemp1 != None and stateTemp1.board != state.board):
                    stateTemp1.x = r
                    stateTemp1.y = c
                    states.append(stateTemp1)

        return states

    def movesRight(self, inputState: State, row, column, oppColor):

        # check if it's not at the right
        rowLen = len(inputState.board[row])
        if(column + 1 >= rowLen):
            return None

        # get My color and the opponent color
        myColor = BLACKCELL if oppColor == WHITECELL else WHITECELL

        # check if it has the oppColor at its right
        if(inputState.board[row][column+1] != oppColor):
            return None

        # copy board to get the next state in a new object
        state = State(inputState.board, myColor)

        # change this cell with myColor
        state.board[row][column] = myColor
        column += 1

        # loop to right and change every cell to myColor
        while(column < rowLen and state.board[row][column] == oppColor):
            state.board[row][column] = myColor
            column += 1

        # check that there's another cell like me at the other side
        if(column < rowLen and state.board[row][column] == myColor):
            return state

        # if there's no cells like me return None
        return None

    def movesLeft(self, inputState: State, row, column, oppColor):

        # check if it's not at the left
        if(column <= 0):
            return None

        # get My color and the opponent color
        myColor = BLACKCELL if oppColor == WHITECELL else WHITECELL

        # check if it has the oppColor at its left
        if(inputState.board[row][column-1] != oppColor):
            return None

        # copy board to get the next state in a new object
        state = State(inputState.board, myColor)

        # change this cell with myColor
        state.board[row][column] = myColor
        column -= 1

        # loop to left and change every cell to myColor
        while(column >= 0 and state.board[row][column] == oppColor):
            state.board[row][column] = myColor
            column -= 1

        # check that there's another cell like me at the other side
        if(column >= 0 and state.board[row][column] == myColor):
            return state

        # if there's no cells like me return None
        return None

    def movesBottom(self, inputState: State, row, column, oppColor):

        numOfRows = len(inputState.board)

        # check if it's not at the bottom
        if(row + 1 >= numOfRows):
            return None

        # get My color and the opponent color
        myColor = BLACKCELL if oppColor == WHITECELL else WHITECELL

        # check if it has the oppColor under it
        if(inputState.board[row+1][column] != oppColor):
            return None

        # copy board to get the next state in a new object
        state = State(inputState.board, myColor)

        # change this cell with myColor
        state.board[row][column] = myColor
        row += 1

        # loop to bottom and change every cell to myColor
        while(row < numOfRows and state.board[row][column] == oppColor):
            state.board[row][column] = myColor
            row += 1

        # check that there's another cell like me at the other side
        if(row < numOfRows and state.board[row][column] == myColor):
            return state

        # if there's no cells like me return None
        return None

    def movesTop(self, inputState: State, row, column, oppColor):

        # check if it's not at the top
        if(row <= 0):
            return None

        # get My color and the opponent color
        myColor = BLACKCELL if oppColor == WHITECELL else WHITECELL

        # check if it has the oppColor above it
        if(inputState.board[row-1][column] != oppColor):
            return None

        # copy board to get the next state in a new object
        state = State(inputState.board, myColor)

        # change this cell with myColor
        state.board[row][column] = myColor
        row -= 1

        # loop to top and change every cell to myColor
        while(row >= 0 and state.board[row][column] == oppColor):
            state.board[row][column] = myColor
            row -= 1

        # check that there's another cell like me at the other side
        if(row >= 0 and state.board[row][column] == myColor):
            return state

        # if there's no cells like me return None
        return None

    def movesTopLeft(self, inputState: State, row, column, oppColor):

        # check if it's not at the top left
        if(row <= 0 or column <= 0):
            return None

        # get My color and the opponent color
        myColor = BLACKCELL if oppColor == WHITECELL else WHITECELL

        # check if it has the oppColor at the top left
        if(inputState.board[row-1][column-1] != oppColor):
            return None

        # copy board to get the next state in a new object
        state = State(inputState.board, myColor)

        # change this cell with myColor
        state.board[row][column] = myColor
        row -= 1
        column -= 1

        # loop to top left and change every cell to myColor
        while(row >= 0 and column >= 0 and state.board[row][column] == oppColor):
            state.board[row][column] = myColor
            row -= 1
            column -= 1

        # check that there's another cell like me at the other side
        if(row >= 0 and column >= 0 and state.board[row][column] == myColor):
            return state

        # if there's no cells like me return None
        return None

    def movesTopRight(self, inputState: State, row, column, oppColor):

        rowLen = len(inputState.board[row])

        # check if it's not at the top right
        if(row <= 0 or column + 1 >= rowLen):
            return None

        # get My color and the opponent color
        myColor = BLACKCELL if oppColor == WHITECELL else WHITECELL

        # check if it has the oppColor at the top right
        if(inputState.board[row-1][column+1] != oppColor):
            return None

        # copy board to get the next state in a new object
        state = State(inputState.board, myColor)

        # change this cell with myColor
        state.board[row][column] = myColor
        row -= 1
        column += 1

        # loop to top right and change every cell to myColor
        while(row >= 0 and column < rowLen and state.board[row][column] == oppColor):
            state.board[row][column] = myColor
            row -= 1
            column += 1

        # check that there's another cell like me at the other side
        if(row >= 0 and column < rowLen and state.board[row][column] == myColor):
            return state

        # if there's no cells like me return None
        return None

    def movesBottomLeft(self, inputState: State, row, column, oppColor):

        numOfRows = len(inputState.board)

        # check if it's not at the bottom left
        if(row + 1 >= numOfRows or column <= 0):
            return None

        # get My color and the opponent color
        myColor = BLACKCELL if oppColor == WHITECELL else WHITECELL

        # check if it has the oppColor at the bottom left
        if(inputState.board[row+1][column-1] != oppColor):
            return None

        # copy board to get the next state in a new object
        state = State(inputState.board, myColor)

        # change this cell with myColor
        state.board[row][column] = myColor
        row += 1
        column -= 1

        # loop to bottom left and change every cell to myColor
        while(row < numOfRows and column >= 0 and state.board[row][column] == oppColor):
            state.board[row][column] = myColor
            row += 1
            column -= 1

        # check that there's another cell like me at the other side
        if(row < numOfRows and column >= 0 and state.board[row][column] == myColor):
            return state

        # if there's no cells like me return None
        return None

    def movesBottomRight(self, inputState: State, row, column, oppColor):
        rowLen = len(inputState.board[row])
        numOfRows = len(inputState.board)

        # check if it's not at the bottom right
        if(row + 1 >= numOfRows or column+1 >= rowLen):
            return None

        # get My color and the opponent color
        myColor = BLACKCELL if oppColor == WHITECELL else WHITECELL

        # check if it has the oppColor at the bottom right
        if(inputState.board[row+1][column+1] != oppColor):
            return None

        # copy board to get the next state in a new object
        state = State(inputState.board, myColor)

        # change this cell with myColor
        state.board[row][column] = myColor
        row += 1
        column += 1

        # loop to bottom right and change every cell to myColor
        while(row < numOfRows and column < rowLen and state.board[row][column] == oppColor):
            state.board[row][column] = myColor
            row += 1
            column += 1

        # check that there's another cell like me at the other side
        if(row < numOfRows and column < rowLen and state.board[row][column] == myColor):
            return state

        # if there's no cells like me return None
        return None
