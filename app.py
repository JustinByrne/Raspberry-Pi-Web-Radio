#!/usr/bin/python3

import subprocess
import json
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)
process = None
currentStation = 'No station selected'
pause = False
volume = 50

#
#   Routes
#
@app.route('/')
def index():
    global currentStation
    global pause
    global volume

    stations = getAllStations()
    return render_template('index.html', currentStation=currentStation, pause=pause, volume=volume, stations=stations)

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
    adjustVolume('up')
    return redirect(url_for('index'))

@app.route('/volume-down')
def volumeDown():
    sendKeyPress('/')
    adjustVolume('down')
    return redirect(url_for('index'))

@app.route('/play-pause')
def togglePlay():
    global pause
    
    sendKeyPress('p')
    if pause == True:
        pause = False
    elif pause == False:
        pause = True
    return redirect(url_for('index'))


#
# Functions
#
def playStation(stationSlug):
    global process
    global volume

    stopPlaying()
    setCurrentStation(getStationName(stationSlug))
    process = subprocess.Popen(['mplayer', getStationUrl(stationSlug), '-softvol', '-volume', str(volume) ], \
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

def adjustVolume(direction):
    global volume

    if direction == 'up':
        volume = volume + 3
    
    if direction == 'down':
        volume = volume - 3
    
    if volume > 100:
        volume = 100
    
    if volume < 0:
        volume = 0

if __name__ == '__main__':
    app.run()