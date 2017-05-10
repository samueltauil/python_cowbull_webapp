import json
import requests
from requests import exceptions
from initialization_package import app
from flask import render_template, request
from flask.views import MethodView
from python_cowbull_game.GameObject import GameObject


class GameSPA(MethodView):
    def get(self):
        game_modes = []
        table = None
        error_message = ""
        return_template = None
        r = None

        cowbull_url = "{}/modes".format(app.config.get('cowbull_url', None))
        if cowbull_url is None:
            raise ValueError("CowBull URL is Null!")

        try:
            r = requests.get(url=cowbull_url)
        except exceptions.ConnectionError as re:
            error_message = "Game is unavailable: {}.".format(str(re))

        if r is not None:
            if r.status_code != 200:
                table = [{
                    "mode": "Game is unavailable. Status code {}".format(r.status_code),
                    "digits": "n/a", "guesses": "n/a"
                }]
            else:
                table = r.json()

            game_modes = str([mode["mode"] for mode in table]).replace('[','').replace(']','').replace("'","")

            return_template = render_template(
                "index.html",
                digits=0,
                guesses=0,
                game_modes=game_modes,
                modes_table=table
            )
        else:
            return_template = render_template(
                "error.html",
                error_message=error_message
            )

        return return_template

    def post(self):
        pass