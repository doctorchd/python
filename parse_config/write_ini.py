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
config['DEFAULT'] = {
    "delay": 10,
    "jitter": 5,
    "loss": 1,
    "bandwidth": 1000
}
config['group1'] = {}
config['group1']['param1'] = 'value1'
config['group1']['param2'] = 'value2'

config['group2'] = {}
group2 = config['group2']
group2['param3'] = 'value3'
group2['param4'] = 'value4'

with open(TEST_FILE, 'w') as configfile:
    config.write(configfile)


