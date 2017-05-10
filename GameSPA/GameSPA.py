import json
from flask import render_template, request
from flask.views import MethodView
from python_cowbull_game.GameObject import GameObject


class GameSPA(MethodView):
    def get(self):
        digits = GameObject.digits_used
        guesses = GameObject.guesses_allowed
        game_modes = str([mode for mode in GameObject.digits_used])\
            .replace('[','').replace(']','').replace("'",'')
        table = []
        for mode in game_modes:
            table.append({
                "mode": mode,
                "digits": digits[mode],
                "guesses": guesses[mode]
            })

        return render_template(
            "index.html",
            digits=digits,
            guesses=guesses,
            game_modes=game_modes,
            modes_table=table
        )
