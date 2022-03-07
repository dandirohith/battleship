import random

GRID_LENGTH = 10
SHIP_NAMES = [
    "Carrier",
    "Battleship",
    "Destroyer",
    "Submarine",
    "Patrol boat"
]
SHIP_SIZES = [
    5, 
    5,
    4,
    4,
    3
]

n_ships = len(SHIP_SIZES)

# ships = np.zeros((n_ships, GRID_LENGTH, GRID_LENGTH))


ships = []
for i in range(n_ships):
    l = []
    for j in range(GRID_LENGTH):
        lis = []
        for k in range(GRID_LENGTH):
            lis.append(0)
        l.append(lis)
    ships.append(l)

# player ship placement
# ships[0][0][:5] = 1
for i in range(5):
    ships[0][0][i] = 1

# ships[1][4:8][7] = 1
for i in range(4,8):
    ships[1][i][7] = 1

# ships[2][9][3:6] = 1
for i in range(3,6):
    ships[2][9][i] = 1

# ships[3][3:6][1] = 1
for i in range(3,6):
    ships[3][i][1] = 1

# ships[4][5][8:10] = 1
for i in range(8,10):
    ships[4][5][i] = 1

class Battleship:
    def __init__(self, ships):
        self._ships = ships
        self._turn_revealed = []
        
    @property
    def _board(self):
        return to_board(self._ships)
        
    @property
    def grid_length(self):
        return self._board.shape[0]
    
    @property
    def is_solved(self):
        return self.revealed.sum() == self._board.sum()
    
    @property
    def revealed(self):
        return to_board(self._revealed_ships)
        
    @property
    def _revealed_ships(self):
        if self.turns > 0:
            return self._turn_revealed[-1]
        else:
            return np.ma.masked_all_like(self._ships)
    
    @property
    def ship_sizes(self):
        return self._ships.sum(axis=(1, 2))
    
    @property
    def sunk(self):
        ship_sizes = self._ships.sum(axis=(1, 2))
        revealed_sizes = (self._revealed_ships
                              .sum(axis=(1, 2))
                              .filled(0))
        
        return ship_sizes == revealed_sizes
    
    @property
    def turn_revealed(self):
        return [np.ma.masked_all_like(self._board)] \
                + [to_board(revealed) for revealed in self._turn_revealed]
    
    @property
    def turns(self):
        return len(self._turn_revealed)
    
    def guess(self, i, j):
        if not self.revealed.mask[i, j]:
            raise ValueError(f"{i}, {j} already guessed")
        else:
            prev_sunk = self.sunk

            next_ships = self._revealed_ships.copy()
            next_ships[:, i, j] = self._ships[:, i, j]
            self._turn_revealed.append(next_ships)
            
            curr_sunk = self.sunk
            
            if (curr_sunk == prev_sunk).all():
                sunk = None
            else:
                sunk = (curr_sunk & ~prev_sunk).argmax()
            
            return self._board[i, j], sunk

class Strategy():
    @abstractmethod
    def next_guess(self, revealed):
        pass

    def reveal(self, i, j, hit_or_miss, sunk):
        pass

def play(ships, strategy, progress_bar=False):
    game = Battleship(ships)
    
    if progress_bar:
        pbar = tqdm(total=int(ships.sum()))
    
    while not game.is_solved:
        i, j = strategy.next_guess(game.revealed)
        hit_or_miss, sunk = game.guess(i, j)
        strategy.reveal(i, j, hit_or_miss, sunk)
        
        if progress_bar and hit_or_miss == 1:
            pbar.update()
            
    if progress_bar:
        pbar.close()
        
    return game

class ManualStrategy(Strategy):
    def next_guess(self, revealed):
        i = int(input("Enter row to guess: "))
        j = int(input("Enter column to guess: "))
        return i, j

try:
    play(ships, ManualStrategy())
except KeyboardInterrupt:
    print("Game ended")