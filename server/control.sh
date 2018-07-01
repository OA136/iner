#!/bin/bash
#echo "USAGE: $0 thread_num data_size attack_num sleep_space"
thread=9
attack=4
data=20000000
frequent=0


while [ $thread -le 20 ]
do
	frequent=0			
#	while [ $frequent \< 0.1 ]
	while [ $(echo "$frequent < 0.1" | bc) = 1 ]
	do
		frequent=`echo "scale=3;$frequent + 0.01" | bc`
		#frequent=$(($frequent*10.0))
		echo $thread $data $attack $frequent
		./allrun.sh $thread $data $attack $frequent 
	done
	thread=$[ $thread + 1 ]
done

