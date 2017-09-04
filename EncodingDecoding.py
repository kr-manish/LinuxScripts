#!/usr/bin/env python

import os
import sys

import logging
import argparse
import base64

def base64_encode_decode(data, action):
        logging.debug("data {} to {}".format(data, action))
        if action == 'decode':
                decoded = base64.b64decode(data)
                logging.info("decoded result: {}",format(decoded))
        else:
                encoded = base64.b64encode(data)
                logging.info("encoded result: {}".format(encoded))

# To parse the arguments passed
def argument_parser():
        parser = argparse.ArgumentParser()
        parser.add_argument("method", choices=['base64', 'caeser', 'vigenere', 'DES', 'RSA'], help="which type of encryption/decryption to be used.")
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument("--encode", help="For encoding a string")
        group.add_argument("--decode", help="For decoding")
        parser.add_argument("-v", "--verbose", action="store_true")
        args = parser.parse_args()
        return args


def main():

        args = argument_parser()
        if args.verbose:
                logging.basicConfig(level=logging.DEBUG)
        else:
                logging.basicConfig(level=logging.INFO)

        if args.method == 'base64':
                action = 'encode' if args.encode else 'decode'
                data = args.encode if action=='encode' else args.decode
                base64_encode_decode(data, action)

if __name__ == "__main__":
        main()

