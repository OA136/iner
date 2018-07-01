#!/bin/bash
python init.py
if [ $# != 4 ];then
	echo "USAGE: $0 thread_num data_size attack_num sleep_space"
	exit 1;
fi
before_attack_start=10
attack_length=200
./start.sh 1 $before_attack_start
sleep $before_attack_start

before=`python getrecords_num.py`
before=$[ $before + 1 ]
echo $before

thread_num=$1
data_size=$2
attack_num=$3
sleep_space=$4
./start-attack.sh $thread_num $data_size $attack_num $sleep_space
sleep $attack_length

./kill-attack.sh
after=`python getrecords_num.py`
echo $after
sleep 10
./kill.sh
./insert.sh $before $after $thread_num $attack_num $data_size $sleep_space




