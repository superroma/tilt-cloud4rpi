from os import uname
from socket import gethostname
import sys
import time
import cloud4rpi
import rpi
import tilt

# Put your device token here. To get the token,
# sign up at https://cloud4rpi.io and create a device.
DEVICE_TOKEN = '__YOUR_DEVICE_TOKEN__'

# Constants
DATA_SENDING_INTERVAL = 60  # secs
DIAG_SENDING_INTERVAL = 600  # secs
POLL_INTERVAL = 0.5  # 500 ms

temp = 20
gravity = 1000


def F2C(degreesF):
    return (degreesF - 32) / 1.8


def getTemp():
    return temp


def getGravity():
    return gravity


def main():
    beacon = tilt.getFirstTilt()
    temp = F2C(int(beacon['Temp'])) if beacon else None
    gravity = beacon['Gravity'] if beacon else None

    # Put variable declarations here
    variables = {
        'Gravity': {
            'type': 'numeric',
            'bind': getGravity
        },
        'Beer Temp': {
            'type': 'numeric',
            'bind': getTemp
        }
    }

    diagnostics = {
        'CPU Temp': rpi.cpu_temp,
        'IP Address': rpi.ip_address,
        'Host': gethostname(),
        'Operating System': " ".join(uname())
    }

    device = cloud4rpi.connect(DEVICE_TOKEN)
    device.declare(variables)
    device.declare_diag(diagnostics)

    device.publish_config()

    # Adds a 1 second delay to ensure device variables are created
    time.sleep(1)

    try:
        data_timer = 0
        diag_timer = 0
        while True:
            if data_timer <= 0:
                beacon = tilt.getFirstTilt()
                temp = F2C(int(beacon['Temp'])) if beacon else None
                gravity = beacon['Gravity'] if beacon else None
                device.publish_data()
                data_timer = DATA_SENDING_INTERVAL

            if diag_timer <= 0:
                device.publish_diag()
                diag_timer = DIAG_SENDING_INTERVAL

            time.sleep(POLL_INTERVAL)
            diag_timer -= POLL_INTERVAL
            data_timer -= POLL_INTERVAL

    except KeyboardInterrupt:
        cloud4rpi.log.info('Keyboard interrupt received. Stopping...')

    except Exception as e:
        error = cloud4rpi.get_error_message(e)
        cloud4rpi.log.error("ERROR! %s %s", error, sys.exc_info()[0])

    finally:
        sys.exit(0)


if __name__ == '__main__':
    main()
