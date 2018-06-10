#!/bin/bash
sudo apt install -y speedtest-cli
mkdir -p /var/SETT/
curl -fsSL https://raw.githubusercontent.com/aryonp/SETT/master/sett.py > /var/SETT/sett.py
crontab -l > settcron
echo "30 10,15 * * * python /var/SETT/sett.py" >> settcron
crontab settcron
rm settcron
