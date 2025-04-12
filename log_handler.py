def get_log(task_id, username):
    try:
        with open(f"logs/{task_id}.txt") as f:
            data = f.read()
        if task_id.split("_")[1] != username:
            return "🔐 Not authorized."
        return data
    except:
        return "Log not found."
