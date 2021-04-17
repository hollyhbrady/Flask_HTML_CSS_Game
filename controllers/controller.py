from flask import render_template
from app import app
from modules.game import *
from modules.player import *

@app.route('/')
def home():
    return render_template('home.html', title='Home')

@app.route('/<player1>/<player2>')
def game(player1, player2):
    play_game(player1, player2)
    return render_template('result.html', title='Game Result', result=play_game(player1, player2))
    
    

