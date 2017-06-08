# Commands for lirc

import subprocess
from time import sleep

def power(remote):
    subprocess.Popen(["irsend", "SEND_ONCE", remote, "KEY_POWER"]) 
    print("Power...")

def volume_up(remote, count = 1):
    count = int(count)
    commands = ["KEY_VOLUMEUP"] * count
    tooltip = "Volume up"
    if count > 1: tooltip += " by " + str(count)
    print(tooltip + "...")
    for command in commands:
        subprocess.Popen(["irsend", "SEND_ONCE", remote, command])
        sleep(.25)

def volume_down(remote, count = 1):
    count = int(count)
    commands = ["KEY_VOLUMEDOWN"] * count
    tooltip = "Volume down"
    if count > 1: tooltip += " by " + str(count)
    print(tooltip + "...")
    for command in commands:
        subprocess.Popen(["irsend", "SEND_ONCE", remote, command])
        sleep(.25)

def volume_mute(remote):
    subprocess.Popen(["irsend", "SEND_ONCE", remote, "KEY_MUTE"]) 
    print("Mute...")

def channel_up(remote, count = 1):
    count = int(count)
    commands = ["KEY_CHANNELUP"] * count
    tooltip = "Channel up"
    if count > 1: tooltip += " by " + str(count)
    print(tooltip + "...")
    for command in commands:
        subprocess.Popen(["irsend", "SEND_ONCE", remote, command])
        sleep(.25)

def channel_down(remote, count = 1):
    count = int(count)
    commands = ["KEY_CHANNELDOWN"] * count
    tooltip = "Channel down"
    if count > 1: tooltip += " by " + str(count)
    print(tooltip + "...")
    for command in commands:
        subprocess.Popen(["irsend", "SEND_ONCE", remote, command])
        sleep(.25)

def channel_previous(remote):
    subprocess.Popen(["irsend", "SEND_ONCE", remote, "Pre-Ch"]) 
    print("Previous channel...")

def channel_set(remote, channel):
    if isinstance(channel, int):
        digits = list(str(channel))
        for digit in digits:
            command = str("KEY_" + digit)
            subprocess.Popen(["irsend", "SEND_ONCE", remote, command])
            sleep(.25)
        print("Channel changed to " + str(channel) + "...")

def change_source(remote):
    subprocess.Popen(["irsend", "SEND_ONCE", remote, "KEY_CYCLEWINDOWS"])
    sleep(.25)
    subprocess.Popen(["irsend", "SEND_ONCE", remote, "KEY_CYCLEWINDOWS"])
    sleep(.25)
    subprocess.Popen(["irsend", "SEND_ONCE", remote, "KEY_ENTER"])
    print("Chance source...")

def change_source_to_cable(remote):
    subprocess.Popen(["irsend", "SEND_ONCE", remote, "KEY_TV"]) 
    print("Chance source to cable...")
