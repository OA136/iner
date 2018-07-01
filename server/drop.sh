#!/bin/bash
before=`netstat -i | awk '$1 ~ /'ens3'.*/'`
bef_RX_OK=`echo $before | awk '{print $8+$4}'`
bef_RX_DRP=`echo $before | awk '{print $6+$7+$10+$11}'`

echo $bef_RX_OK 
echo $bef_RX_DRP




