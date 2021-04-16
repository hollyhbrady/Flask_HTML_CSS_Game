from modules.player import Player

def play_game(player1, player2):
    if player1 == "rock" and player2 == "scissors":
        return "Player 1 wins by playing rock"
    if player1 == "scissors" and player2 == "rock":
        return "Player 2 wins by playing rock"
    if player1 == "scissors" and player2 == "paper":
        return "Player 1 wins by playing scissors"
    if player1 == "paper" and player2 == "scissors":
        return "Player 2 wins by playing scissors"
    if player1 == "paper" and player2 == "rock":
        return "Player 1 wins by playing paper"
    if player1 == "rock" and player2 == "paper":
        return "Player 2 wins by playing paper"
    if player1 == "rock" and player2 == "rock":
        return "No winner, this game is a draw. Best of 3?"
    if player1 == "paper" and player2 == "paper":
        return "No winner, this game is a draw. Best of 3?"
    if player1 == "scissors" and player2 == "scissors":
        return "No winner, this game is a draw, Best of 3?"
    else:
        return "What game are you trying to play?"
