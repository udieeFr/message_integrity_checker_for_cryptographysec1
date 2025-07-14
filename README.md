# RSA Digital Signature System

A Python implementation of RSA digital signatures for message authentication and integrity verification.

## Features

- Generates 2048-bit RSA key pairs
- Signs messages using SHA-256 hashing and PKCS#1 v1.5 padding
- Verifies message authenticity and integrity
- Stores signed messages with their signatures
- Interactive command-line interface

## Prerequisites

- Python 3.x
- PyCryptodome library

## Installation

1. Install the required library:
```bash
pip install pycryptodome
