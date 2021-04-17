from flask import render_template, request
from app import app
from modules.game import Game
from modules.player import *

@app.route('/')
def home():
    return render_template('home.html', title='Home')

@app.route('/result', methods=["GET"])
def form():
    return render_template('result.html', title='Game Result', result="result")

@app.route('/result', methods=["POST"])
def game():
    player1 = request.form["player1"]
    player1_gesture = request.form["player1gesture"]
    new_player1 = Player(player1, player1_gesture)
    player2 = request.form["player2"]
    player2_gesture = request.form["player2gesture"]
    new_player2 = Player(player2, player2_gesture)
    rock_paper_scissors = Game(new_player1, new_player2)
    return render_template('result.html', title='Game Result', result=rock_paper_scissors.play_game(new_player1, new_player2))
    
    

