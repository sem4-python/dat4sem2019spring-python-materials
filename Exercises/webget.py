import os
import urllib.request as req
from urllib.parse import urlparse
import sys

def download(url, to=None):
    data = req.urlretrieve(url, to)
    print(data[1])
 

for x in range(1, len(sys.argv)):
    download(sys.argv[x])