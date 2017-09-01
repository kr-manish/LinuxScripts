#!/usr/bin/env python

import os
import sys

import argparse
import base64

def base64_encode_decode(data, action):
        if action == 'decode':
                decoded = base64.b64decode(data)
                print decoded

def main():
        parser = argparse.ArgumentParser()
        parser.add_argument("method", choices=['base64', 'caeser', 'vigenere', 'DES', 'RSA'], help="which type of encryption/decryption to be used.")
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument("--encode", help="For encoding a string")
        group.add_argument("--decode", help="For decoding")
        args = parser.parse_args()

        if args.method == 'base64':
                action = 'encode' if args.encode else 'decode'
                data = args.encode if action=='encode' else args.decode
                base64_encode_decode(data, action)

if __name__ == "__main__":
        main()

