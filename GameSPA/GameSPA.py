import json
import requests
from initialization_package import app
from flask import render_template, request
from flask.views import MethodView
from python_cowbull_game.GameObject import GameObject


class GameSPA(MethodView):
    def get(self):
        cowbull_url = "{}/modes".format(app.config.get('cowbull_url', None))
        if cowbull_url is None:
            raise ValueError("CowBull URL is Null!")

        table = None
        r = requests.get(url=cowbull_url)

        if r.status_code != 200:
            table = [{"mode": "Game is unavailable", "digits": "n/a", "guesses": "n/a"}]
        else:
            table = r.json()

        game_modes = str([mode["mode"] for mode in table]).replace('[','').replace(']','').replace("'","")

        return render_template(
            "index.html",
            digits=0,
            guesses=0,
            game_modes=game_modes,
            modes_table=table
        )
