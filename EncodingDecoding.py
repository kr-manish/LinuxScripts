#!/usr/bin/env python

import os
import sys

import argparse

def main():
        parser = argparse.ArgumentParser()
        parser.add_argument("type", help="which type of encryption/decryption to be used.")
        group = parser.add_mutually_exclusive_group()
        group.add_argument("--encode", help="For encoding a string")
        group.add_argument("--decode", help="For decoding")
        args = parser.parse_args()

        if args.type == 'base64':
                print "base64"

if __name__ == "__main__":
        main()

