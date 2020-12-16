""" @package app
This is the flask application for the Sonos Controller.
"""
from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

from app import routes
