from flask import render_template
from app import app
from modules import game
from modules.player import *

@app.route('/')
def home():
    return "Hello! Here are the rules: Rock wins over scissors - because rock smashes scissors. Scissors wins over paper - because scissors cut paper. Paper wins over rock - because paper covers rock. Same gesture is a tie. Are you ready to play?"

@app.route('/<player1>/<player2>')
def play_game(player1, player2):
    return f"1, 2, 3! {game.play_game(player1, player2)}"

