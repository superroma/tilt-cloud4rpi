# test BLE Scanning software
# jcs 6/8/2014

import blescan as blescan
import sys

import bluetooth._bluetooth as bluez


def getFirstTilt():
    dev_id = 0
    try:
        sock = bluez.hci_open_dev(dev_id)
        print "ble thread started"

    except:
        print "error accessing bluetooth device..."
        sys.exit(1)

    blescan.hci_le_set_scan_parameters(sock)
    blescan.hci_enable_le_scan(sock)

    tilts = {
        'a495bb10c5b14b44b5121370f02d74de': 'Red',
        'a495bb20c5b14b44b5121370f02d74de': 'Green',
        'a495bb30c5b14b44b5121370f02d74de': 'Black',
        'a495bb40c5b14b44b5121370f02d74de': 'Purple',
        'a495bb50c5b14b44b5121370f02d74de': 'Orange',
        'a495bb60c5b14b44b5121370f02d74de': 'Blue',
        'a495bb70c5b14b44b5121370f02d74de': 'Pink'
    }
    result = {}

    returnedList = blescan.parse_events(sock, 100)
    for beacon in returnedList:
        if (beacon['uuid'] in tilts):
            tiltColor = tilts[beacon['uuid']]
            result = {
                'Color': tiltColor,
                'Temp': beacon['major'],
                'Gravity': beacon['minor']
            }
    return result
