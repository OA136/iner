#!/bin/bash
echo $(netstat -nat|awk '$4 ~ /'"$1"'.*/'|awk '$6=="ESTABLISHED" || $6=="SYN_RECV"'| wc -l)
