#!/usr/bin/env python3

import sys

import requests

IPAM_USER = 'admin'
IPAM_PASS = 'admin'
SUBNET_ID = '141'

def main() -> int:

    # print(f'subnet id: {SUBNET_ID}')

    # authenticate
    requests.packages.urllib3.disable_warnings()
    response = requests.post(
        f"https://ipam.sq/api/oamutils/user/",
        auth=(IPAM_USER, IPAM_PASS),
        verify=False
    )

    if response.status_code != 200:
        raise Exception(f'Cannot authenticate\n{response.json()}')

    auth_token = response.json()['data']['token']

    # print(f'auth token: {auth_token}')

    # get ips
    response = requests.get(
        f"https://ipam.sq/api/oamutils/subnets/{SUBNET_ID}/addresses/",
        headers={'phpipam-token': auth_token},
        verify=False
    )

    if response.status_code != 200:
        raise Exception(f'Cannot get IPs\n{response.json()}')

    ips = response.json()['data']
    # print(ips)

    # update ips
    for ip in ips:
        if ip['is_gateway'] == '1':
            continue

        # print(f'ip: {ip}')
        print(f'ip id: {ip["id"]}')
        print(f'ip address: {ip["ip"]}')
        print(f'ip hostname: {ip["hostname"]}')

        response = requests.patch(
            f'https://ipam.sq/api/oamutils/addresses/{ip["id"]}/',
            headers={'phpipam-token': auth_token},
            data={
                'custom_nas_user': {ip['hostname']}
            },
            verify=False
        )

    if response.status_code != 200:
        raise Exception(f'Cannot update IP {ip["ip"]}\n{response.json()}')

    return 0


if __name__ == '__main__':

    sys.exit(main())
