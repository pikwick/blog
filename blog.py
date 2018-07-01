import random
import requests
import api
from uuid import uuid4

MAC_ETH1 = 'fa:16:3f:15:20:10'
MAC_ETH2 = 'fa:16:3f:15:20:20'
MOID_ETH2 = 'dvportgroup-14065'
IP_ETH2 = '10.10.58.1'
MAC_ETH3 = 'fa:16:3f:15:20:30'
MOID_ETH3 = 'dvportgroup-14066'
IP_ETH3 = '10.11.58.1'
MAC_ETH3_1 = 'fa:16:3f:15:20:31'
MOID_ETH3_1 = 'dvportgroup-5705'
IP_ETH3_1 = '10.11.58.2'
VM1_MAC = 'fa:16:3e:f5:13:f6'
VM2_MAC = 'fa:16:3e:02:33:e6'

edge_name = 'router10'
edge_id = str(uuid4())


ENABLE_PING_RULES = [
    {
        'source_port_range_min': None,
        'source_port_range_max': None,
        'source_ip_address': None,
        'destination_port_range_min': None,
        'destination_port_range_max': None,
        'destination_ip_address': None,
        'ip_version': 4,
        'enabled': True,
        'action': 'allow',
        'direction': 'ingress',
        'protocol': 'any',
        'name': 'ingress_rule'},
    {
        'source_port_range_min': None,
        'source_port_range_max': None,
        'source_ip_address': None,
        'destination_port_range_min': None,
        'destination_port_range_max': None,
        'destination_ip_address': None,
        'ip_version': 4,
        'enabled': True,
        'action': 'allow',
        'direction': 'egress',
        'protocol': 'any',
        'name': 'egress_rule'
    }
]

def genmac(prefix=None):
    octets = []
    if prefix:
        octets = prefix.split(':')
    octets += ['%02x' % random.randint(0x00, 0xff) for i in range(0, 6 - len(octets))]
    return ':'.join(octets)

headers = {'Content-type': 'application/json'}

# data = {
#         'id': edge_id,
#         'name': 'router1',
#         'connlimit': 65535,
#         'bandwidth': 50,
#         'external': {
#             'mac_address': MAC_ETH1,
#             'ipv4': {
#                 'gateway': '2.122.30.193',
#                 'ip_address': '2.122.30.223/24'
#             },
#             'ipv6': {
#                 'gateway': '2002:1:1::1',
#                 'ip_address': '2002:1:1::2/64'
#             }
#         },
#         'floating_ips': [
#             {"floating_ip": "195.122.30.232/24", "fixed_ip": "10.11.58.17/24"}
#         ],
#         'interfaces': [{
#             "mac_address": MAC_ETH2,
#             "port_group": MOID_ETH2,
#             "fixed_ips": ['{}/24'.format(IP_ETH2)],
#             "is_trunk": True,
#             "dhcp": {
#                 "gateway": "10.10.58.1",
#                 "dns_nameservers": ["8.8.8.8", "8.8.4.4"],
#                 "host_routes": [
#                     {"nexthop": "4.4.4.4", "destination": "8.4.8.4"}
#                 ]
#             },
#             "hosts": [{
#                 "device_id": "instance-41",
#                 "mac_address": genmac('02:42:ac'),
#                 "fixed_ips":["10.10.58.42", "2002:1:1:17::1"],
#                 "fw_rules": [{
#                     "start_port": None,
#                     "end_port": None,
#                     "remote_ip_address": None,
#                     "ip_version": 4,
#                     "enabled": True,
#                     "action": "allow",
#                     "direction": "ingress",
#                     "protocol": "icmp",
#                     "description": "",
#                     "connlimit": 65535,
#                     "name": "Allow ICMP ingress"
#                 }, {
#                     "start_port": None,
#                     "end_port": None,
#
#                     "remote_ip_address": None,
#                     "ip_version": 4,
#                     "enabled": True,
#                     "action": "allow",
#                     "direction": "egress",
#                     "protocol": "icmp",
#                     "description": "",
#                     "connlimit": 65535,
#                     "name": "Allow ICMP egress"
#                 }]
#             }]
#         }, {
#             "mac_address": MAC_ETH3,
#             "port_group": MOID_ETH3,
#             "fixed_ips": ['{}/24'.format(IP_ETH3)],
#             "is_trunk": True,
#             "dhcp": {
#                 "gateway": "10.5.0.1",
#                 "dns_nameservers": ["8.8.8.8", "8.8.4.4"],
#                 "host_routes": [{"nexthop": "4.4.4.4", "destination": "8.4.8.4"}]
#             },
#             "hosts": [{
#                 "device_id": "instance-42",
#                 "mac_address": VM1_MAC,
#                 "fixed_ips":["10.11.58.17", "2002:1:1:17::2"],
#                 "fw_rules": []
#             }]
#         }],
#         'port_forwarding': [{
#             "protocol": "tcp",
#             "internal_port": 8080,
#             "external_port": 80,
#             "local_ip": "10.10.58.42"
#         }, {
#             "protocol": "tcp",
#             "external_ports_range": {"start": 9090, "end": 10000},
#             "local_ip": "10.10.58.42"
#         }],
#         'fw_rules':[{
#             "source_port_range_min": None,
#             "source_port_range_max": None,
#             "source_ip_address": None,
#             "destination_port_range_min": None,
#             "destination_port_range_max": None,
#             "destination_ip_address": None,
#             "ip_version": 4,
#             "enabled": True,
#             "action": "allow",
#             "direction": "ingress",
#             "protocol": "icmp",
#             "description": "",
#             "connlimit": 65535,
#             "name": "Allow ICMP ingress"
#         }, {
#             "source_port_range_min": None,
#             "source_port_range_max": None,
#             "source_ip_address": None,
#             "destination_port_range_min": None,
#             "destination_port_range_max": None,
#             "destination_ip_address": None,
#             "ip_version": 4,
#             "enabled": True,
#             "action": "allow",
#             "direction": "egress",
#             "protocol": "icmp",
#             "description": "",
#             "connlimit": 65535,
#             "name": "Allow ICMP ingress"
#         }],
#         'routes': [],
#         'tenant': {
#             "pool": "group-v14707",
#             "folder": "group-v14703"
#         }
#     }


#Create edge

data = {"name": edge_name,
        "connlimit": 65535,
        "interfaces": [{
            "mac_address": MAC_ETH2,
            "port_group": MOID_ETH2,
            "fixed_ips": ['{}/24'.format(IP_ETH2)],
            "is_trunk": True,
            "dhcp": {
                "gateway": "10.10.58.1",
                "dns_nameservers": ["8.8.8.8", "8.8.4.4"],
                "host_routes": [
                    {"nexthop": "4.4.4.4", "destination": "8.4.8.4/32"}
                ]
            },
            "hosts": []
        },
        {
            "mac_address": MAC_ETH3,
            "port_group": MOID_ETH3,
            "fixed_ips": ['{}/24'.format(IP_ETH3)],
            "is_trunk": True,
            "dhcp": {
                "gateway": "10.11.58.1",
                "dns_nameservers": ["8.8.8.8", "8.8.4.4"],
                "host_routes": [
                    {"nexthop": "4.4.4.4", "destination": "8.4.8.4/32"}
                ]
            },
            "hosts": []
        }],
        "floating_ips": [],
        "bandwidth": None,
        "external": None,
        "routes": [],
        "port_forwarding": [],
        "id": edge_id,
        "tenant": {"folder": "group-v14703",
                   "pool": "resgroup-14707"},
        "fw_rules": ENABLE_PING_RULES}


#Hosts

# data =  {u'hosts': [{u'device_id': u'instance-247144',
#              u'fixed_ips': [u'10.10.10.3'],
#              u'fw_rules': [],
#              u'mac_address': u'fa:16:3e:fb:49:d0',
#              u'vm_hostname': u'itest-1'}]}

#Sharings

# data = {
#     'sharings':
#              [{ 'share_id': 100,
#                u'login': u'test9',
#                u'name': u'test9',
#                u'password': u'test9',
#                u'total_size': 1,
#                u'type': u'nfs'},
#               # { 'share_id': 101,
#               #  u'login': u'test5',
#               #  u'name': u'test5',
#               #  u'password': u'test5',
#               #  u'total_size': 1,
#               #  u'type': u'nfs'},
#               # { 'share_id': 102,
#               #  u'login': u'test5',
#               #  u'name': u'test5',
#               #  u'password': u'test5',
#               #  u'total_size': 1,
#               #  u'type': u'nfs'},
#               # {'share_id': 103,
#               #  u'login': u'test5',
#               #  u'name': u'test5',
#               #  u'password': u'test5',
#               #  u'total_size': 10,
#               #  u'type': u'nfs'}]
# }
#



