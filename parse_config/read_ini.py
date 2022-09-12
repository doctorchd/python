#!/usr/bin/env python3

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
config.read(TEST_FILE)
print(type(config))
print(type(config.sections()))
for section in config.sections():
    print("section =", section)
    print(type(config[section]))
    print(config[section])
    for key in config[section]:
        print(key, "==>", config[section][key])
