#!/bin/bash
set -euo pipefail
DURATION="${1:-420}"

ssh -tt -i ~/.ssh/key hacker@dojo.pwn.college /challenge/run <<CMD
tcpdump -i eth0 port 31337 -w /tmp/cap.pcap &
PID=\$!
sleep $DURATION
kill -INT \$PID
wait \$PID || true
tshark -r /tmp/cap.pcap -Y "tcp.len>0 && tcp.port==31337" -T fields -e tcp.payload | tr -d "\\n" | xxd -r -p ; echo
exit
CMD