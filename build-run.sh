#!/usr/bin/env bash

first_time=1
while true; do
    clear
    make crypto
    if [[ first_time -eq 1 ]]; then
        first_time=0
        open http://localhost:5000
    fi
    docker run --name crypto -it --rm -e DEBUG=1 -p 5000:5000 ivonet/crypto
done
