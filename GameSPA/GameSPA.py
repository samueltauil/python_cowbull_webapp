import requests
from requests import exceptions
from initialization_package import app
from flask import render_template, request
from flask.views import MethodView


class GameSPA(MethodView):
    def get(self):
        error_message = ""
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
                app.config["mode_table"] = table

            game_modes = str([mode["mode"] for mode in table]).replace('[','').replace(']','').replace("'","")

            return_template = render_template(
                "index.html",
                digits=0,
                guesses=0,
                game_modes=game_modes,
                modes_table=table,
                game_url="{}/game".format(app.config.get("cowbull_url", ""))
            )
        else:
            return_template = render_template(
                "error.html",
                error_message=error_message
            )

        return return_template

    def post(self):
        mode = request.form.get("mode", "normal")
        game_modes = []
        table = None
        error_message = ""
        return_template = None
        r = None

        cowbull_url = "{}/game?mode={}"\
            .format(
                app.config.get('cowbull_url', None),
                mode
            )
        if cowbull_url is None:
            raise ValueError("CowBull URL is Null!")

        try:
            r = requests.get(url=cowbull_url)
        except exceptions.ConnectionError as re:
            error_message = "Game is unavailable: {}.".format(str(re))

        if r is not None:
            if r.status_code != 200:
                return_template = render_template(
                    "error.html",
                    error_message="For some reason, it hasn't been possible "
                                  "to get a game. The status code was: {}"
                    .format(r.status_code)
                )
            else:
                game_object = r.json()
                return_template = render_template(
                    "playgame.html",
                    digits=game_object.get("digits", None),
                    guesses=game_object.get("guesses", None),
                    key=game_object.get("key", None),
                    served_by=game_object.get("served-by", "None"),
                    modes_table=app.config.get("mode_table", []),
                    game_url="{}/game".format(app.config.get("cowbull_url", ""))
                )
        else:
            return_template = render_template(
                "error.html",
                error_message="For some reason, it hasn't been possible "
                              "to get a game. The status code was: {}"
                    .format(r.status_code)
            )

        return return_template
