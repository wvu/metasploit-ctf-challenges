#!/bin/sh -e

# HACK: Anime character to butterfly, "Is this ASLR?"
exec qemu-riscv64 -E FAKE_ASLR="$(printf "A%.s" $(seq "$RANDOM"))" /qemu/arnold
