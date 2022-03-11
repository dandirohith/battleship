
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
    
    def HuntTarget(self, x, y):
    #print("\n")
    #print("Starting Search with Hunt and Target Method")
        game = 1
        hit_count = 0
        target = "stop"
        Carrier_Hits = 0
        Carrier_Locations = [[]]
        Battleship_Hits = 0
        Battleship_Locations = [[]]
        Cruiser_Hits = 0
        Cruiser_Locations = [[]]
        Submarine_Hits = 0
        Submarine_Locations = [[]]
        Destroyer_Hits = 0
        Destroyer_Locations = [[]]

        while(game > 0):
            
            #time.sleep(2)
            #print(Legend_horz)
            #for x in self.opponent_board:
            #    print(x)
            #print("\n")
                
            # G1 = (randint(0,9)) #Row
            # G2 = (randint(0,9)) #Column
            G1 = x
            G2 = y

            unsunk = 0
            G1_index = 0
            G2_index = 0
            
            for x in self.opponent_board:
                for y in x:
                    if y == 7:
                        unsunk = 1
                        G1 = G1_index
                        G2 = G2_index
                        break
                    G2_index += 1
                if unsunk == 1:
                    break
                G1_index += 1
                G2_index = 0
            
            if self.opponent_board[G1][G2] != 6 and self.opponent_board[G1][G2] != 8:
                if self.opponent_board[G1][G2] != 7:
                    hit_count += 1
    
                # if self.opponent_board[G1][G2] != 0 and self.opponent_board[G1][G2] != 7:
                    # if self.opponent_board[G1][G2] == 5:
                    #     Carrier_Hits += 1
                    #     Carrier_Locations = [[G1,G2]]
                        #print("Ship Hit")
                    # elif self.opponent_board[G1][G2] == 4:
                    #     Battleship_Hits += 1
                    #     Battleship_Locations = [[G1,G2]]
                    #     #print("Ship Hit")
                    # elif self.opponent_board[G1][G2] == 3:
                    #     Cruiser_Hits += 1
                    #     Cruiser_Locations = [[G1,G2]]
                    #     #print("Ship Hit")
                    # elif self.opponent_board[G1][G2] == 2:
                    #     Submarine_Hits += 1
                    #     Submarine_Locations = [[G1,G2]]
                    #     #print("Ship Hit")
                    # elif self.opponent_board[G1][G2] == 1:
                    #     Destroyer_Hits += 1
                    #     Destroyer_Locations = [[G1,G2]]
                    #     #print("Ship Hit")
                    
                    # self.opponent_board[G1][G2] = 7
                    #print("Hit!")
                    # hit_count += 1
                    
                    target = "go"
                
                elif self.opponent_board[G1][G2] == 7:
                    target = "go"
                
                G1_Archive = G1
                G2_Archive = G2
                target_impossible1 = 0
                target_impossible2 = 0 
                target_impossible3 = 0
                target_impossible4 = 0
                
                while target == "go":
                        
                    Directions = [1,2,3,4]
                    Next_Coordinate = "Not Locked"
                        
                    if G1 == 0:
                        Directions.remove(1)
                        target_impossible1 = 1
                    if G1 == 9:
                        Directions.remove(2)        
                        target_impossible2 = 1
                    if G2 == 0:
                        Directions.remove(3)
                        target_impossible3 = 1
                    if G2 == 9:
                        Directions.remove(4)
                        target_impossible4 = 1
                    
                    #print(Directions)
                    #print("G1= " + str(G1))
                    #print("G2= " + str(G2))
                    target_direction = random.choice(Directions)
                    #print("Direction Locked")
                    #print(target_direction)
                    #time.sleep(2)
                    #print(Legend_horz)
                    #for x in self.opponent_board:
                    #    print(x)
                    #print("\n")
                    
                    #time.sleep(5)
                
                    
                        #--UP--
                    if target_direction == 1:
                        if self.opponent_board[G1-1][G2] != 6 and self.opponent_board[G1-1][G2] != 7 and self.opponent_board[G1-1][G2] != 8:
                            G1 = G1 - 1
                            Next_Coordinate = "Locked"
                        else:
                            target_impossible1 = 1
                            #print("up impossible")
                        #--DOWN--
                    if target_direction == 2:
                        if self.opponent_board[G1+1][G2] != 6 and self.opponent_board[G1+1][G2] != 7 and self.opponent_board[G1+1][G2] != 8:
                            G1 = G1 + 1
                            Next_Coordinate = "Locked"
                        else:
                            target_impossible2 = 1
                            #print("down impossible")
                        #--LEFT--
                    if target_direction == 3:  
                        if self.opponent_board[G1][G2-1] != 6 and self.opponent_board[G1][G2-1] != 7 and self.opponent_board[G1][G2-1] != 8:
                            G2 = G2 - 1
                            Next_Coordinate = "Locked"
                        else:
                            target_impossible3 = 1
                            #print("Left impossible")
                        #--RIGHT--
                    if target_direction == 4:
                        if self.opponent_board[G1][G2+1] != 6 and self.opponent_board[G1][G2+1] != 7 and self.opponent_board[G1][G2+1] != 8:
                            G2 = G2 + 1
                            Next_Coordinate = "Locked"
                        else:
                            target_impossible4 = 1
                            #print("Right impossible")
                            
                    if target_impossible1 == 1 and target_impossible2 == 1 and target_impossible3 == 1 and target_impossible4 == 1:
                        target = "stop"
                    #print("Next G1= " + str(G1))
                    #print("Next G2= " + str(G2))
                    #time.sleep(1)
                    
                    if Next_Coordinate == "Locked":
                        
                        self.turn_count += 1
                        self.x = G1
                        self.y = G2

                        # attack at g1,g2
                        # get info of attack at g1,g2 
                        # if attack is hit
                        # update opponent_board




                        # if self.opponent_board[G1][G2] == 5:
                        #     Carrier_Hits += 1
                        #     if Carrier_Hits == 1:
                        #         Carrier_Locations = [[G1,G2]] 
                        #     else:
                        #         Carrier_Locations = numpy.append(Carrier_Locations,[[G1,G2]],axis=0)
                        #     #print(Carrier_Locations)
                        # elif self.opponent_board[G1][G2] == 4:
                        #     Battleship_Hits += 1
                        #     if Battleship_Hits == 1:
                        #         Battleship_Locations = [[G1,G2]]
                        #     else:
                        #         Battleship_Locations = numpy.append(Battleship_Locations,[[G1,G2]],axis=0)
                        #     #print(Battleship_Locations)
                        # elif self.opponent_board[G1][G2] == 3:
                        #     Cruiser_Hits += 1
                        #     if Cruiser_Hits == 1:
                        #         Cruiser_Locations =[[G1,G2]]
                        #     else:
                        #         Cruiser_Locations = numpy.append(Cruiser_Locations,[[G1,G2]],axis=0)
                        #     #print(Cruiser_Locations)
                        # elif self.opponent_board[G1][G2] == 2:
                        #     Submarine_Hits += 1
                        #     if Submarine_Hits == 1:
                        #         Submarine_Locations = [[G1,G2]]
                        #     else:
                        #         Submarine_Locations = numpy.append(Submarine_Locations,[[G1,G2]],axis=0)
                        #     #print(Submarine_Locations)
                        # elif self.opponent_board[G1][G2] == 1:
                        #     Destroyer_Hits += 1
                        #     if Destroyer_Hits == 1: 
                        #         Destroyer_Locations = [[G1,G2]]
                        # else:
                        #     Destroyer_Locations = numpy.append(Destroyer_Locations,[[G1,G2]],axis=0)
                        #print(Destroyer_Locations)
                        
                        if self.opponent_board[G1][G2] != 0:
                            self.opponent_board[G1][G2] = 7
                            G1_Archive = G1
                            G2_Archive = G2
                            #print("Hit!")
                            hit_count += 1
                            
                            #print(Legend_horz)
                            #for x in self.opponent_board:
                            #    print(x)
                            #print("\n")
                            #time.sleep(1)
                            
                            # if Carrier_Hits == 5:
                            #     for x in Carrier_Locations:
                            #         #print(x)
                            #         coor1 = x[0]
                            #         coor2 = x[1]
                            #         self.opponent_board[coor1][coor2] = 8
                            #         Carrier_Hits = 6
                            #     target = "stop"
                            # if Battleship_Hits == 4:
                            #     for x in Battleship_Locations:
                            #         #print(x)
                            #         coor1 = x[0]
                            #         coor2 = x[1]
                            #         self.opponent_board[coor1][coor2] = 8
                            #         Battleship_Hits = 5
                            #     target = "stop"
                            # if Cruiser_Hits == 3:
                            #     for x in Cruiser_Locations:
                            #         #print(x)
                            #         coor1 = x[0]
                            #         coor2 = x[1]
                            #         self.opponent_board[coor1][coor2] = 8
                            #         Cruiser_Hits = 4
                            #     target = "stop"
                            # if Submarine_Hits == 3:
                            #     for x in Submarine_Locations:
                            #         #print(x)
                            #         coor1 = x[0]
                            #         coor2 = x[1]
                            #         self.opponent_board[coor1][coor2] = 8
                            #         Submarine_Hits = 4
                            #     target = "stop"
                            # if Destroyer_Hits == 2:
                            #     for x in Destroyer_Locations:
                            #         #print(x)
                            #         coor1 = x[0]
                            #         coor2 = x[1]
                            #         self.opponent_board[coor1][coor2] = 8
                            #         Destroyer_Hits = 3
                            #     target = "stop"

                        else:
                            self.opponent_board[G1][G2] = 6
                            G1 = G1_Archive
                            G2 = G2_Archive
                            #print("miss")
                            
                        target_impossible1 = 0
                        target_impossible2 = 0 
                        target_impossible3 = 0
                        target_impossible4 = 0
                    
                else:
                    self.opponent_board[G1][G2] = 6
                
                if hit_count == 17:
                    #print("Game Complete")
                    #print(self.turn_count)
                    game = 0
                    
        # return self.opponent_board,self.turn_count

    def hit_or_miss(self, x, y , info):
        self.info = info

        ## info = 1 for miss, 0 for a hit, -1 for an out of range shooting, 2 for special move nullify. 3 for your next move to be a Hawkeye Shot
        if info != -1 and info == 0:
            self.opponent_board[x][y] = 7
            self.turn_count += 1
            hunt(self,x,y)
        elif info==1:
            self.opponent_board[x][y] = 6
            self.turn_count += 1
            # trials
            

prev_attack = []
ships = [
 [3, 3, 3, 1],
 [4, 3, 4, 0],
 [5, 8, 4, 0]
 [1, 1, 5, 1]
 [9, 1, 5, 1] ]
        
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

