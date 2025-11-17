#!/bin/bash
set -e
export DEBIAN_FRONTEND=noninteractive

REPO_URL="git@gitlab.com:Vitaliy911/my-petclinic.git"
PROJECT_DIR="project"
APP_DIR="/home/appuser/app"

sudo apt-get update -y
sudo apt-get install -y openjdk-11-jdk git maven

sudo id -u appuser &>/dev/null || sudo useradd -m -s /bin/bash appuser
sudo -u appuser mkdir -p $APP_DIR
cd /home/appuser

sudo -u appuser git clone $REPO_URL $PROJECT_DIR

cd $PROJECT_DIR
sudo -u appuser chmod +x mvnw
sudo -u appuser ./mvnw package -DskipTests
cp target/*.jar $APP_DIR/
sudo -u appuser nohup java -jar $APP_DIR/*.jar > /home/appuser/app.log 2>&1 &

echo "PetClinic запущено, лог збережено в /home/appuser/app.log"

echo -e "Host gitlab.com\n\tStrictHostKeyChecking no\n\tIdentityFile /home/appuser/.ssh/id_ed25519\n" | sudo tee /home/appuser/.ssh/config
sudo chown appuser:appuser /home/appuser/.ssh/config
sudo chmod 600 /home/appuser/.ssh/config

