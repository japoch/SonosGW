""" @package app
This is the flask application for the Sonos Controller.
"""
from flask import Flask

app = Flask(__name__)

# pylint: disable=wrong-import-position
from app import routes
