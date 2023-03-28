import unittest
from board import Board, FancyBoard

def reversedEnumerate(l: list):
    return zip(range(len(l)-1, -1, -1), l)

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board(3)
        
    def test_separate_board(self):
        self.assertIsInstance(self.board.separate_board(), list)
        self.assertEqual(len(self.board.separate_board()), 3)
        
        for row in self.board.separate_board():
            self.assertIsInstance(row, list)
            for space in row:
                self.assertIsInstance(space, int)
        
    def test_available_moves(self):
        self.assertIsInstance(self.board.available_moves(), list)
        self.assertEqual(len(self.board.available_moves()), 9)
        self.board.set_player_token('X', 1)
        self.assertEqual(len(self.board.available_moves()), 8)
                
    def test_check_winner_x_row(self):
        self.assertFalse(self.board.check_win(['X', 'O']))
        for i in range(3):
            self.board.set_player_token('X', i)
        self.assertEqual(self.board.check_win(['X', 'O']), 'X')
        
    def test_check_winner_x_col(self):
        self.assertFalse(self.board.check_win(['X', 'O']))
        sep_game_board = self.board.separate_board()
        for row in sep_game_board:
            self.board.set_player_token('X', row[0]) 
        self.assertEqual(self.board.check_win(['X', 'O']), 'X')
        
    def test_check_winner_x_dig_left(self):
        self.assertFalse(self.board.check_win(['X', 'O']))
        sep_game_board = self.board.separate_board()
        for idx, row in enumerate(sep_game_board):
            self.board.set_player_token('X', row[idx]) 
        self.assertEqual(self.board.check_win(['X', 'O']), 'X')
        
    def test_check_winner_x_dig_right(self):
        self.assertFalse(self.board.check_win(['X', 'O']))
        sep_game_board = self.board.separate_board()
        for idx, row in reversedEnumerate(sep_game_board):
            self.board.set_player_token('X', row[idx]) 
        self.assertEqual(self.board.check_win(['X', 'O']), 'X')
        
    def check_if_not_draw(self):
        self.assertFalse(self.board.check_draw())
        
    def check_if_game_board_full(self):
        for i in self.board.available_moves():
            self.board.set_player_token('X', i)
        self.assertTrue(self.board.check_draw())
        
        

if __name__ == '__main__':
    unittest.main()