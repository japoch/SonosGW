""" @package app
This is the flask application for the Sonos Controller.
"""
from flask import Flask

app = Flask(__name__)

from app import routes
