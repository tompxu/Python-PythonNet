'''
Created on 2013-4-27

@author: miracle
'''
import urllib, sys
def DownloadFile(filepath):
    fsock = urllib.urlopen(filepath)
    while True:
        buf = fsock.read(1024)
        if not len(buf):
            break
        sys.stdout.write(buf)

if __name__ == '__main__':
    filepath = 'https://www.kernel.org/pub/dist/superrescue/v1/README'
    DownloadFile(filepath)