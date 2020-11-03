#! /bin/sh
openssl rand -hex 14 >> data/password.txt
openssl rand -hex 14 >> data/password.txt
geth --datadir data --password data/password.txt account new