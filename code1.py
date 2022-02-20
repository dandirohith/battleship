from pickle import FALSE
import random
from re import A

class BattleShip:
    def __init__(self):
        self.team_name = "Team 1"
        self.board = board
        self.opponent_board = opponent_board
        self.info = -1

    def set_board(self):
        return self.board

    def attack(self):
        x = random.randint(0,10)
        y = random.randint(0,10)
        return (x,y)

    def hit_or_miss(self, x, y , info):
        self.info = info
        ## info = 1 for miss, 0 for a hit, -1 for an out of range shooting, 2 for special move nullify. 3 for your next move to be a Hawkeye Shot
        if info != -1 and info == 0:
            self.opponent_board[x][y] = info


class Coordinate:
    x = ""
    y = -1

    def __init__(self, *args):
        alpha = "ABCDEFGHIJ"
        if(len(args)==0):
            r = random.randint(0, 9)   
            self.x = alpha[random.randint(0,9)]
            self.y = r
        elif isinstance(args[0], str): #str, int
            self.x = args[0]
            self.y = args[1]
        elif isinstance(args[0], int): #int, int
            self.x = alpha[args[0]]
            self.y = args[1]

    def Coordinate(self,shot):
        self.x = shot[0]
        self.y = int(shot[1])

    def X(self):
        return self.x

    def xint(self):
        alpha = "ABCDEFGHIJ"
        for i in range(0, 10):
            if(alpha[i] == self.x):
                return i
        return -1

    def Y(self):
        return self.y

    def get(self):
        return (self.x + str(self.y))

    def split(self,value):
        returnValue  = { value[0]: int(value[1]) } # returning x: y  map
        return returnValue

    def equals(self,c): # assuming function parameter as string 
        if(len(c)!=2):
            return False
        return (c[0]==self.x and int(c[1])==self.y)

    def hashcode(self):
        return hash(self.x) + hash(self.y)

class Grid:
    coords = {}
    gridOwner = -1
    gridSize = 10

    def __init__(self, owner):
        self.gridOwner = owner

    def getCoord(self, *args):
        # x, y:
        if(len(args)== 2):
            x = args[0]
            y = args[1]
            fullcoord = x.upper() + str(y);
            return (self.coords).get(fullcoord)
        else:
            c = args[0]
            x = c[0].upper()
            y = c[1]
            fullcoord = x + y
            return (self.coords).get(fullcoord)
    def probCheck(self,coordinate): # coordinate as string
        if( (coordinate.Y() > self.gridSize) or (coordinate.xint() > self.gridSize )or (coordinate.Y() < 0)):
            return 1
        if (self.coords).get(coordinate.get()) is not None: 	
            if((self.coords).get(coordinate.get()) == "*"):	
                return 0
            else:		
                return 1
        else:
            return 0
    def isFree(self,*args):
        alpha = "ABCDEFGHIJ"
        if(len(args) == 2):
            xloc = -1
            for i in range(0,10):
                if(alpha[i]==args[0]):
                    xloc = i
                    break
            if(xloc < 0 or xloc >= 10 or args[1] < 0 or args[1] > gridSize):
                return 2
            else:
                if((self.coords).get(args[0]+str(args[1]))) is not NONE:
                    return 1
                else:
                    return 0
        else:
            xloc = -1
            for i in range(0,10):
                if(alpha[i]==args[0]):
                    xloc = i
                    break
            if(xloc < 0 or xloc >= 10 or int(args[1]) < 0 or int(args[1]) > gridSize):
                return 2
            else:
                if((self.coords).get(args[0]+args[1])) is not NONE:
                    return 1
                else:
                    return 0
    def fire(self, coordinate):
        if((self.coords).get(coordinate.get()) is not None):
            if((self.coords).get(coordinate.get()) == "*"):
                (self.coords).update({coordinate.get(), "X"})
                return 2
            else:
                return 0
        else:
            self.coords.update({coordinate.get(), "X"})
            return 1

class ProbabilityMap:
    p = False
    s = False
    d = False
    b = False
    a = False
    highest = -1
    probabilities = {}
    userGrid = Grid(-1)
    
    def isEdge(self,i,j):
        return ((i == 0 or 
				i == self.userGrid.getGridSize()-1  or
				j == 0 or 
				j == self.userGrid.getGridSize()-1)
			and
			not(i == 0 and j == 0) or
			(i == 0 and j == self.userGrid.getGridSize()-1) or
			(i == self.userGrid.getGridSize()-1 and j == 0) or
			(i == self.userGrid.getGridSize()-1 and j == self.userGrid.getGridSize()-1))
    
    def isCorner(self,i,j):
        return ((i == 0 and j == 0) or
				(i == 0 and j == self.userGrid.getGridSize()-1) or
				(i == self.userGrid.getGridSize()-1 and j == 0) or
				(i == self.userGrid.getGridSize()-1 and j == self.userGrid.getGridSize()-1))
    
    def __init__(self, g):
        self.p = True
        self.s = True
        self.d = True
        self.b = True
        self.a = True
        self.userGrid = g
        assesMap();

    def assessMap(self):
        sizes = (self.userGrid).getShipSizes()
        highest = 0
        for i in range((self.userGrid).getGridSize()):
            for j in range((self.userGrid).getGridSize()):
                coord = Coordinate(i, j)
                probability = 0

                if(self.userGrid.probCheck(coord)==0):
                    for k in range(sizes.length):
                        if(checkDirection(self.userGrid, sizes[k], i, j, "left")):
                            probability += 1
                        if(checkDirection(self.userGrid, sizes[k], i, j, "right")):
                            probability += 1
                        if(checkDirection(self.userGrid, sizes[k], i, j, "up")):
                            probability += 1
                        if(checkDirection(self.userGrid, sizes[k], i, j, "down")):
                            probability += 1
                    if(isEdge(i, j)):
                        probability *= 1.25
                    elif(isCorner(i, j)):
                        probability *= 1.5
                    highest = max(probability, highest)
                    Alphabet = "ABCDEFGHIJKLMNOPQGRSTUVWXYZ"
