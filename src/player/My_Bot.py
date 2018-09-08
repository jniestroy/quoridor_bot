import random

from src.player.IBot    import *
from src.action.IAction import * 
from src.Path import *
from src.GridCoordinates import *


class My_Bot(IBot):
    def play(self, board,opp_coord) -> IAction:
        # 1 chance over 3 to place a fence
        #validFencePlacings = board.validFencePlacings()
        possible_fence = []
        # for coord_fence in board.storedValidFencePlacings:
        #     if board.isFencePlacingBlocking(coord_fence) == 0:
        #         r = (-(board.Fence_Distance(coord_fence)),coord_fence)
        #         possible_fence.append(r)

        if  self.remainingFences() > 0 and len(board.storedValidFencePlacings) > 0:
            for coord_fence in board.storedValidFencePlacings:
                if(Path.ManhattanDistance(opp_coord, coord_fence.coord) < 3 or Path.ManhattanDistance(self.pawn.coord, coord_fence.coord) < 3):
                
                    if board.isFencePlacingBlocking(coord_fence) == 0:
                        r = (board.Fence_Distance(coord_fence),coord_fence)
                        possible_fence.append(r)
                else:
                    for placed_fence in board.fences:
                        if Path.ManhattanDistance(placed_fence.coord, coord_fence.coord) < 3 and  Path.ManhattanDistance(self.pawn.coord, coord_fence.coord) < 3:
                            if board.isFencePlacingBlocking(coord_fence) == 0:
                                r = (board.Fence_Distance(coord_fence),coord_fence)
                                possible_fence.append(r)
        possible_fence.sort(key=lambda tup: tup[0],reverse = True)
        #print('New Move'
        # for i in possible_fence:
        #     print(i[0])
        p1 = (Path.Dijkstra(board,self.pawn.coord,board.endPositions(0)))
        p2 = (Path.Dijkstra(board,opp_coord,board.endPositions(1)))
        diff = Path.length(p2) -Path.length(p1)
        if len(possible_fence) > 0:
            rand = possible_fence[0]
            worst = possible_fence[len(possible_fence)-1]
            #print("Best Wall: " + str(rand[0]) + ' Worst Wall: ' + str(worst[0]))
            if rand[0] > (Path.length(p2) -Path.length(p1)):
                wall = True
            else:
                wall = False
            if worst[0] - rand[0] < -1:
                f = worst[1]
                fence1 = Fence(self, None)
                fence2 = Fence(self, None)
                if f.direction == Fence.DIRECTION.HORIZONTAL:
                    fence1.direction = Fence.DIRECTION.VERTICAL
                    fence2.direction = Fence.DIRECTION.VERTICAL
                    c1 = GridCoordinates.top(GridCoordinates.left((f.coord)))
                    c2 = GridCoordinates.top(GridCoordinates.right(GridCoordinates.right(GridCoordinates.right(f.coord))))
                    fence1.coord = c1
                    fence2.coord = c2
                else:
                    fence1.direction = Fence.DIRECTION.HORIZONTAL
                    fence2.direction = Fence.DIRECTION.HORIZONTAL
                    c1 = GridCoordinates.bottom(GridCoordinates.bottom(GridCoordinates.bottom(GridCoordinates.left((f.coord)))))
                    c2 = GridCoordinates.top(GridCoordinates.left(f.coord))
                    fence1.coord = c1
                    fence2.coord = c2

        else:
            wall = False
        #print(worst[0])
        
        if random.randint(0,0) == 0 and self.remainingFences() > 0 and len(board.storedValidFencePlacings) > 0 and wall:
            #print(rand[0])
            if (diff - worst[0]) > (rand[0] - diff) and board.isValidFencePlacing(fence1.coord,fence1.direction):
            #if board.isValidFencePlacing(fence1.coord,fence1.direction):
                
                randomFencePlacing = fence1
            elif (diff - worst[0]) > (rand[0] - diff) and board.isValidFencePlacing(fence2.coord,fence2.direction):#
                randomFencePlacing = fence2
                
            else:
                randomFencePlacing = rand[1]
            #print(randomFencePlacing.coord)
            return randomFencePlacing
        #print(possible_fence)
        #print("There are " + str(near_fence) + "Possible Fences Near")
        # if random.randint(0, 2) == 0 and self.remainingFences() > 0 and len(board.storedValidFencePlacings) > 0:
        #     #randomFencePlacing = random.choice(board.storedValidFencePlacings)
        #     randomFencePlacing = random.choice(possible_fence)
        #     attempts = 5
        #     while board.isFencePlacingBlocking(randomFencePlacing(0)) and attempts > 0:
        #         #print("Cannot place blocking %s" % randomFencePlacing)
        #         randomFencePlacing = random.choice(board.storedValidFencePlacings)
        #         attempts -= 1
        #     if (attempts == 0):
        #         validPawnMoves = board.storedValidPawnMoves[self.pawn.coord]
        #         return random.choice(validPawnMoves)
        #     return randomFencePlacing
        else:
            validPawnMoves = board.storedValidPawnMoves[self.pawn.coord] #board.validPawnMoves(self.pawn.coord)
            p1 = (Path.Dijkstra(board,self.pawn.coord,board.endPositions(0)))
            for move in validPawnMoves:
                if str(move) == str(p1.firstMove()):
                    return move
            return random.choice(validPawnMoves)



            
