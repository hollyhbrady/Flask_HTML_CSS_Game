from modules.player import Player

def play_game(player1, player2):
    if player1.gesture == "rock" and player2.gesture == "scissors":
        return "Player 1 wins by playing rock"
    if player1.gesture == "scissors" and player2.gesture == "rock":
        return "Player 2 wins by playing rock"
    if player1.gesture == "scissors" and player2.gesture == "paper":
        return "Player 1 wins by playing scissors"
    if player1.gesture == "paper" and player2.gesture == "scissors":
        return "Player 2 wins by playing scissors"
    if player1.gesture == "rock" and player2.gesture == "paper":
        return "Player 2 wins by playing paper"
    if player1.gesture == "paper" and player2.gesture == "rock":
        return "Player 1 wins by playing paper"
    if player1.gesture == "rock" and player2.gesture == "rock":
        return "No winner, this game is a draw"
    if player1.gesture == "paper" and player2.gesture == "paper":
        return "No winner, this game is a draw"
    if player1.gesture == "scissors" and player2.gesture == "scissors":
        return "No winner, this game is a draw"
    else:
        return "What game are you trying to play?"
