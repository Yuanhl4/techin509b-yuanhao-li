import unittest
import logic
import cli
#import random


class TestLogic(unittest.TestCase):

    def test_empty_bpard(self):
        self.assertEqual(logic.make_empty_board(), 
            [[None, None, None],
            [None, None, None],
            [None, None, None],]
        )
    
    def test_get_winner(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')

    def test_vaible_spot(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        row = 0
        col = 1
        self.assertEqual(board[row][col],None)

    def test_player_switch(self):
        player = "X"
        self.assertEqual(logic.other_player(player), "O")

    def test_bot_move(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        #original_board = [row[:] for row in board]
        #self.assertEqual(board, original_board)
        x, y = logic.bot_move(board)
        self.assertIsInstance((x,y), tuple)
        self.assertIsNone(board[x][y])

    # TODO: Test all functions from logic.py!

    #def 
    #def mahr_test():
        #print("1111\n")

if __name__ == '__main__':
    unittest.main()
