#!/bin/bash
acckers=("192.168.1.10" "192.168.1.11" "192.168.1.12" "192.168.1.13");
user='root'
for accker in ${acckers[@]};do
	ssh $user@$accker "ps -aux | grep get.py | awk '{print \$2}' | xargs kill -9"
done
