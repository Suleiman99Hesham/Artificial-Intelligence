from config import EMPTYCELL
from config import BLACKCELL
from config import WHITECELL


class State:
    def __init__(self, board, whoDidThis):
        self.board = []
        for row in board:
            self.board.append(list(row))
        self.whoDidThis = whoDidThis
        self.x = -1
        self.y = -1

    def reverse_State(self):
        self.whoDidThis = BLACKCELL if self.whoDidThis == WHITECELL else WHITECELL

    def generateID(self):
        tempId = "" + self.whoDidThis
        for row in board:
            for col in row:
                tempId += col
        self.id = tempId
        return self.id
