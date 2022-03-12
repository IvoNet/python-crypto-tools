#!/usr/bin/env bash

first_time=1
docker rm -f crypto 2>/dev/null
while true; do
#    clear
    make crypto
    if [[ first_time -eq 1 ]]; then
        first_time=0
        open http://localhost:6000
    fi
    docker run --name crypto -it --rm -e DEBUG=1 -p 6000:5000 ivonet/crypto
done
