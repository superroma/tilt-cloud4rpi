# tilt-cloud4rpi
Send data from [Tilt hydrometer](https://tilthydrometer.com) to the [cloud4rpi.io](https://cloud4rpi.io) control panel. Works on Rasbperry Pi.

## Installation
On a Rasbperry Pi, make sure system is up-to date:
```sh
sudo apt update && sudo apt upgrade
```
Install prerequisites
```sh
sudo apt install git python python-pip
```
Install cloud4rpi python package
```sh
sudo pip install cloud4rpi
```
Then clone this repo
```sh
git clone https://github.com/superroma/tilt-cloud4rpi
cd tilt-cloud4rpi
```
Edit `control.py` and replace `__YOUR_DEVICE_TOKEN__` with device token given to you when adding new device at [cloud4rpi.io](https://cloud4rpi.io)

## Running
Just run
```sh
sudo python control.py
```
Your cloud4rpi.io device page should show **Gravity** and **Beer Temp** values.

## Running as a service
Use provided `service_install.sh` script to run `control.py` as a service.
```sh
sudo bash service_install.sh control.py
```
Now you can start|stop|restart this service by running systemctl command like this:
```sh
sudo systemctl start cloud4rpi.service
```





