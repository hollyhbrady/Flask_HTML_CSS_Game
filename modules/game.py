from modules.player import Player

class Game:

    def __init__ (self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def play_game(self, player1, player2):
        if self.player1.gesture == "rock" and self.player2.gesture == "scissors":
            return f"{player1.name} wins by playing rock against {player2.name}'s scissors"
        if self.player1.gesture == "scissors" and self.player2.gesture == "rock":
            return f"{player2.name} wins by playing rock against {player1.name}'s scissors"
        if self.player1.gesture == "scissors" and self.player2.gesture == "paper":
            return f"{player1.name} wins by playing scissors against {player2.name}'s paper"
        if self.player1.gesture == "paper" and self.player2.gesture == "scissors":
            return f"{player2.name} wins by playing scissors against {player1.name}'s paper"
        if self.player1.gesture == "paper" and self.player2.gesture == "rock":
            return f"{player1.name} wins by playing paper {player2.name}'s rock"
        if self.player1.gesture == "rock" and self.player2.gesture == "paper":
            return f"{player2.name} wins by playing paper {player1.name}'s rock"
        if self.player1.gesture == "rock" and self.player2.gesture == "rock":
            return "No winner, this game is a draw. Best of 3?"
        if self.player1.gesture == "paper" and self.player2.gesture == "paper":
            return "No winner, this game is a draw. Best of 3?"
        if self.player1.gesture == "scissors" and self.player2.gesture == "scissors":
            return "No winner, this game is a draw, Best of 3?"
        else:
            return "What game are you trying to play?"
