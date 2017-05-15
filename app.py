import logging
import os
from flask import render_template
from initialization_package import app
from GameSPA.GameSPA import GameSPA
from Utilities.set_config import set_config

# Set configuration
set_config(app=app)

# Add a game view. The game view is actually contained within a class
# based on a MethodView. See flask_controllers/GameController.py
game_view = GameSPA.as_view('Game')
app.add_url_rule(
    '/',
    view_func=game_view,
    methods=["GET", "POST", "PUT"]
)

if __name__ == "__main__":
    app.run\
        (
            host=app.config["FLASK_HOST"],
            port=app.config["FLASK_PORT"],
            debug=True
        )
