#!/usr/bin/env python3

"""
https://docs.python.org/3/library/configparser.html
"""

import configparser

# -----------------------------------------------------------------------------
# definitions
# -----------------------------------------------------------------------------
TEST_FILE = "test.conf"

# -----------------------------------------------------------------------------
# functions
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# action
# -----------------------------------------------------------------------------
config = configparser.ConfigParser()
# config.read(TEST_FILE)
try:
    with open(TEST_FILE, 'r') as f:
        config.read_file(f)
except Exception as exc:
    print(exc)

print(type(config))
print(type(config.sections()))
for section in config.sections():
    print("section =", section)
    print(type(config[section]))
    print(config[section])
    for key in config[section]:
        print(key, "==>", config[section][key])
