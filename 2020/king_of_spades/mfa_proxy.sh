#!/bin/sh -e

cat <<EOF
minimalist file access proxy

Authorized operations:
  - File download
  - File upload

Don't Nmap me, bro.

EOF

while read -r; do
  case "$REPLY" in
    L*)
      echo "Downloading file..." >&2
      echo "$REPLY"
      ;;
    P*)
      echo "Uploading file..." >&2
      echo "$REPLY"
      ;;
    *)
      echo "$REPLY"
  esac
done | exec \
  socat -lf /dev/null - unix-connect:/qemu/qemu.sock,forever
