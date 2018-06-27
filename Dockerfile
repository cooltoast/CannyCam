FROM ubuntu:16.04

RUN mkdir -p /CannyCam
WORKDIR /CannyCam

RUN \
  apt-get update && \
  apt-get install -y -q python python-opencv

COPY xmls xmls
COPY canny.py canny.py
COPY haarcam.py haarcam.py
COPY cannycam.py cannycam.py

CMD python cannycam.py