#This script can be used from any user
'''
Use this script as follows on 'openstack' machine: 
cd
wget -O release_ips.py https://raw.githubusercontent.com/CN-UPB/tng-sdk-benchmark/dev/release_ips.py #temporary
printf "source /opt/stack/devstack/accrc/admin/admin\npython release_ips.py \n rm floating_ip_list.yaml \n" > release_ips.sh
chmod +x release_ips.sh
(crontab -l && echo "* * * * * /bin/bash ~/release_ips.sh") | crontab - #adding a cronjob
./release_ips.sh #manual run
'''
import os
import yaml
os.system("/usr/local/bin/openstack floating ip list -f yaml > floating_ip_list.yaml")
with open("floating_ip_list.yaml") as f:
    yaml_data = yaml.safe_load(f)
    for ele in yaml_data:
        if ele.get("Fixed IP Address")==None:
            os.system("/usr/local/bin/openstack floating ip delete {}".format(ele.get("Floating IP Address")))
