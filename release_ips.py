#This script can be used from any user
'''
Use this script as follows: 
cd
printf "source /opt/stack/devstack/accrc/admin/admin\npython PATH_TO_RELEASE_IPS_PYTHON_FILE \n rm floating_ip_list.yaml \n" > release_ips.sh
chmod +x release_ips.sh
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
