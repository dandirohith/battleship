
import random

class BattleShip:
    def __init__(self):
        self.team_name = "10k"
        self.ships = ships
        self.opponent_board = opponent_board
        self.info = -1
        self.parity_board = parity_board
        self.turn_count = 0
        self.x = x
        self.y = y

    def set_ships(self):
        return self.ships

    def attack(self):
        return (self.x,self.y)

    def trials(self):
        rand_index = random.randint(0,49)
        self.x = self.parity_board[rand_index][0]
        self.y = self.parity_board[rand_index][1]
        (self.parity_board).remove([self.x,self.y])
        (self.prev_attack).append([self.x,self.y])

    def hit_or_miss(self, x, y , info):
        self.info = info

        ## info = 1 for miss, 0 for a hit, -1 for an out of range shooting, 2 for special move nullify. 3 for your next move to be a Hawkeye Shot
        if info != -1 and info == 0:
            self.opponent_board[x][y] = 7
            self.turn_count += 1
        elif info==1:
            self.opponent_board[x][y] = 6
            self.turn_count += 1
            # trials
            

prev_attack = []
ships = [
 [3, 3, 3, 1],
 [4, 3, 4, 0],
 [5, 8, 4, 0],
 [1, 1, 5, 1],
 [9, 1, 5, 1], ]
        
parity_board = []
temp = 1
for i in range(10):
    for j in range(10):
        if(temp==1):
            parity_board.append([i,j])
        temp = 1 - temp

opponent_board = []
for i in range(10):
    lis = []
    for j in range(10):
        lis.append(0)
    opponent_board.append(lis)

