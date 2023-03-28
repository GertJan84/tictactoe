from abc import ABC
from blessed import Terminal
import string

def reversedEnumerate(l: list):
    return zip(range(len(l)-1, -1, -1), l)

class Board(ABC):
    
    @staticmethod
    def print_vs_title(players: list) -> None:
        '''Print vs title'''
        print(f'\n==== {players[0].name} ({players[0].token}) vs {players[1].name} ({players[1].token}) ====\n')
    
    def __init__(self, board_size=None) -> None:
        if not board_size:
            board_size = input('How many squares across should the board be? ')
            while not board_size.isdigit():
                print('That is not a option')
                board_size = input('How many squares across should the board be? ')
            self.__board_size = int(board_size)
        else:
            self.__board_size = board_size
        self.__game_board = [i for i in range((self.__board_size ** 2))]
        
    @property
    def game_board(self):
        return self.__game_board
    
    @property
    def board_size(self):
        return self.__board_size
        
    def separate_board(self) -> list[list[int]]:
        '''Get game board defied by rows and columns'''
        return [self.game_board[i:i+self.board_size] for i in range(0, len(self.game_board), self.board_size)]
                        
    def __get_player_locations(self, token: str) -> list[int]:
        '''Get all player tokens from the board'''
        return [idx for idx, square in self.game_board if square == token]
    
    def set_player_token(self, token: str, location: int) -> None:
        '''Set player token on the board'''
        self.game_board[self.game_board.index(location)] = token
        
    def available_moves(self) -> list[int]:
        '''Get a list of available moves'''
        return [idx for idx, square in enumerate(self.game_board) if str(square).isdigit()]  
            
    def check_win(self, tokens: list) -> str | bool:
        '''Check if there is a winner'''
        
        sep_game_board = self.separate_board()
        
        for token in tokens:
            # Check all rows
            for row in sep_game_board:
                if all([token == square for square in row]):
                    return token
                
            # Check all columns
            for item, _ in enumerate(sep_game_board):
                if all([row[item] == token for row in sep_game_board]):
                    return token

            # Check diagonal left to right
            if all([row[idx] == token for idx, row in enumerate(sep_game_board)]):
                return token
            
            # Check diagonal right to left
            if all([row[idx] == token for idx, row in reversedEnumerate(sep_game_board)]):
                return token
            
        return False

    def check_draw(self) -> bool:
        '''Check if there is a number on the board'''
        for square in self.game_board:
            if str(square).isdigit():
                return False
        return True
    
class SimpleBoard(Board):
    def __init__(self) -> None:
        super().__init__()
                
    def print_board(self, players: list) -> None:
        '''Print a board'''
        
        Board.print_vs_title(players)
        
        counter = 0
        
        print('+', end='')
        
        dashes_top_bottom = '----'*self.board_size
        dashes_between_rows = '+'
        print(dashes_top_bottom[:-1], end='+\n')
        
        dashes_between_rows += '---+'*self.board_size
        
        
        
        for idx, row in enumerate(self.separate_board()):
            
            print('|', end=' ')
            for i in row:
                
                counter += 1
                
                if not str(i).isdigit():
                    print(f'{i} ', end='| ')
                else:
                    print(f'{counter} ', end='| ')
            print()  
            
            if idx < len(row) -1:                    
                print(dashes_between_rows)

           
        print('+', end='')
        print(dashes_top_bottom[:-1], end='+\n')
        
class FancyBoard(Board):
    def __init__(self, board_size=None) -> None:
        super().__init__(board_size)
        self.__term = Terminal()
        self.__alphabet = list(string.ascii_uppercase)
        
    @property
    def get_alphabet(self) -> list[int]:
        return self.__alphabet
        
    def get_letter_index(self, letter: str) -> int | bool:
        '''Get index of letter'''
        if letter in self.get_alphabet:
            return self.get_alphabet.index(letter)
        return False
        
            
    def print_board(self, players: list) -> None:
        '''Print a board'''
        
        print(self.__term.clear)
        
        Board.print_vs_title(players)
        
        for n in range(self.board_size):
            print(' ' + self.get_alphabet[n], end=' ')
            
        print()
            
        for idx, row in enumerate(self.separate_board(), 1):
            
            print(idx, end='')
            
            for index, space in enumerate(row):
                
                if str(space).isdigit():
                    
                    if self.separate_board().index(row) % 2 == 0:
                        
                        if index % 2 == 0: 
                            print(self.__term.black_on_snow4('   '), end='')
                        else:
                            print(self.__term.black_on_gray7('   '), end='')
                            
                    else:
                        
                        if index % 2 == 0: 
                            print(self.__term.black_on_gray7('   '), end='')
                        else:
                            print(self.__term.black_on_snow4('   '), end='')
                            
                elif space == 'X':
                    print(self.__term.black_on_chartreuse3('   '), end='')
                    
                elif space == 'O':
                    print(self.__term.black_on_violetred('   '), end='')
                    
            print()
