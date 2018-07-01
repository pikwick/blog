import json
import os

STATE_PATH = '/home/ivand/Projects/toochka-net/edge/edge/test/unit/states'

for json_file in os.listdir(STATE_PATH):
    file_path = os.path.join(STATE_PATH, json_file)
    if os.path.isfile(file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)
            for interface in range(len(data['router']['interfaces'])):
                for host in range(len(data['router']['interfaces'][interface]['hosts'])):
                    print(file_path, data['router']['interfaces'][interface]['hosts'][host]['device_id'])
                    data['router']['interfaces'][interface]['hosts'][host][u'vm_hostname'] = data['router']['interfaces'][interface]['hosts'][host][u'device_id']
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)







