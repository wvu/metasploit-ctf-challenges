# https://github.com/wvu/ye-olde-bsd

FROM alpine AS simh

WORKDIR /simh

RUN apk --no-cache add -t build-essential \
      gcc \
      libc-dev \
      make

RUN wget https://github.com/simh/simh/archive/master.tar.gz && \
    tar xf master.tar.gz && \
    make -C simh-master vax780 && \
    cp simh-master/BIN/vax780 . && \
    rm -rf simh-master master.tar.gz && \
    apk del build-essential

FROM alpine
LABEL author="wvu"

WORKDIR /simh

COPY --from=simh /simh/vax780 .

RUN apk --no-cache add libcap

COPY . .

RUN gunzip *.gz && \
    chown -R nobody:nobody . && \
    setcap cap_net_bind_service+ep vax780 && \
    apk del libcap

EXPOSE 25 79

USER nobody
CMD ["./vax780", "boot.ini"]
