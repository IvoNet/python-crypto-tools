#!/usr/bin/env bash

while true; do
    clear
    make crypto
    docker run -it --rm -p 5000:5000 ivonet/crypto
    sleep 1
done
