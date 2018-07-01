#!/bin/bash
apt install expect
#acckers=("10.0.3.21" "10.0.3.34");
acckers=("192.168.1.10" "192.168.1.11" "192.168.1.12" "192.168.1.13");
user='main'
path='/home/main/'
password='main'

#-----------push get to accker--------------------#
for accker in ${acckers[@]};do
	expect -c "
  spawn scp -r ./get $user@$accker:$path
  expect {
    \"*assword\" {set timeout 2; send \"$password\r\";}
    \"yes/no\" {send \"yes\r\"; exp_continue;}
  }
  expect eof"
done

#-----------add victim-pub-key in accker----------#
cd $HOME
ssh-keygen
user='root'
password='root'
for accker in ${acckers[@]};do
	expect -c "
  spawn ssh-copy-id -i $HOME/.ssh/id_rsa.pub $user@$accker
  expect {
    \"*assword\" {set timeout 2; send \"$password\r\";}
    \"yes/no\" {send \"yes\r\"; exp_continue;}
  }
  expect eof"
done

#------------install package in test service-time accker------------#
testacckers=("192.168.1.10");
for accker in ${testacckers[@]};do
	ssh $user@$accker "chmod u+x /home/main/get/*.sh"
	ssh $user@$accker "sh /home/main/get/install-package.sh"
done
