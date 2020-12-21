#!/bin/bash
# download and install latest geckodriver for linux or mac.
# required for selenium to drive a firefox browser.

install_dir="/usr/local/bin"

# Setup for downloading the latest file
json=$(curl -s https://api.github.com/repos/mozilla/geckodriver/releases/latest)
tagName=$(echo "${json}" | jq .tag_name) && tagName=${tagName//\"}

# Downloads and installs
wget "https://github.com/mozilla/geckodriver/releases/download/${tagName}/geckodriver-${tagName}-linux64.tar.gz" 
wait
sleep 5
tar -xzf "geckodriver-${tagName}-linux64.tar.gz"
rm geckodriver-${tagName}-linux64.tar.gz
chmod +x geckodriver
mv geckodriver "$install_dir"
echo "installed geckodriver binary in $install_dir"
ls ${install_dir} | grep "geckodriver"
