FROM ubuntu:16.04

RUN mkdir -p /CannyCam
WORKDIR /CannyCam

RUN \
  apt-get update && \
  apt-get install -y -q python python-opencv

ADD xmls /CannyCam/xmls
ADD canny.py /CannyCam/canny.py
ADD haarcam.py /CannyCam/haarcam.py
ADD cannycam.py /CannyCam/cannycam.py

CMD python cannycam.py