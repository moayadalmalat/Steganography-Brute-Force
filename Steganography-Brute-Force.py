#!/usr/bin/python
from multiprocessing import pool
from pyfiglet import Figlet
import argparse
from sys import argv
from time import time
def banner():
    

    print(Figlet(font='graffiti').renderText('Moayad'))
    
def parseArgs():
    
    

    parser = argparse.ArgumentParser(epilog='Example: {} -i image.jpg -o output.txt -w worlist.txt'.format(argv[0]))
    parser._optionals.title = 'OPTIONS'
    parser.add_argument('-i', '--image', help='select stego image', required=True)
    parser.add_argument('-o', '--output', help='select file name for extracted data', required=True)
    parser.add_argument('-w', '--wordlist', help='select a wordlist', required=True)
    return parser.parse_args().image, parser.parse_args().output, parser.parse_args().wordlist

def steghide(password):
    from subprocess import call, DEVNULL
    cmd = 'steghide extract -sf {0} -fx {1} -p {2}', format(image, output, password)
    if call(cmd.split(),stdout = DEVNULL,stderr = DEVNULL) == 0:
        print('[=] Password: {}\n[Ctrl + C] to stop'.format(password))

if __name__== '__main__':
    
    

    banner()
    image, output, wordlist = parseArgs()
    pool = pool()
    start = time()
    pool.map(steghide,[password.rstrip() for password in open(wordlist, errors = 'ignore')])
    totalTime = time() - start
    timeFormat = 'seconds'
    if(totalTime >= 60):
        totalTime = totalTime/60
        timeFormat = 'minutes'
        if(totalTime >= 3600):
            totalTime = totalTime/60
            timeFormat = 'hours'
    print('[=] Finished : {0:.f2} {1}'.format(totalTime,timeFormat))
