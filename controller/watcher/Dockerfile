FROM resin/rpi-raspbian:buster

RUN apt-get update
RUN apt-get install python3 python3-pip python3-dev python3-setuptools gcc make vim

# 環境変数を設定
ENV PYTHONUNBUFFERED 1

# requirements.txtを使ってパッケージをインストール
WORKDIR /work
ADD requirements.txt /work/
RUN pip3 install -r requirements.txt

# work/srcディレクトリをワークディレクトリに設定
WORKDIR /work/src
