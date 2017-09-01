#!/usr/bin/env python

import os
import sys

import argparse

def base64_encode_decode(value, action):


def main():
        parser = argparse.ArgumentParser()
        parser.add_argument("type", choices=['base64', 'caeser', 'vigenere', 'DES', 'RSA'], help="which type of encryption/decryption to be used.")
        group = parser.add_mutually_exclusive_group()
        group.add_argument("--encode", help="For encoding a string")
        group.add_argument("--decode", help="For decoding")
        parser.add_argument("data", help="Data to encrypt/decrypt")
        args = parser.parse_args()

        if args.type == 'base64':
                print "base64"

if __name__ == "__main__":
        main()

