# Mitra-X Drift Network

Run powerful VPS-managed tasks via Telegram Bot.

## Usage

1. Start bot: `/start <access-key>`
2. Run task: `/imgb <ip> <port> <duration>`
3. Check logs: `/log <task-id>`
4. VPS status: `/status`

## Folder Setup

- `config/`: Your team, VPS & access keys
- `logs/`: Logs saved per task
- `cron/mitra_maintenance.sh`: Run daily via `crontab`

## Notes

- VPS must have `freeroot`, `./root.sh`, and `M/`
- Required: Python 3.10+, paramiko, tmux
