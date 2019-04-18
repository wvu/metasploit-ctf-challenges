# https://github.com/wvu/ye-olde-bsd

FROM ubuntu:16.04
LABEL author="wvu"

WORKDIR /simh

RUN apt-get update && \
    apt-get -y install \
      build-essential \
      unzip \
      wget && \
    rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*

RUN wget https://github.com/simh/simh/archive/master.zip && \
    unzip master.zip && \
    make -C simh-master vax780 && \
    cp simh-master/BIN/vax780 . && \
    rm -rf simh-master master.zip

COPY . .

RUN gunzip *.gz && \
    chown -R nobody:nogroup . && \
    setcap cap_net_bind_service+ep vax780 && \
    apt-get -y --autoremove purge \
      build-essential \
      unzip \
      wget

EXPOSE 25 79

USER nobody
CMD ["./vax780", "boot.ini"]
