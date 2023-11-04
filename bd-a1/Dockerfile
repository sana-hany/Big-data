FROM ubuntu:latest

WORKDIR /home/doc-bd-a1/

RUN apt-get update && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends apt-utils software-properties-common wget \
    && apt-get install -y build-essential python3 python3-distutils \
    && wget --no-check-certificate https://bootstrap.pypa.io/get-pip.py \
    && python3 get-pip.py --trusted-host pypi.org --trusted-host files.pythonhosted.org

ENV DEBIAN_FRONTEND noninteractive \
    && DBCONF_NONINTERACTIVE_SEEN true

RUN apt-get install -y python3-pandas \
    && echo "Africa/Egypt" > /etc/timezone \
    && dpkg-reconfigure -f noninteractive tzdata

RUN apt-get install -y python3-sklearn \
    && echo "Africa/Egypt" > /etc/timezone \
    && dpkg-reconfigure -f noninteractive tzdata

RUN apt-get install -y python3-seaborn \
    && echo "Africa/Egypt" > /etc/timezone \
    && dpkg-reconfigure -f noninteractive tzdata

RUN apt-get install -y python3-matplotlib \
    && echo "Africa/Egypt" > /etc/timezone \
    && dpkg-reconfigure -f noninteractive tzdata

COPY . /home/doc-bd-a1/


  

