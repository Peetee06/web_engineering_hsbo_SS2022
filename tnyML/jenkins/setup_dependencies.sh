#!/bin/bash

curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs
cd ${WORKSPACE}/tnyML
sudo npm install
sudo npm install -g @angular/cli