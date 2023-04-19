"""@brief the routes for Flask application
"""
import hashlib
import json
import time

import requests
from flask import render_template, url_for
from soco import SoCo
from app import app

app.config.from_pyfile("settings.py")
sonos = SoCo(app.config["SPEAKER_IP"])


def gen_sig():
    """@brief return the MD5 checksum """
    return hashlib.md5(
        (
            app.config["ROVI_API_KEY"]
            + app.config["ROVI_SHARED_SECRET"]
            + repr(int(time.time()))
        ).encode("utf-8")
    ).hexdigest()


def get_track_image(artist, album):
    """@brief get the track image from Rovi """
    blank_image = url_for("static", filename="img/blank.jpg")
    if "ROVI_SHARED_SECRET" not in app.config:
        return blank_image
    if "ROVI_API_KEY" not in app.config:
        return blank_image

    headers = {"Accept-Encoding": "gzip"}
    req = requests.get(
        "http://api.rovicorp.com/recognition/v2.1/music/match/album?apikey="
        + app.config["ROVI_API_KEY"]
        + "&sig="
        + gen_sig()
        + "&name= "
        + album
        + "&performername="
        + artist
        + "&include=images&size=1",
        headers=headers,
        timeout=30,
    )

    if req.status_code != requests.codes.ok:
        return blank_image

    result = json.loads(req.content)
    try:
        return result["matchResponse"]["results"][0]["album"]["images"][0]["front"][3]["url"]
    except (KeyError, IndexError):
        return blank_image


def current_track():
    """@brief get the current track information from Sonos """
    track = sonos.get_current_track_info()
    track["title"] = track["title"][:30]
    track["artist"] = track["artist"][:30]
    return track


@app.route("/play")
def play():
    """@brief the play function """
    sonos.play()
    return "Ok"


@app.route("/pause")
def pause():
    """@brief the pause function """
    sonos.pause()
    return "Ok"


@app.route("/following")
def following():
    """@brief the following function """
    sonos.next()
    return "Ok"


@app.route("/previous")
def previous():
    """@brief the previous function """
    sonos.previous()
    return "Ok"


@app.route("/volume")
def volume():
    """@brief get the actual volume """
    vol = sonos.volume
    return vol


@app.route("/volume_up")
def volume_up():
    """@brief the volume up function """
    sonos.set_relative_volume(10)
    return "Ok"


@app.route("/volume_down")
def volume_down():
    """@brief the volume down function """
    sonos.set_relative_volume(-10)
    return "Ok"


@app.route("/volume_mute")
def volume_mute():
    """@brief the mute function """
    sonos.mute = True
    return "Ok"


@app.route("/volume_unmute")
def volume_unmute():
    """@brief the unmute function """
    sonos.mute = False
    return "Ok"


@app.route("/track_01")
def track_01():
    """@brief switch to new track """
    sonos.play_uri('http://mp3stream1.apasf.apa.at:8000', title='FM4.ORF.AT', force_radio=True)
    return "Ok"


@app.route("/track_02")
def track_02():
    """@brief switch to new track """
    sonos.play_uri('http://streams.radiopsr.de/psr-live/mp3-192/mediaplayer', title='Radio PSR Live', force_radio=True)
    return "Ok"


@app.route("/track_03")
def track_03():
    """@brief switch to new track """
    sonos.play_uri('http://nrj.de/sachsen', title='Energy Sachsen', force_radio=True)
    return "Ok"


@app.route("/track_04")
def track_04():
    """@brief switch to new track """
    sonos.play_uri('http://stream.sunshine-live.de/live/mp3-192', title='Sunshine Live', force_radio=True)
    return "Ok"


@app.route("/info-light")
def info_light():
    """@brief the info-light function """
    track = current_track()
    return json.dumps(track)


@app.route("/info")
def info():
    """@brief the info function """
    track = current_track()
    track["image"] = get_track_image(track["artist"], track["album"])
    transport = sonos.get_current_transport_info()
    track["playing"] = transport["current_transport_state"] != "STOPPED"
    track["mute"] = sonos.mute
    return json.dumps(track)


@app.route("/")
@app.route('/index')
def index():
    """@brief the index function """
    track = current_track()
    track["image"] = get_track_image(track["artist"], track["album"])
    return render_template("index.html", track=track)
