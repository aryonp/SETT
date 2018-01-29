#!/bin/bash
sudo apt install -y python-pip
pip install speedtest-cli
mkdir -p /var/SETT/
cp sett.py /var/SETT/
crontab -l > settcron
echo "30 10,15 * * * python /var/SETT/sett.py" >> settcron
crontab settcron
rm settcron
