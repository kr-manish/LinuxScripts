#!//usr/bin/env python

import os
import sys

import requests
import argparse

def http_post(url, payload=None):
        print "in post"
        r = requests.post(url, data=payload)
        print r.text

def main():

        parser = argparse.ArgumentParser()
        group = parser.add_mutually_exclusive_group()
        group.add_argument("-v", "--verbose", action="store_true")
        group.add_argument("-q", "--quite", action="store_true")
        parser.add_argument("method", help="Which HTTP method to be used?")
        parser.add_argument("url", help="URL to make a request")
        parser.add_argument("--payload", help="Payload to be sent to the url.")
        args = parser.parse_args()

        if args.method == 'post':
                if args.url:
                        http_post(args.url)
                else:
                        print "Enter the URL!!"

if __name__ == '__main__':
        main()
