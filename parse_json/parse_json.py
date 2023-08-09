#!/usr/bin/env python3

import sys
import json
import argparse


def main() -> int:

  parser = argparse.ArgumentParser()
  parser.add_argument('filename')
  args = vars(parser.parse_args())

  # print(f'args["filename"]: {args["filename"]}')

  with open(args['filename'], 'r') as data_file:
    # data = json.load(json_file)
    # print(f'data: {data}')
    # print(f'type of data: {type(data_file)}')
    # data = data_file.read()
    # print(f'type of data: {type(data)}')
    while True:
      data_string = data_file.readline()
      print(f'data_string: {data_string}')
      print(f'type of data_string: {type(data_string)}')

      json_data = json.loads(data_string)
      print(f'\ntype of json_data: {type(json_data)}')
      print(f'json_data: {json_data}')
      print(f'json_data.keys(): {json_data.keys()}')
      input('continue?')
      # if data_string is None:
      #   break
      # print(f'type of data_string: {type(data_string)}')
      # print(data_string)


  return 0


if __name__ == "__main__":
  sys.exit(main())
