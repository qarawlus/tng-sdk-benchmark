#This script will run in openstack 'stack' user
'''
Use it directly or through a script as follows: 
cd
printf "python PATH_TO_RELEASE_IPS_PYTHON_FILE" > release_ips.sh
chmod +x release_ips.sh
./release_ips.sh
'''
import os
import yaml
os.system("source ~/devstack/accrc/admin/admin")
os.system("openstack floating ip list -f yaml > floating_ip_list.yaml")
with open("floating_ip_list.yaml") as f:
    yaml_data = yaml.safe_load(f)
    for ele in yaml_data:
        if ele.get("Fixed IP Address")==None:
            os.system("openstack floating ip delete {}".format(ele.get("Floating IP Address")))
