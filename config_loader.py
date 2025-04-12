import json
from datetime import datetime

def validate_key(key):
    with open("config/access_keys.json") as f:
        keys = json.load(f)
    for name, data in keys.items():
        if data['key'] == key:
            if datetime.strptime(data['expires'], "%Y-%m-%dT%H:%M") > datetime.now():
                return {"name": name, "role": data['role']}
    return None
