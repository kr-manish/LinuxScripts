#!/usr/bin/env python

import os
import sys

import logging
import argparse
import base64

# To Encode/Decode Base64
def base64_encode_decode(action, data):
    if action == 'decode':
        decoded = base64.b64decode(data)
        logging.info("decoded result: {}".format(decoded))
    else:
        encoded = base64.b64encode(data)
        logging.info("encoded result: {}".format(encoded))

# Caeser Cypher
def caeser_cypher(key, action, data):

    if action == 'decode':
        key = -key

    for chr in data:
        num = ord(chr)
        num += key
# To parse the arguments passed
def argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("method", choices=['base64', 'caeser', 'vigenere', 'DES', 'RSA'], help="which type of encryption/decryption to be used.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--encode", help="For encoding a string")
    group.add_argument("--decode", help="For decoding")
    parser.add_argument("-k", "--key", type=int, help="Key to encrypt or decrypt")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()
    return args


def main():

    # Get all the arguments
    args = argument_parser()

    # Check the verbosity level
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG, format='%(funcName)s:%(levelname)s:%(message)s')
    else:
        logging.basicConfig(level=logging.INFO, format='%(funcName)s:%(levelname)s:%(message)s')

    method = args.method
    action = 'encode' if args.encode else 'decode'
    data = args.encode if action=='encode' else args.decode

    logging.debug("{} this {} string using {}".format(action, data, method))

    if method == 'base64':
        base64_encode_decode(action, data)

    if method == 'caeser':
        caeser_cypher(args.key, action, data)

if __name__ == "__main__":
    main()

