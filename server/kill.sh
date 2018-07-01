#!/bin/bash
#jobs -rl|grep start.sh | awk '{print $2}' | xargs kill -9
ps -aux |grep cpu.py |awk '{print $2}' | xargs kill -9
ps -aux |grep drop.py |awk '{print $2}' | xargs kill -9
ps -aux |grep tcp_mem.py |awk '{print $2}' | xargs kill -9
ps -aux |grep width.py |awk '{print $2}' | xargs kill -9
ps -aux |grep getwidth.py |awk '{print $2}' | xargs kill -9
ps -aux |grep save.py |awk '{print $2}' | xargs kill -9

acckers=("192.168.1.10");
user='root'
for accker in ${acckers[@]};do
	ssh $user@$accker "ps -aux |grep service-time.py |awk '{print \$2}'|xargs kill -9;ps -aux |grep test-connection.py |awk '{print \$2}'|xargs kill -9"
done
#ps -aux|grep save.py | awk '{print $2}' |xargs kill -9
