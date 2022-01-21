# King of Spades

Run `./build.sh` to build and run just this challenge.

## Objective

[TempleOS] ([Shrine]) is running in QEMU with Shrine's [Mfa] program
exposed on TCP port 7770 using glorious `socat(1)` duct tape.

Players must figure out how to interact with the service, obtain the
flag, and exfiltrate it.

## Solution

Run `./solve.py` with [pwntools] installed.

[TempleOS]: https://en.wikipedia.org/wiki/TempleOS
[Shrine]:   https://github.com/minexew/Shrine
[Mfa]:      https://github.com/minexew/Shrine/blob/master/Mfa/Mfa.HC
[pwntools]: https://github.com/Gallopsled/pwntools
