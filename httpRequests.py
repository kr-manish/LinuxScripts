#!//usr/bin/env python

import os
import sys

import requests
import argparse

def http_post(url, payload=None, verbosity = False):
        if verbosity:
                print "making a POST request!!!"
        r = requests.post(url, data=payload)
        print r.text

def main():

        parser = argparse.ArgumentParser()
        group = parser.add_mutually_exclusive_group()
        group.add_argument("-v", "--verbose", action="store_true")
        group.add_argument("-q", "--quite", action="store_true")
        parser.add_argument("method", choices=['post', 'get', 'put', 'delete'], help="Which HTTP method to be used?")
        parser.add_argument("--url", required=True, help="URL to make a request")
        parser.add_argument("--payload", help="Payload to be sent to the url.")
        args = parser.parse_args()

        if args.method == 'post':
                verbosity = True if args.verbose else False
                if args.payload:
                        http_post(args.url, args.payload, verbosity)
                else:
                        http_post(args.url, verbosity)

if __name__ == '__main__':
        main()
