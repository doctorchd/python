#!/usr/bin/env python3

import sys

import requests

IPAM_URL = 'https://ipam.sq:8443/api/oamutils'
IPAM_USER = 'oamadmin'
IPAM_PASS = 'vaiquah7AihietheiYoo'
SUBNET_ID = '388'


def main() -> int:

    # authenticate
    requests.packages.urllib3.disable_warnings()
    response = requests.post(
        f"{IPAM_URL}/user/",
        auth=(IPAM_USER, IPAM_PASS),
        verify=False
    )

    if response.status_code != 200:
        raise Exception(f'Cannot authenticate\n{response.json()}')

    auth_token = response.json()['data']['token']

    # print(f'auth token: {auth_token}')

    # read users file
    all = False
    with open('users.csv', 'r') as users:
        for line in users:
            # print(line.strip())
            username = line.strip().split(',')[3]
            vpn_ip = line.strip().split(',')[6]
            description = "contact id: 12; remark: created in batch"
            print(f'username: {username}, vpn_ip: {vpn_ip}, description: "{description}"')

            response = requests.post(
                f"{IPAM_URL}/addresses/",
                headers={'phpipam-token': auth_token},
                data={
                    'ip': vpn_ip,
                    'subnetId': SUBNET_ID,
                    'hostname': username,
                    'description': description,
                    'custom_nas_user': username
                },
                verify=False
            )

            if response.status_code != 201:
                raise Exception(f'Cannot create IP {vpn_ip}: {response.json()}')

            if not all:
                input('Proceed?')

    return 0


if __name__ == '__main__':

    sys.exit(main())
