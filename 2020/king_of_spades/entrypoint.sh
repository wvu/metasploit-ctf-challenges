#!/bin/sh -ex

qemu-system-x86_64 \
  -m 512 -hda /qemu/shrine.qcow2 \
  -device pcnet,netdev=u1 -netdev user,id=u1 \
  -chroot /qemu -runas 65534:65534 \
  -vnc :0 -monitor none \
  -serial unix:/qemu/qemu.sock,server,nowait \
  -daemonize

# XXX: "nobody" needs access to this socket
chown -v root:nobody /qemu/qemu.sock
chmod -v 660 /qemu/qemu.sock

# XXX: Duct tape!
socat -d -d \
  tcp-listen:7770,fork,reuseaddr \
  exec:/qemu/mfa_proxy.sh,stderr,su=nobody
