#!/bin/bash
set -e
set -o pipefail

# Install Docker if it is not installed
if ! type docker > /dev/null 2>&1; then
  echo "Docker is not installed. Installing Docker..."
  sudo apt-get update
  sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common
  curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
  sudo add-apt-repository -y "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
  sudo apt update
  apt-cache policy docker-ce
  sudo apt install -y docker-ce
else
  echo "Docker is already installed."
fi

# Install Docker Compose if it is not installed
if ! type docker-compose > /dev/null 2>&1; then
  echo "Docker Compose is not installed. Installing Docker Compose..."
  sudo curl -L "https://github.com/docker/compose/releases/download/v2.19.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
  sudo chmod +x /usr/local/bin/docker-compose
else
  echo "Docker Compose is already installed."
fi

echo "Starting Docker Compose..."
sudo docker-compose -f docker-compose.yml down
sudo docker-compose -f docker-compose.yml up --build -d
