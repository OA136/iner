#!/bin/bash
acckers=("192.168.1.10");
user='root'
server='192.168.0.10'
for accker in ${acckers[@]};do
	ssh $user@$accker "sh /home/main/get/service-start.sh http://$server/ $1 $2" >./log/remote.log 2>&1 &
done
#python save.py $1 >./log/save.log 2>&1 &
#	python save.py
#python getwidth.py $1 >getwidth.log 2>&1 &
python tcp_mem.py $1 >./log/tcp_mem.log 2>&1 &
python width.py $1 >./log/width.log 2>&1 &
python drop.py $1 >./log/drop.log 2>&1 &
python cpu.py $1 >./log/cpu.log 2>&1 &

