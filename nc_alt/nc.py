#!/usr/bin/python2.7

import os
import sys

import argparse
import logging

def argument_parser():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true")
    group.add_argument("-q", "--quite", action="store_true")
    parser.add_argument("-l", "--listen", action="store_true", help="Listen to the incoming connection")
    parser.add_argument("-p", "--port", required=True, type=int, help="Port to listen to")
    args = parser.parse_args()
    return args

def main():
    # Get all arguments first
    args = argument_parser()


if __name__ == '__main__':
    main()
