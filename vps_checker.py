import json
import socket

def get_status():
    with open("config/vps.json") as f:
        vps_list = json.load(f)["vps_list"]

    result = []
    for vps in vps_list:
        s = socket.socket()
        s.settimeout(1)
        try:
            s.connect((vps["ip"], 22))
            result.append(f"[{vps['name']}] 🟢 Online")
        except:
            result.append(f"[{vps['name']}] 🔴 Offline")
        s.close()
    return "\n".join(result)
