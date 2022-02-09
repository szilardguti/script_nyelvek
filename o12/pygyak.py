#!/usr/bin/env python3
import urllib.request

def get_page(url: str) -> str:
    return urllib.request.urlopen(url).read().decode('utf-8')
