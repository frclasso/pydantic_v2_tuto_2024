# PyEnv
# ==========================================================================
## install
pyenv install 3.10

## create
pyenv virtualenv 3.10 <nome do projeto>

## Ativar o ambiente virtual
pyenv activate <nome do projeto>

# ===========================================================================
# Git hub
cd ~/.ssh && ssh-keygen
# On Linux run: 
cat id_rsa.pub

git config --global user.name
git config --global user.email

# If the user has generated a ssh public/private key pair set before

#     check which key have been authorized on your github or gitlab account settings
#     determine which corresponding private key must be associated from your local computer

eval $(ssh-agent -s)

# define where the keys are located
ssh-add ~/.ssh/wsl_idsa
/home/blueshift/.ssh/wsl_idsa

# More extensive troubleshooting and even automated fixing can be done with:
ssh -vT git@github.com

# Alternatively, according to below comments, we could issue:
ssh -vT git@gitlab.com

# Basic Commands:

sudo docker info                                 —  shows docker status and configuration
sudo docker ps                                   — show docker containers
sudo docker ps -l                               — show “latest” docker container -l = lower case L
sudo docker ps -a                               — show “all” docker container; even those not running
sudo docker images                           — show docker images (and tags)
sudo docker run -it <container> <app>       — connect / login to work interactively on container
systemctl status docker                     — show status and log for docker  <CTRL-C> to exit
sudo systemctl enable docker          — enable docker <not usually needed> using system control
sudo systemctl start docker             —  start docker <if it was stopped>
sudo service docker stop                  — Stop docker service
sudo service docker start                 — Start docker service
sudo service docker restart              — restart docker service
sudo usermod -aG docker <AdminUser>     — Add the <AdminUser> to Linux Authorized users for docker replace <AdminUser> with your username must log out and log back in for it to take affect

# ==========================================

sudo dockerd
sudo service --status-all 
sudo service docker start

# or

sudo systemctl start docker
sudo systemctl enable docker
sudo systemctl restart docker

# create
docker create --name postgres_container -p 6432:5432 -e POSTGRES_PASSWORD=meidouzangetsuha postgres

# start
docker start postgres_container

# log
docker logs -f postgres_container

# run and connecting to postgres
docker exec -it postgres_container psql -U postgres


# Dockerfile =========================================
## Build 
docker build -t web:latest .
## run
docker run -d --name <nome do container> -e "PORT=8765" -e "DEBUG=0" -p 8007:8765 web:latest

# docker stop
docker stop django-heroku
# docker delete
docker rm django-heroku

# ==================  POSTGRES ========================

# Switching Over to the postgres Account
sudo -i -u postgres
psql

- exit:
\q

# Step 4 — Creating a New Database
createdb sammy
ou
sudo -u postgres createdb databasename


## Checking if Postgres Service is Installed

### 2.1 Check if Postgres is Active

sudo systemctl is-active postgresql

You should see : active

### 2.2 Check if Postgres is enabled

sudo systemctl is-enabled postgresql

You should see : enabled

### 2.3 Check Postgres Service status

sudo systemctl status postgresql







# Apache Hive
## create database for hive
CREATE DATABASE metastore;

# create user
CREATE USER hive WITH ENCRYPTED PASSWORD '#AmorDaMinhaVida2022';

# Grant access
GRANT ALL ON DATABASE  metastore TO hive;

# run on terminal to connect to mestaore databse
psql -h localhost -p 6432 -d metastore -U hive -W

# reset passord
pg_ctl -D "C:\Program Files\PostgreSQL\15\data" restart  
psql -U postgres
ALTER USER postgres WITH PASSWORD '#AmorDaMinhaVida2022';



