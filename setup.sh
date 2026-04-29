#!/bin/bash
sudo apt-get update -y
sudo apt-get install -y python3-pip
pip3 install -r requirements.txt
python3 -m playwright install chromium
mkdir -p results payloads
echo '[+] RvndmXSS ELITE setup completed'
