#!/bin/bash
#acckers=("10.0.3.21" "10.0.3.34");
acckers=("192.168.1.10" "192.168.1.11" "192.168.1.12" "192.168.1.13");

user='root'

#------------remove get from acckers------------#
for accker in ${acckers[@]};do
	ssh $user@$accker "rm -r /home/main/get"
done
