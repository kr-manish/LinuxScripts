#!//usr/bin/env python

import os
import sys

import requests
import argparse

def http_post(url, payload=None, verbosity=False):
    if verbosity:
        print "making a POST request!!!"
    r = requests.post(url, data=payload)
    print r.text

def http_get(url, verbosity=False, payload=None, api=None):
    if verbosity:
        print "making a GET request!"
    else:
        print "quite"


def argsParser():
    """ This function is to parse the arguments """
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true")
    group.add_argument("-q", "--quite", action="store_true")
    parser.add_argument("method", choices=['post', 'get', 'put', 'delete'], help="Which HTTP method to be used?")
    parser.add_argument("--url", required=True, help="URL to make a request")
    parser.add_argument("--payload", help="Payload to be sent to the url.")
    return parser.parse_args()

def main():
    """ Main Function """
    args = argsParser()
    verbosity = True if args.verbose else False
    method = args.method.lower()
    api_key = 'c0749e2654b34b0cd887df2b8b673bdc9f6c5b1af6906c41a29b386e0d8bd4ee'
    if args.method == 'post':
        if args.payload:
            http_post(args.url, verbosity, args.payload)
        else:
            http_post(args.url, verbosity)

    elif args.method == 'get':
        if args.payload:
            http_get(args.url, verbosity, arg.payload, api=api_key)
        else:
            http_get(args.url, verbosity)

if __name__ == '__main__':
    main()
