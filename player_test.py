import unittest
from player import HumanPlayer, RandomPlayer, SequentialPlayer
from board import Board, FancyBoard

class TestBoard(unittest.TestCase):
    def setUp(self) -> None:
        self.board = Board(3)
        self.hmp = HumanPlayer('X')
        self.rmp = RandomPlayer('X')
        self.sep = SequentialPlayer('X')
        self.fanboard = FancyBoard(3)
    
    def test_humanplayer_location(self):
        self.assertEqual(self.hmp.set_move(self.board, 1), 0)
        self.assertEqual(self.hmp.set_move(self.fanboard, 'a1'), 0)
        
    def test_sequentialplayer_location(self):
        self.assertEqual(self.sep.set_move(self.board), 0)
        self.board.set_player_token('X', 0)
        self.assertEqual(self.sep.set_move(self.board), 1)
        
    def test_randomplayer_location(self):
        for _ in self.board.available_moves():
            random_player_move = self.rmp.set_move(self.board)
            self.assertTrue(random_player_move in self.board.available_moves())
            self.board.set_player_token('X', random_player_move)

        
if __name__ == '__main__':
    unittest.main()