# Raspberry Pi Web Radio

A python flask based web radio with the ability to play internet radio station

## Requirements

This site has a few system requirements. Majority of this are python related

* mplayer
* python 3
* pip 3
* python3-venv

## Installation

Download the repository to the raspberry pi

```bash
git clone https://github.com/JustinByrne/Raspberry-Pi-Web-Radio.git
```

Move into the directory

```bash
cd ./Raspberry-Pi-Web-Radio
```

Create a virtual environment

```bash
python3 -m venv raspberrypiwebradioenv
```

Activate the virtual environment

```bash
source raspberrypiwebradioenv/bin/activate
```

To install the requirements run the following

```bash
pip install -r requirements.txt
```

Then the station file needs to be configured, copy the example using the following

```bash
cp stations.json.example stations.json
```

### Adding the service

Firstly copy the service file

```bash
cp raspberrypiwebradio.service.example raspberrypiwebradio.service
```

Edit the service replacing `<username>` with your username this is usually `pi`. Then move the service to the services directory.

```bash
sudo mv raspberrypiwebradio.service /etc/systemd/system/raspberrypiwebradio.service
```

Enable the service to start on startup and start it

```bash
sudo systemctl enable raspberrypiwebradio.service
sudo systemctl start raspberrypiwebradio.service
```
