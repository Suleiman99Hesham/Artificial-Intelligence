from config import EMPTYCELL
from config import BLACKCELL
from config import WHITECELL
from state import State
from MovesGenerator import MovesGenerator
from StateEvaluator import is_gameover
from StateEvaluator import evaluate
obj = MovesGenerator()
limit = 5


def minimax(state):
    global limit
    states = obj.getNextStates(state)
    if(states):
        return max(map(lambda state: [state, min_play(state, limit, state.whoDidThis)], states), key=lambda x: x[1])
    else:
        return (state, -1)


def min_play(state, limit, oppColor=BLACKCELL):
    limit -= 1
    if is_gameover(state) or limit <= 0:
        state_value = evaluate(state, oppColor)
        return state_value
    states = obj.getNextStates(state)
    if (states):
        return min(map(lambda state: max_play(state, limit, state.whoDidThis), states))
    else:
        state.reverse_State()
        return max_play(state, limit)


def max_play(state, limit, oppColor=BLACKCELL):
    limit -= 1
    if is_gameover(state) or limit <= 0:
        state_value = evaluate(state, oppColor)
        return state_value
    states = obj.getNextStates(state)
    if (states):
        return max(map(lambda state: min_play(state, limit, state.whoDidThis), states))
    else:
        state.reverse_State()
        return min_play(state, limit)
