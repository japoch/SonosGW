"""This script is an webfrontend for the
   Sonos Controller"""
from app import app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
