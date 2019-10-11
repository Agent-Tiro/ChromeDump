import re
import os

s = re.compile(b'\x70\x00\x72\x00\x6f\x00\x74\x00\x65\x00\x63\x00\x74\x00\x65\x00\x64\x00\x5f\x00\x73\x00\x74\x00\x6f\x00\x72\x00\x61\x00\x67\x00\x65(.*?)\S*', re.MULTILINE|re.DOTALL)
dirs = []

with os.scandir('chromedump/') as entries:
    for entry in entries:
        dirs.append(entry)

for f in dirs:
    with open(f, 'rb') as dump:
        r = dump.read()
        if s.search(r) != None:
            print(s.search(r).group())


    


