import unittest
from modules.player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.roosa = Player("Roosa", "rock")

    def test_player_has_name(self):
        self.assertEqual("Roosa", self.roosa.name)
    
    def test_player_has_gesture(self):
        self.assertEqual("rock", self.roosa.gesture)