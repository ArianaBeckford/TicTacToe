import math
import random

class Player:
    def __init__(self, letter):
        #letter is x or o
        self.letter = letter
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)    

    def get_move(self, game):
        #rnadom valid sport for next move
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8):')
            #check value by trying to cast it to an integer
            #if not integer is invalid
            #if that spot isn't available on the board, it's invalid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')

        return val
class UnbeatablePlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves()) #randomly chosen
        else:
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, s, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        #check if previous move was winner
        if s.current_winner == other_player:
            return {'position': None,
            'score': 1 * (s.num_empty_squares() + 1) if other_player == max_player else -1 * (s.num_emptysquares() + 1)
            }
        elif not s.empty_squares():
            return {'position': None, 'score': 0}

        #initialize dictionaries
        if player == max_player:
            best = {'position': None, 'score': -math.inf} #each score maximizes
        else:
            best = {'position': None, 'score': math.inf}  #each score minimizes  
        for possible_move in s.available_moves():
            #1 make a move, try that spot
            s.make_move(possible_move, player)

            #2 use minimax to simulate a game after making that move
            sim_score = self.minimax(s, other_player)

            #3 undo the move
            s.board[possible_move] = ' '
            s.current_winner = None
            sim_score['position'] = possible_move

            #4 update dictionaries if necessary
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score

            else:
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best

