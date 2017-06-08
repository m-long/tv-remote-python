# Controller to execute lirc commands given a message
import lirc

def run(remote, payload_str):
    if "volume" in payload_str:
        # See if input contains a number. If yes, use first
        count = 1
        ints = [int(s) for s in payload_str.split() if s.isdigit()]
        if ints and ints[0] > 1:
            count = ints[0]
        if "up" in payload_str:
            lirc.volume_up(remote, count)
        elif "down" in payload_str:
            lirc.volume_down(remote, count)
        elif "mute" in payload_str:
            lirc.volume_mute(remote)
        else:
            print("Command not found...")
    elif "power" in payload_str:
        lirc.power(remote)
    elif "channel" in payload_str:
        # See if input contains a number. If yes, use first
        ints = [int(s) for s in payload_str.split() if s.isdigit()]
        if ints and ints[0] >=1:
            lirc.channel_set(remote, ints[0])
        elif any (word in payload_str for word in ["previous", "prev"]):
            lirc.channel_previous(remote)
        elif "up" in payload_str:
            lirc.channel_up(remote)
        elif "down" in payload_str:
            lirc.channel_down(remote)
    elif "source" in payload_str:
        if any (word in payload_str for word in ["cable", "tv"]):
            lirc.change_source_to_cable(remote)
        else:
            lirc.change_source(remote)
