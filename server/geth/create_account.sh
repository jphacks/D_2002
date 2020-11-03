#! /bin/sh
openssl rand -hex 14 >> data/password1.txt
openssl rand -hex 14 >> data/password2.txt
geth --datadir data --password data/password1.txt account new
geth --datadir data --password data/password2.txt account new