# Instauration Guide for Geth

1. Create account
```sh
docker-compose run geth sh create_account.sh
```

2. Create genesis.json
```sh
docker-compose run geth sh create_genesis_json.sh
```
* Please specify a network name to administer (no spaces, hyphens or capital letters please)
\> genesis

* What would you like to do? (default = stats)
 1. Show network stats
 2. Configure new genesis
 3. Track new remote server
 4. Deploy network components
\> 2

* What would you like to do? (default = create)
 1. Create new genesis from scratch
 2. Import already existing genesis
\> 1

* Which consensus engine to use? (default = clique)
 1. Ethash - proof-of-work
 2. Clique - proof-of-authority
\> 2

* How many seconds should blocks take? (default = 15)
\> 3

* Which accounts are allowed to seal? (mandatory at least one)
\> 0x5261084afab11a6845d8292d4469ce54976f71a6
\> 0x

Please input your address you generated former process.
e.g. 0x5261084afab11a6845d8292d4469ce54976f71a6

* Which accounts should be pre-funded? (advisable at least one)
\> 0x5261084afab11a6845d8292d4469ce54976f71a6
\> 0x

Please input your address you generated former process.

* Should the precompile-addresses (0x1 .. 0xff) be pre-funded with 1 wei? (advisable yes)
\> no

* Specify your chain/network ID if you want an explicit one (default = random)
\> 32414

* What would you like to do? (default = stats)
 1. Show network stats
 2. Manage existing genesis
 3. Track new remote server
 4. Deploy network components
\> 2

 1. Modify existing configurations
 2. Export genesis configurations
 3. Remove genesis configuration
\> 2

Please quit with Ctrl+c.
3. Create Genesis Block

4.