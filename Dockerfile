FROM python:3.8-bullseye

RUN pip3 install online-judge-tools &&\
  oj --version

RUN apt-get update -yqq &&\
  apt-get install -yqq npm &&\
  npm install -g atcoder-cli &&\
  acc --version
