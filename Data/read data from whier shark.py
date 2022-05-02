"""
we need to install this package in order to read
pcapng file

#pip install python-pcapng

"""

from pcapng import FileScanner

with open(r'C:UserszahangirDownloadsMDS19 Wireshark Log 08072021.pcapng', 'rb') as fp:
    scanner = FileScanner(fp)
    for block in scanner:
        print(block)
        print(block._raw) #byte type raw data
