import logging
import os


def set_config(app=None):
    if app is None:
        raise ValueError("APP is undefined!!")

    #
    # Expected OS Env Vars (lower case):
    # LOGGING_FORMAT --> Python logging fmt     !! Default: "%(asctime)s %(levelname)s: %(message)s"
    # COWBULL_SERVER --> http://server_url      !! Note NO TRAILING /
    # COWBULL_PORT   --> 80                     !! Note integer
    # FLASK_HOST     --> 0.0.0.0                !! Only if using Flask to serve
    # FLASK_PORT     --> 5000                   !! "    "    "    "    "    "

    logging.basicConfig(
        level=logging.DEBUG,
        format=os.getenv(
            "logging_format",
            os.getenv(
                "LOGGING_FORMAT",
                "%(asctime)s %(levelname)s: %(message)s"
            )
        )
    )

    # Google App Environment configuration
    logging.debug("Setting COWBULL_SERVER")
    cowbull_server = os.getenv(
        "cowbull_host",
        os.getenv(
            "COWBULL_HOST",
            "localhost"
        )
    )
    app.config["cowbull_server"] = "cowbull-test-project.appspot.com" #cowbull_server
    logging.debug("Setting COWBULL_SERVER --> {}".format(app.config["cowbull_server"]))

    logging.debug("Setting COWBULL_PORT")
    cowbull_port = os.getenv(
        "cowbull_port",
        os.getenv(
            "COWBULL_PORT",
            5000
        )
    )
    app.config["cowbull_port"] = cowbull_port
    logging.debug("Setting COWBULL_PORT --> {}".format(app.config["cowbull_port"]))

    logging.debug("Setting FLASK_HOST")
    app.config["FLASK_HOST"] = os.getenv(
        "flask_host",
        os.getenv(
            "FLASK_HOST",
            "0.0.0.0"
        )
    )

    logging.debug("Setting FLASK_PORT")
    try:
        app.config["FLASK_PORT"] = int(os.getenv(
            "flask_port",
            os.getenv(
                "FLASK_PORT",
                8001
            )
        ))
    except ValueError:
        app.config["FLASK_PORT"] = 8001

    logging.debug("Setting COWBULL_VERSION")
    app.config["cowbull_version"] = "v0_1"
    logging.debug("Setting COWBULL_VERSION --> {}".format(app.config["cowbull_version"]))

    logging.debug("Setting COWBULL_URL")
    app.config["cowbull_url"] = "http://{}:{}/{}".format(
        app.config["cowbull_server"],
        app.config["cowbull_port"],
        app.config["cowbull_version"]
    )
    logging.debug("Setting COWBULL_URL --> {}".format(app.config["cowbull_url"]))

    logging.debug("COWBULL_SERVER : {}".format(app.config["cowbull_server"]))
    logging.debug("COWBULL_PORT   : {}".format(app.config["cowbull_port"]))
    logging.debug("COWBULL_VERSION: {}".format(app.config["cowbull_version"]))
    logging.debug("COWBULL_URL    : {}".format(app.config["cowbull_url"]))
    logging.debug("FLASK_HOST     : {}".format(app.config["FLASK_HOST"]))
    logging.debug("FLASK_PORT     : {}".format(app.config["FLASK_PORT"]))

