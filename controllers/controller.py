from flask import render_template
from app import app
from modules import game
from modules.player import *

@app.route('/')
def home():
    return render_template('home.html', title='Home')

@app.route('/<player1>/<player2>')
def play_game(player1, player2):
    return render_template('result.html', title='Game Result')
    
    
    f"1, 2, 3! {game.play_game(player1, player2)}"

