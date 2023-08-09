#!/bin/env python3

import subprocess
import re

NAME = "gsg0.sq.mil.gov.ua"

nases = {
  "t107_7": "176.102.34.150",
  "t115_0": "20.95.80.5",
  "t115_1": "80.91.188.227"
}

dns_servers = {
  "cloudflare": ["1.1.1.1", "1.0.0.1"],
  "google": ["8.8.4.4", "8.8.8.8"],
  "quad": ["9.9.9.9", "149.112.112.112"],
  "open_dns": ["208.67.222.222", "208.67.220.2"],
  "control_d": ["76.76.2.0", "76.76.10.0"],
  "clean_browsing": ["185.228.168.9", "185.228.169.9"],
  "alternate_dns": ["76.76.19.19", "76.223.122.150"],
  "adguard_dns": ["94.140.14.14", "94.140.15.15"]
}

for provider in dns_servers.keys():
  for server in dns_servers[provider]:
    print(f"--- {server} ({provider}) ---")

    matches = {}
    for nas in nases.keys():
      matches[nas] = 0

    for i in range(0, 100):
      # print('.', end='')
      res = subprocess.run(['host', NAME, server], stdout=subprocess.PIPE, check=True)
      lines = res.stdout.decode('ascii').split('\n')
      # print(lines)
      for line in lines:
        if re.match(r'.* has address .*', line):
          # print(line)
          for nas in nases.keys():
            regexp = '.* ' + nases[nas]
            # print(regexp)
            if re.match(regexp, line):
              # print(line)
              # print('match')
              # else:
              #   print('no match')
              matches[nas] += 1
              # print(nas)
          break
    for nas in matches.keys():
      print(f'{nas}: {matches[nas]}')
