#!/bin/bash
echo 'Starting installation of Devstack with OSM config'
cd devstack
echo '[[local|localrc]]' > local.conf
echo 'ADMIN_PASSWORD=admin' >> local.conf
echo 'DATABASE_PASSWORD=$ADMIN_PASSWORD' >> local.conf
echo 'RABBIT_PASSWORD=$ADMIN_PASSWORD' >> local.conf
echo 'SERVICE_PASSWORD=$ADMIN_PASSWORD' >> local.conf

echo 'LOGFILE=$DEST/logs/stack.sh.log' >> local.conf
echo 'FLOATING_RANGE=172.16.0.1/16' >> local.conf

# Install devstack
./stack.sh

# Auth admin project
source accrc/admin/admin

# Create OSM subnets
neutron net-create mgmt --provider:network_type=vlan --provider:physical_network=public --provider:segmentation_id=500 --shared
neutron subnet-create --name subnet-mgmt mgmt 10.208.0.0/24 --allocation-pool start=10.208.0.2,end=10.208.0.254 --dns 8.8.8.8 

neutron net-create data --shared
neutron subnet-create --name subnet-mgmt data 192.168.134.0/24 --allocation-pool start=192.168.134.2,end=192.168.134.254
 
# Create mgmt router
openstack router create mgmt_rt 
openstack router set --external-gateway public
# openstack router add subnet mgmt_rt public-subnet
openstack router add subnet mgmt_rt subnet-mgmt

# Remove Quotas
openstack quota set admin --floating-ips -1
openstack quota set admin --volumes -1
openstack quota set admin --instances -1