
#
# quoridor.py
# 
# @author    Alain Rinder
# @date      2017.05.28-06.02
# @version   0.1
# @note      Python version: 3.6.1 [recommended] - 3.5.0 [minimal: https://docs.python.org/3/library/typing.html]
#
# TODO: 
# OK Use GridCoordinates class instead of col/row
# OK Param graphical interface (disable draw functions...)
# OK Split source files
#    Handle exec params
# OK Check if fence placing will not block a player
# OK Create algorithms for path finding
#    BuilderBot: maximise other pawns path
# OK PERFORMANCE ISSUES: store valid fence placings, valid pawn moves with updates
# OK Check blocking fence using path without pawns (one path could exist but cannot be currently accessible because of a pawn) (DFS)
# OK Blocking fence checking failed on testing path with the future fence -> update valid pawn moves when appending fence in method isFencePlacingBlocking

from src.Settings          import *
from src.Game              import *
from src.player.Human      import *
from src.player.RandomBot  import *
from src.player.RunnerBot  import *
from src.player.BuilderBot import *
from src.player.My_Bot import *
from src.Path import *
from src.player.My_Bot1 import *
from src.GridCoordinates import *
from datetime import datetime

def main():
    """
    Main function of quoridor. 
    Create a game instance and launch game rounds.
    """
    startTime = datetime.now()
    game = Game([ # 2 or 4
        My_Bot("Justin"),
        #My_Bot1("Alain")
        #BuilderBot("Benoit"),
        #BuilderBot("Clément"),
        Human("Pierre")
        #RandomBot("Justin"),
        
        #RandomBot("Nick")
    ], totalFenceCount = 20, cols = 9, rows = 9)
    game.start(10) # rounds
    game.end()
    print(datetime.now() - startTime)
    global TRACE
    # print("TRACE")
    # for i in TRACE:
    # 	print("%s: %s" % (i, TRACE[i]))

main()
#top left of board is (0,0)
#bottom right is (8,8)
#if player 0 hits (8,:) they win 
#if player 1 hits (0,:) they win

#to find path end coords = self.endPositions for each player
