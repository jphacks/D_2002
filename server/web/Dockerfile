# Docker Hubにあるpythonイメージをベースにする
FROM python:3.6

# 環境変数を設定
ENV PYTHONUNBUFFERED 1

# requirements.txtを使ってパッケージをインストール
WORKDIR /work
ADD requirements.txt /work/
RUN pip install -r requirements.txt

# work/srcディレクトリをワークディレクトリに設定
WORKDIR /work/src
