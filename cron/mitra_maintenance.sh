#!/bin/bash
cd /root/dir/
rm -rf *.tmp *.out *.log
tmux list-sessions -F '#S' | grep 'imbg_' | xargs -I {} tmux kill-session -t {}
find logs/ -type f -mtime +3 -delete
touch .mitra_alive
