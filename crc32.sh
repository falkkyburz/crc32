#!/bin/bash
gcc -c crc32.c
gcc -shared -o crc32.dll crc32.o
[ -f crc32.o ] && rm crc32.o
