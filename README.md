# IvoNet Python Crypto tools

This repository is mainly used to help solve AIVD Christmas puzzles.

But it also demonstrates many of the old cryptographic formulae.


# Prerequisites

* Docker
* Python 3.8+


# Build

`make` is used to build the docker images. 
To make the crypto image you first need to build the base image with all the dependencies.

to get help on how to use the build system just type `make` without any parameters

## Crypto base image

```bash
make crypto-base
```

## Crypto main image

```bash
make crypto
```

# Release

Follow the instructions given by `make`.

# Run

```bash
docker run -d --rm -p 5000:5000 ivonet/crypto
```
