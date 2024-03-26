#!/bin/bash

sudo systemctl stop alexa-assist 2>/dev/null
sudo systemctl disable alexa-assist 2>/dev/null
sudo rm /lib/systemd/system/alexa-assist.service 2>/dev/null
sudo cp service/alexa-assist.service /lib/systemd/system/
sudo systemctl enable alexa-assist
sudo systemctl start alexa-assist

