import paramiko

def connect_and_run(vps, command):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(vps["ip"], username=vps["user"], password=vps["pass"])
        stdin, stdout, stderr = ssh.exec_command(command)
        return stdout.read().decode()
    except Exception as e:
        return f"[{vps['name']}] ❌ Connection failed: {e}"
