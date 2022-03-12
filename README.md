# IvoNet Python Crypto tools

This repository is mainly used to help solve AIVD Christmas puzzles.

But it also demonstrates many of the old cryptographic formulae.


# Prerequisites

* Docker
* Python 3.8+

# Create Python virtual environment

from the project root:

```shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Make sure to always activate the virtual env with 
`source venv/bin/activate` before using the command line in the project


# Build

`make` is used to build the docker images. 
To make the crypto image you first need to build the base image with all the dependencies.

to get help on how to use the build system just type `make` without any parameters

## Crypto base image

This image only needs to be build if it is not yet there or if you added a new requirement (dependency)

```bash
make crypto-base
```

## Crypto main image

Contains the crypto tools

```bash
make crypto
```

# Release

Follow the instructions given by `make`.

# Run

```bash
docker run -d --rm -p 5000:5000 ivonet/crypto
```

or run:

```bash
build-run.sh
```
every time you want to rebuild just press ctrl-c once and twice to quit

## Without docker

Be sure to install the `crypto-base/requirements.txt` in your environment and all should work fine.

```bash
pip3 install -r ./crypto-base/requirements.txt
```


# Swagger

You can see all the endpoints by running the application and going to 
the [swagger](http://localhost:5000) page.
