#!/bin/bash

# echo "Enter into the shell host"
echo "Showing the current directory: $(pwd)"
echo "========= We need to connect to the remote host ========="

ssh -t -i ~/.ssh/key hacker@dojo.pwn.college "/challenge/run" 2>&1 | tee -a ssh_connection.log

if [ ${PIPESTATUS[0]} -ne 0 ]; then
    echo "SSH connection failed. Please check the log for more details."
    exit 1
fi