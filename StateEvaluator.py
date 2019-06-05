from config import EMPTYCELL
from config import BLACKCELL
from config import WHITECELL
from state import State
from MovesGenerator import MovesGenerator


def is_gameover(state):
    obj = MovesGenerator()
    is_over = True
    is_over = is_over and not obj.getNextStates(state)
    state.reverse_State()
    is_over = is_over and not obj.getNextStates(state)
    state.reverse_State()
    return is_over


def evaluate(state, oppColor=WHITECELL):
    white_Counter = 0
    black_Counter = 0
    for row in state.board:
        for col in row:
            if (col == BLACKCELL):
                black_Counter += 1
            if (col == WHITECELL):
                white_Counter += 1
    # wa always play as black
    if(oppColor == WHITECELL):
        return black_Counter - white_Counter
    else:
        return white_Counter - black_Counter
