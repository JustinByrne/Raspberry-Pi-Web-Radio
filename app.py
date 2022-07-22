#!/usr/bin/python3

import subprocess
from flask import Flask, render_template, redirect

app = Flask(__name__)
process = None
currentStation = 'No station selected'

@app.route('/')
def index():
    global currentStation

    return render_template('index.html', currentStation=currentStation)

@app.route('/play/<stationName>')
def playRadio(stationName):
    global process
    global currentStation

    # station = getStationUrl(stationName)
    currentStation = stationName

    # process = subprocess.Popen(
    #     [
    #         'mplayer',
    #         station,
    #         '-softvol',
    #         '-volume',
    #         '50'
    #     ],
    #     stdin=subprocess.PIPE,
    #     stdout=None,
    #     stderr=None,
    #     bufsize=0
    # )

    return redirect('/')

@app.route('/stop')
def stopRadio():
    global process
    global currentStation

    currentStation = 'No station selected'

    # if process is not None:
    #     process.stdin.write('q')

    return redirect('/')

@app.route('/volume-up')
def volumeUp():
    global process

    # if process is not None:
    #     process.stdin.write('*')

    return redirect('/')

@app.route('/volume-down')
def volumeDown():
    global process

    # if process is not None:
    #     process.stdin.write('/')

    return redirect('/')

@app.route('/play-pause')
def togglePlay():
    global process

    # if process is not None:
    #     process.stdin.write('p')

    return redirect('/')

def getStationUrl(stationName):
    return 'hello'

if __name__ == '__main__':
    app.run()