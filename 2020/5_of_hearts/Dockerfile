FROM alpine
LABEL author="wvu"

WORKDIR /qemu

RUN apk --no-cache add \
      busybox-extras \
      qemu-riscv64

COPY . .

RUN chmod 701 . && \
    chmod 604 5_of_hearts.png && \
    chmod 704 arnold && \
    chmod 705 arnold.sh && \
    chmod 600 inetd.conf && \
    mv 5_of_hearts.png /tmp/🂵

EXPOSE 23

CMD ["/usr/sbin/inetd", "-fe", "inetd.conf"]
