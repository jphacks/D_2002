# Docker Hubにあるpythonイメージをベースにする
FROM python:3.8

# 環境変数を設定
ENV PYTHONUNBUFFERED 1

# requirements.txtを使ってパッケージをインストール
WORKDIR /work
ADD requirements.txt /work/
RUN apt-get update -y
RUN apt-get upgrade -y 
RUN apt-get -y install python3-tk
RUN pip3 install -U pip
RUN pip3 install -r requirements.txt

# work/srcディレクトリをワークディレクトリに設定
WORKDIR /work/src
