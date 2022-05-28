import sys
import re
import yaml
from pwn import *

'''
This module aims to cread process or remote connection

'''

def BuildProcess(conf_file,mode = sys.argv[1]):
    with open(conf_file,'r') as file:
        conf = yaml.safe_load(file)
    # phase configure file
    if (mode == 'r'):
        return remote(conf['ip'],conf['port'])
    # remote connection
    elif (mode == 'a'):
        p = process(conf['elf'])
        gdb.attach(p)
    # gdb attach
        return p
    elif (mode == 'd'):
        return gdb.debug(conf['elf'],conf['gibscript'])
    # gdb to debug
    elif (mode == 'p'):
        return process(conf['elf'])
    # local process