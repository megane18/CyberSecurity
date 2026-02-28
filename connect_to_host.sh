#!/bin/bash

echo "Showing the current directory: $(pwd)"
echo "========= We need to connect to the remote host ========="

stdbuf -oL ssh -tt -i ~/.ssh/key hacker@dojo.pwn.college 'echo "========= SSH CONNECTED: entering /challenge/run ========="; /challenge/run' 2>&1 | tee -a ssh_connection.log
# /challenge/run <<'INNER'
# set -euo pipefail

# echo "========= PROOF: I am on the remote host ========="
# echo "remote_user=$(whoami)"
# echo "remote_host=$(hostname)"
# echo "remote_pwd=$(pwd)"
# ip addr | sed -n '1,120p'
# date

# echo "========= Connected to the remote host ========="

# echo "========= Scanning all 254 possible hosts ========="
# subnet="10.0.0"
# port="31337"

# for item in {1..254}; do
#     IP="$subnet.$item"
#     echo "Scanning $IP:$port"
#     if nc -z -w 1 "$IP" "$port" 2>&1; then
#         echo "Host $IP:$port is responding."
#     else
#         echo "Host $IP:$port is not responding."
#     fi
# done

# echo "========= Scanning completed :) ========="
# INNER
# EOF

if [ ${PIPESTATUS[0]} -ne 0 ]; then
    echo "SSH connection failed. Check ssh_connection.log for details."
    exit 1
fi

echo "========= Check ssh_connection.log for results ========="