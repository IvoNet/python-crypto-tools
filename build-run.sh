#!/usr/bin/env bash

idx=1
while true; do
    clear
    make crypto
    if [[ idx -eq 1 ]]; then
        idx=0
        open http://localhost:5000
    fi
    docker run --name crypto -it --rm -e DEBUG=1 -p 5000:5000 ivonet/crypto
done
