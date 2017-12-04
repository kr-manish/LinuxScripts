#!/usr/bin/env python

import requests
import wget
import os

from bs4 import BeautifulSoup, SoupStrainer

url = "https://www.fireeye.com/blog/threat-research/2017/10/2017-flare-on-challenge-solutions.html"
root_url = "https://www.fireeye.com"

file_types = ['.pdf']

for file_type in file_types:

    response = requests.get(url)

    for link in BeautifulSoup(response.content, 'html.parser', parse_only=SoupStrainer('a')):
        if link.has_attr('href'):
            if file_type in link['href']:
                full_path = root_url + link['href']
                print full_path
                wget.download(full_path)
