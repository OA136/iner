#!/bin/bash
ssh root@192.168.1.10 "python /home/main/get/insert.py"
python insert_every_table.py $1 $2 $3 $4 $5 $6
#python insert.py $1 $2 $3 $4 $5 $6
#insert service to inf and delete where service is mull
ssh root@192.168.1.10 "python /home/main/get/update_inf_service.py"

#copy inf into result
#python dealwith_inf.py

#update inf attack num after attack and before attack
python dealwith_inf.py $1 $2

#compute avg data of inf
python avg_inf.py $3 $4 $5 $6
