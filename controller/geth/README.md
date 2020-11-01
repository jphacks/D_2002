# Installation Guide for Geth Server

## 1. Create account

```sh
docker-compose run geth sh create_account.sh
```

## 2. Copy genesis.json from src of server

server/geth/genesis.json ➡︎ controller/geth/genesis.json  

## 3. Create Genesis Block

```sh
docker-compose run geth sh init_geth.sh
```
