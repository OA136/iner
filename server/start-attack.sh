#!/bin/bash
acckers=("192.168.1.10" "192.168.1.11" "192.168.1.12" "192.168.1.13");
user='root'
server='192.168.0.10'
count=$3
for accker in ${acckers[@]};do
	count=$[count-1];
	ssh root@$accker "python /home/main/get/get.py http://$server:6699/ $1 $2 $3" >./log/$accker.log 2>&1 &
	if [ $count == 0 ]
	then
		break
	fi
done
#ssh -p 223 root@192.168.75.136 "python /home/sq/get/get.py http://192.168.75.134:6699/ $1" >136.log 2>&1 &
