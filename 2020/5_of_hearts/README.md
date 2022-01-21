# 5 of Hearts

Run `./build.sh` to build and run just this challenge.

## Objective

Exploit a [RISC-V] stack-based buffer overflow on TCP port 23 and
retrieve the flag from the filesystem.

Savvy players can use the `md5sum(1)` command on the target to get the
hash of the flag without exfiltrating it.

## Solution

Install [pwntools]. Run `./brute.py` to get the ELF. Run `./solve.py` to
solve the challenge.

[RISC-V]:   https://en.wikipedia.org/wiki/RISC-V
[pwntools]: https://github.com/Gallopsled/pwntools
