#!/usr/bin/env python

import requests
import wget
import os

from bs4 import BeautifulSoup, SoupStrainer

url = "https://attack.mitre.org/#"
root_url = "https://attack.mitre.org"

#file_types = ['.pdf']
file_types = ["TA00"]

for file_type in file_types:
    response = requests.get(url)

    for link in BeautifulSoup(response.content, 'html.parser', parse_only=SoupStrainer('a')):
        if link.has_attr('href'):
            if file_type in link['href']:
                full_path = root_url + link['href']
                print(full_path,link.get_text())
