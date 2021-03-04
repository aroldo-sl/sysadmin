# sudo apt install --fix-missing apt-transport-https
# sudo apt install --fix-missing  curl
echo "deb [arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main" | sudo tee /etc/apt/sources.list.d/brave-browser-release.list

