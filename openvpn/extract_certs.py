#!/usr/bin/env python3

import sys
import re

# ---------------------------
# definitions
# ---------------------------
ca_file     = 'ca.crt'
cert_file   = 'cert.crt'
key_file    = 'key.pem'

comment_ptrn    = re.compile("^ *#")
ca_start_ptrn   = re.compile("^<ca>")
cert_start_ptrn = re.compile("^<cert>")
key_start_ptrn  = re.compile("^<key>")
ca_stop_ptrn    = re.compile("^</ca>")
cert_stop_ptrn  = re.compile("^</cert>")
key_stop_ptrn   = re.compile("^</key>")

# ---------------------------
# action
# ---------------------------

# check if config file is specified
if len(sys.argv) != 2:
    print("Error: must be exactly one argument")
    exit(255)

config_file = sys.argv[1]

# open config file
with open(config_file, mode='r') as f:
    config = f.readlines()
    f.close()

# extract components
component = None

ca      = []
cert    = []
key     = []

for line in config:
    if not comment_ptrn.match(line):
        if ca_start_ptrn.match(line):
            component = 'ca'
            continue
        elif cert_start_ptrn.match(line):
            component = 'cert'
            continue
        elif key_start_ptrn.match(line):
            component = 'key'
            continue
        elif ca_stop_ptrn.match(line):
            component = None
        elif cert_stop_ptrn.match(line):
            component = None
        elif key_stop_ptrn.match(line):
            component = None

    if component == 'ca':
        ca.append(line)
    elif component == 'cert':
        cert.append(line)
    elif component == 'key':
        key.append(line)

# write components to files
with open(ca_file, 'w') as f:
    for line in ca:
        f.write(line)
    f.close()
    
with open(cert_file, 'w') as f:
    for line in cert:
        f.write(line)
    f.close()
    
with open(key_file, 'w') as f:
    for line in key:
        f.write(line)
    f.close()

