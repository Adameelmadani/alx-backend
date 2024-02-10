#!/usr/bin/env python3
"""
This is our python module
"""
from flask import Flask, render_template
from flask_babel import Babel
"""
These are flask and flask babel modules
"""


class Config:
    """
    config class for flask application
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@app.route('/')
def root():
    """
    This is the root
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(debug=True)
