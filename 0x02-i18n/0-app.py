#!/usr/bin/env python3
"""
This is our python module
"""
from flask import Flask, render_template
"""
These are flask and flask babel modules
"""


app = Flask(__name__)


@app.route('/')
def root():
    """
    This is the root
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(debug=True)
