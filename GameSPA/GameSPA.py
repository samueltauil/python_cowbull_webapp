import json
import logging
import requests
from flask import render_template, request, Response
from flask.views import MethodView
from initialization_package import app
from requests import exceptions
from werkzeug.exceptions import BadRequest


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

    def put(self):
        # Check circuit breaker

        #
        # Get the JSON from the request
        #
        try:
            logging.debug('Attempting to load JSON from PUT request')
            json_dict = request.get_json()
            logging.debug('Loaded JSON. Returned: {}'.format(json_dict))

            key = json_dict.get('key', None)
            digits = json_dict.get('digits', [])
            if key is None or digits == []:
                raise BadRequest(
                    description="The JSON is malformed; either key is None or there are no digits."
                )
        except BadRequest as br:
            response = Response(
                response=json.dumps({
                    "status": 500,
                    "message": "Failed to respond to guess.",
                    "exception": str(br)
                }),
                status=500,
                mimetype="application/json"
            )
            return response

        cowbull_url = None
        try:
            cowbull_url = "{}/game"\
                .format(
                    app.config.get('cowbull_url', None)
                )
            if cowbull_url is None:
                raise BadRequest(description="CowBull URL is Null! The game cannot play!")
            logging.debug("Setting cowbull url to: {}".format(cowbull_url))
        except BadRequest as br:
            response = Response(
                response=json.dumps({
                    "status": 500,
                    "message": "Failed to respond to guess.",
                    "exception": str(br)
                }),
                status=500,
                mimetype="application/json"
            )
            return response

        r = None
        try:
            headers = {"Content-type": "application/json"}
            r = requests.post(url=cowbull_url, data=json.dumps(json_dict), headers=headers)
            logging.debug("XHR Request returned status {}".format(r.status_code))
        except Exception as e:
            response = Response(
                response=json.dumps({
                    "status": 400,
                    "message": "Failed to respond to guess.",
                    "exception": repr(e)
                }),
                status=500,
                mimetype="application/json"
            )
            return response

        try:
            if r is None:
                raise BadRequest(description="There was no response from the game server.")

            json_response = None
            try:
                json_response = r.json()
            except Exception as e:
                raise BadRequest(description="There was no JSON returned from the game server.")

            if r.status_code != 200:
                raise ValueError("Bad status code {}.".format(r.status_code))
        except ValueError as ve:
            response = Response(
                response=json.dumps({
                    "status": 500,
                    "message": "Failed to respond to guess.",
                    "exception": str(br)
                }),
                status=500,
                mimetype="application/json"
            )
            return response
        except BadRequest as br:
            response = Response(
                response=json.dumps({
                    "status": 500,
                    "message": "Failed to respond to guess.",
                    "exception": str(br)
                }),
                status=500,
                mimetype="application/json"
            )
            return response

        return Response(
            response=json.dumps(r.json()),
            status=r.status_code,
            mimetype="application/json"
        )
