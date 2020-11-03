# CHAINED BOX
Branch: master  
![Build Status](https://travis-ci.org/jphacks/D_2002.svg?branch=master)  
Branch: develop  
![Build Status](https://travis-ci.org/jphacks/D_2002.svg?branch=develop)  

<!-- [![IMAGE ALT TEXT HERE](https://jphacks.com/wp-content/uploads/2020/09/JPHACKS2020_ogp.jpg)](https://www.youtube.com/watch?v=G5rULR53uMk) -->

![eye-catching](./docs/eye-catching.jpeg)

## チーム名
## Team Name
### LSM-NAIST
### 私たちについて
### About Us
- We are master's students of Large-Scale Systems Management Lab., Nara Institute Science and Technology, Japan.
## 製品概要
## Product Outline
![product](./docs/product.jpeg)
### 背景(製品開発のきっかけ、課題等） 
### Background
![architecture](./docs/honesty_stand.jpeg)
Honesty stands are unmanned stores. As you can guess form the word “honesty”, the buyers are expected to be “honest”. But sometimes, the merchandises or the cash from the sales are stolen by dishonest thieves. The result shouldn't be a surprise to anyone. Billy Joel sings "Honesty is a such lonely word. Everyone is so untrue". Protecting the merchandises and the cash with existing vending machines is one solution, but the price of them is high. Therefore, sales are often not worth the investment. Therefore, we propose a simple and low-cost smart IoT box named “Chained Box”. 
### 製品説明（具体的な製品の説明）
### Product Description
Chained Box is a smart IoT box controlled by a blockchain. It enables to protect the the merchandises and the sales.
Buyers can pay for the merchandise with electric payment (crypto currency).
Sellers can receive the payment safely.
And, since the sales history is stored in the blockchain, the sellers are free from bookkeeping.
They can focus more efficiently on their main business. 

### 使用方法
### How to Use
You can use Chained Box as following steps.  
1. Access our web page in your browser. (Chrome is strongly recommended.)  
1. Lock or unlock your box in the menu page.



### その他のユースケース
### Other Use Cases
![architecture](./docs/use_cases.jpeg)
- Delivery
- Sharing
- Traceability

### 特長
### Advantages
![architecture](./docs/advantages.jpeg)
#### 1. Data Security
- Blockchains are difficult to change maliciously. 
- Blockchains are maintained by a peer-to-peer network. The system keeps running even if one node goes down. 
#### 2. Electric Payment
- You can pay with crypto-currency.
- A bank account or cash are not needed.
#### 3. Automation
- Smart contracts (as known as the feature of Ethereum) enable the automation of contracts.

### 解決出来ること
### Solutions
### 今後の展望
### Future Work
### 【予定】 注力したこと（こだわり等）
### 【Planned】 Focused Points
* Make the Data Secure
    - We use the Ethereum blockchain. 
* Make it Easy to Use
    - We develop the web-based user interface.
* Make the System Simple and Small
    - We use single board computers to make the system simple and small. The features give the box portability.
* Make the Box Beautiful
    - We give the box cool looks.

## 開発
## Development
### システムの構成
### System Architecture
![architecture](./docs/architecture.jpeg)

### 活用した技術
### Used Technologies
* Database with a Blockchain
* IoT with Single Board Computers

#### フレームワーク・ライブラリ・モジュール
#### Frameworks, Libraries, Modules
* Software
    - Web Server (WS)
        - Nginx: Web server and reverse proxy
    - Web Application (WA)
        - Django: Python-based web framework
    - Blockchain (BC)
        - Ethereum
            - Go Ethereum: Official Golang implementation of the Ethereum protocol
    - Lock Controller (LC)
        - Self-made program
            - Python: Programing language
            - Web3: Python library for interacting with Ethereum
    - Environment Setup
        - Docker: Platform of container virtualization
        - Docker-compose: Orchestration tool for Docker

#### デバイス
#### Devices
* Hardware
    - Host (WS/WA/BC)
        - ODROID-N2: Single board computer with Arm 64-bit, OS (Ubuntu 20.04)
    - Host (LC/BC)
        - Raspberry Pi: Single board computer with Arm 32-bit, OS (Raspbian buster 10)
    - Lock Actuator
        - SG-90: Servo motor
    - Display
        - Longruner 7inch LCD Display 1024 * 600: Display  
    - Battery (Raspberry Pi, Mini Display)
        - ELECOM Mobile Battery 6000mAh, 5V, 3A: Mobile Battery
        - Anker PowerCore 10000mAh, 5V, 2.4A: Mobile Battery

### 独自技術 
### Our Own Technologies
#### ハッカソンで開発した独自機能・技術
### Our Own Features Made in this Hackathon
* 独自で開発したものの内容をこちらに記載してください
* 特に力を入れた部分をファイルリンク、またはcommit_idを記載してください。

#### 製品に取り入れた研究内容（データ・ソフトウェアなど）（※アカデミック部門の場合のみ提出必須）
#### Applied Contents from our Research
* Blockchain
    - Substitute  a blockchain for a relational database
