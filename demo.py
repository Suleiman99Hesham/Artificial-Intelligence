from config import EMPTYCELL
from config import BLACKCELL
from config import WHITECELL
from state import State
from MovesGenerator import MovesGenerator
from MinimaxAlgorithm import minimax
from StateEvaluator import is_gameover
from StateEvaluator import evaluate

state = State(
    [
        [BLACKCELL, WHITECELL, BLACKCELL, BLACKCELL,
            BLACKCELL, WHITECELL, BLACKCELL, BLACKCELL],
        [BLACKCELL, WHITECELL, BLACKCELL, WHITECELL,
            BLACKCELL, WHITECELL, BLACKCELL, BLACKCELL],
        [BLACKCELL, WHITECELL, WHITECELL, WHITECELL,
            WHITECELL, EMPTYCELL, BLACKCELL, BLACKCELL],
        [BLACKCELL, WHITECELL, WHITECELL, EMPTYCELL,
            WHITECELL, WHITECELL, BLACKCELL, BLACKCELL],
        [BLACKCELL, WHITECELL, WHITECELL, WHITECELL,
            WHITECELL, WHITECELL, BLACKCELL, BLACKCELL],
        [BLACKCELL, WHITECELL, EMPTYCELL, WHITECELL,
            BLACKCELL, WHITECELL, BLACKCELL, BLACKCELL],
        [BLACKCELL, WHITECELL, BLACKCELL, BLACKCELL,
            BLACKCELL, WHITECELL, BLACKCELL, BLACKCELL],
        [BLACKCELL, WHITECELL, BLACKCELL, BLACKCELL,
            BLACKCELL, WHITECELL, BLACKCELL, BLACKCELL],
    ], WHITECELL)

print(f"Input: ")
print("x: " + str(state.x) + " , Y: " + str(state.y))
for row in state.board:
    print(row)
print("\n")

s = (state, -1)
while(input("To go to the next one press any key to exit write e") != 'e'):
    s = minimax(s[0])
    if(s[0].x == -1 and s[0].y == -1):
        print(
            f"Player didn't have a play")
        continue
    print(
        f"Player {s[0].whoDidThis} played as he estimates to get {-s[1]} more points at the end:  ")
    print("x: " + str(s[0].x) + " , Y: " + str(s[0].y))
    for row in s[0].board:
        print(row)
    print("\n")
    if(is_gameover(s[0])):
        print(f"Game Finished player 1 get {evaluate(s[0])}")
        print(f"Game Finished player 2 get {evaluate(s[0],BLACKCELL)}")
        break
