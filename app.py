#!/usr/bin/python3

import subprocess
import json
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)
process = None
currentStation = 'No station selected'

#
#   Routes
#
@app.route('/')
def index():
    global currentStation

    stations = getAllStations()
    return render_template('index.html', currentStation=currentStation, stations=stations)

@app.route('/play/<stationSlug>')
def play(stationSlug):
    playStation(stationSlug)
    return redirect(url_for('index'))

@app.route('/stop')
def stop():
    stopPlaying()
    return redirect(url_for('index'))

@app.route('/volume-up')
def volumeUp():
    sendKeyPress('*')
    return redirect(url_for('index'))

@app.route('/volume-down')
def volumeDown():
    sendKeyPress('/')
    return redirect(url_for('index'))

@app.route('/play-pause')
def togglePlay():
    sendKeyPress('p')
    return redirect(url_for('index'))


#
# Functions
#
def playStation(stationSlug):
    global process

    stopPlaying()
    setCurrentStation(getStationName(stationSlug))
    process = subprocess.Popen(['mplayer', getStationUrl(stationSlug), '-softvol', '-volume', '50' ], \
        stdin=subprocess.PIPE, \
        stdout=None, \
        stderr=None, \
        bufsize=0)

def stopPlaying():
    global process

    setCurrentStation('No station selected')
    sendKeyPress('q')
    process = None

def getStationName(stationSlug):
    file = open('stations.json')
    data = json.load(file)

    print(stationSlug)

    for station in data['stations']:
        if station['slug'] == stationSlug:
            return station['name']

def getStationUrl(stationSlug):
    file = open('stations.json')
    data = json.load(file)

    for station in data['stations']:
        if station['slug'] == stationSlug:
            return station['url']

def setCurrentStation(stationName):
    global currentStation

    if currentStation is not stationName:
        currentStation = stationName

def sendKeyPress(key):
    global process

    if process is not None:
        process.stdin.write(format(key).encode('utf-8'))

def getAllStations():
    file = open('stations.json')
    data = json.load(file)
    return data['stations']

if __name__ == '__main__':
    app.run()