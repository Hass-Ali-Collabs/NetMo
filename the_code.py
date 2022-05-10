
#we need to install pcapng

from pcapng import FileScanner

with open(r'example.pcapng', 'rb') as fp:
    scanner = FileScanner(fp)
    for block in scanner:
        print(block)
        print(block._raw) #byte type raw data

#problem in code 