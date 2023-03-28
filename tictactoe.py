from board import FancyBoard, SimpleBoard
from player import HumanPlayer, RandomPlayer, SequentialPlayer

class TicTacToe:
    game_run = 1
    
    @staticmethod
    def decide_player() -> list:
        '''Decide what type of players there are'''
        players = []
        for idx, token in enumerate(['X', 'O'], 1):
            while True:
                type_player = input(f'{idx}# What type of player do you want to be (S/R/H): ')
                if type_player.lower() == 's':
                    players.append(SequentialPlayer(token))
                    break
                elif type_player.lower() == 'h':
                    players.append(HumanPlayer(token))
                    break
                elif type_player.lower() == 'r':
                    players.append(RandomPlayer(token))
                    break
                else:
                    print('That is not a option')
        return players
    
    @staticmethod
    def choice_board() -> SimpleBoard | FancyBoard:
         while True:
            board_type = input('Would you like to see a (s)imple or a (f)ancy board? ').lower()
            if board_type == 's':
                return SimpleBoard()
            elif board_type == 'f':
                return FancyBoard()
            else:
                print('That is not a option')
            
        
    
    def __init__(self) -> None:
        print(f'\nWelcome to game #{TicTacToe.game_run}')
        self.__players = TicTacToe.decide_player()
        self.__board = TicTacToe.choice_board()
        
    @property    
    def board(self):
        return self.__board
    
    @property
    def players(self):
        return self.__players
    
    def play(self):
        
        game_on = True
        while game_on:
            
            for player in self.players:
                
                self.board.print_board(self.players)
                
                move = player.set_move(self.board)
                self.board.set_player_token(player.token, move)
                
                winner_token = self.board.check_win([player.token for player in self.players])
                
                if winner_token:
                    self.board.print_board(self.players)
                    print(f'Player {[player.name for player in self.players if player.token == winner_token][0]} won')
                    TicTacToe.game_run += 1
                    game_on = False
                    break
                
                elif self.board.check_draw():
                    self.board.print_board(self.players)
                    print('Its a draw')
                    TicTacToe.game_run += 1
                    game_on = False
                    break
                
         

if __name__ == "__main__":
    while True:
        TicTacToe().play()
