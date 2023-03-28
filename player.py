from board import Board
from abc import ABC, abstractmethod
import random
import time

class Player(ABC):
    
    already_played = []
    sleep_time = 1
    
    @staticmethod
    def name_taken(name: str) -> bool:
        '''Check if name is already taken'''
        if name in Player.already_played:
            return True
        return False
            
    def __init__(self, token: str, name: str) -> None:
        self.__token = token
        self.__name = name
        Player.already_played.append(name)
        
    @property
    def name(self):
        return self.__name
    
    @property
    def token(self):
        return self.__token
     
    @abstractmethod
    def set_move() -> None:
        pass
    
    @abstractmethod
    def __str__() -> str:
        pass
                
class HumanPlayer(Player):
    def __init__(self, token: str) -> None:
        while True:
            name = input('What is your name ')
            
            if Player.name_taken(name):
                print('Denied! You have already played.')
            else:
                break
            
        super().__init__(token, name)
        
    def set_move(self, board: Board, location=None) -> str | None:
        '''Ask for position and if position is coordinates calculate position and return position'''
        while True:
            if not location:
                location = input(f'On what square do you want to place a {self.token} ')
            if str(location).isdigit():
                board_position = int(location) - 1
                if board_position in board.available_moves():
                    return board_position 
            else:
                x_cor = board.get_letter_index(location[0].upper())
                
                if str(x_cor).isdigit():
                    
                    layout_board = board.separate_board()
                    y_cor = (int(location[1]) - 1)
                    row = layout_board[y_cor]
                    
                    if y_cor < len(row):                    
                        board_position = row[x_cor]
                    if board_position in board.available_moves():
                        return board_position
            print('That is not a valid location')
            location = None
                
    def __str__(self) -> str:
        return f'HumanPlayer name {self.name}, token {self.token}'
        
class RandomPlayer(Player):
    def __init__(self, token: str) -> None:
        while True:
            with open('names') as f:
                random_name = random.choice(f.readlines()).replace('\n', '')
            if not Player.name_taken(random_name):
                break            
            
        super().__init__(token, random_name)
     
    def set_move(self, board: Board) -> int:
        '''Get a random available move'''
        time.sleep(Player.sleep_time)
        return random.choice(board.available_moves())
        
    def __str__(self) -> str:
        return f'RandomPlayer name {self.name}, token {self.token}'
    
        
class SequentialPlayer(Player):
    def __init__(self, token: str) -> None:
        
        i = 0
        while True:
            i += 1
            name = f'Seq{i}'
            
            if not Player.name_taken(name):
                break
        
        super().__init__(token, name)
        
    def set_move(self, board: Board) -> int:
        '''Get the first available move'''
        time.sleep(Player.sleep_time)
        return board.available_moves()[0]
        
    def __str__(self) -> str:
        return f'SequentialPlayer name {self.name}, token {self.token}'
        
    