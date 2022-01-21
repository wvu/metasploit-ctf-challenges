FROM alpine
LABEL author="wvu"

WORKDIR /qemu

RUN apk --no-cache add \
      qemu-system-x86_64 \
      socat

COPY . .

EXPOSE 7770

RUN chmod 701 . && \
    chmod 700 entrypoint.sh && \
    chmod 705 mfa_proxy.sh && \
    chmod 600 shrine.qcow2

ENTRYPOINT ["./entrypoint.sh"]
