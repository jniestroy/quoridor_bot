import random

from src.player.IBot    import *
from src.action.IAction import * 
from src.Path import *

class Fence_bot(IBot):
    def play(self, board,opp_start) -> IAction:
        # 1 chance over 3 to place a fence
        #validFencePlacings = board.validFencePlacings()
        #want this to take in current player and opp coord
        #also new fence placement calc change in total steps remaining for both returns that
        