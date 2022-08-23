import time
from player import HumanPlayer, RandomComputerPlayer, UnbeatablePlayer
class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] #single list is use to represent 3x3 board
        self.current_winner = None #keeps track of winner

    def print_board(self):
        #gets rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_numbers():
        num_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in num_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        #if valid move, then make move
        #return true, if invalid, return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        #check row
        row_index = square // 3
        row = self.board[row_index*3 : (row_index + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        #check column
        col_index = square % 3
        column = [self.board[col_index + i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        #check diagonals
        #check only if the square is an even number, only moves possible to win diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] #left to right
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]] #right to left
            if all([spot == letter for spot in diagonal2]):
                return True
            
        return False


def play(game, x_player, o_player, print_game=True):
    #returns the winner of the game(letter) or none for a tie
    if print_game:
        game.print_board_numbers()

    letter = 'X' #starting letter
    #iterate while game has empty squares
    while game.empty_squares():
        #get move from the right player
        if letter == '0':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f'makes a move to square {square}')
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            #alternate letters
            letter = 'O' if letter == 'X' else 'X'
        #small pause
        if print_game:
            time.sleep(0.8)
           

    if print_game:
        print("It's a tie!")

if __name__ == '__main__':
    x_wins = 0
    o_wins = 0
    ties = 0
    for _ in range(1000):
        x_player = HumanPlayer('X')
        o_player = UnbeatablePlayer('O')
        t = TicTacToe()
        result = play(t, x_player, o_player, print_game=False)
        if result == 'X':
            x_wins += 1
        elif result== 'O':
            o_wins += 1
        else:
            ties += 1

    print(f'After 1000 iterations, we see {x_wins} X wins, {o_wins} O wins, and {ties} ties')


