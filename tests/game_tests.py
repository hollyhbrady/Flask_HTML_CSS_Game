import unittest
from modules.game import *
from modules.player import Player

class TestGame(unittest.TestCase):

    def setUp(self):
        self.roosa = Player("Roosa", "rock")
        self.colin = Player("Colin", "paper")
        self.hannah = Player("Hannah", "scissors")