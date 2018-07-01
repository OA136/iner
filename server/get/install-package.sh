apt install expect
#acckers=("10.0.3.21" "10.0.3.34");
#---------------install and configure redis----------#
expect -c "
  spawn apt-get install redis-server
  expect {
    \"*\[Y/n\]\" {set timeout 2; send \"y\r\";}
    \"*\[y/n\]\" {set timeout 2; send \"y\r\";}
  }
  expect eof"

redispwd='123'
redispath='/etc/redis/redis.conf'
sed -i 's/^bind 127.0.0.1/#bind 127.0.0.1/' $redispath
result=`grep -n "requirepass $redispwd" $redispath`
if [ -z "$result" ]; then	
	sed -i '$a\requirepass '"$redispwd" $redispath
fi
/etc/init.d/redis-server restart
#---------------end redis-----------------------------#

#---------------install python redis-connector--------#

expect -c "
  spawn pip install redis
  expect {
    \"*\[Y/n\]\" {set timeout 20; send \"y\r\";}
    \"*\[y/n\]\" {set timeout 20; send \"y\r\";}
  }
  expect eof"

#---------------end py-redis-con----------------------#


#---------------install mysql-client-core-5.7--------#

expect -c "
  spawn apt-get install mysql-client-core-5.7
  expect {
    \"*\[Y/n\]\" {set timeout 30; send \"y\r\";}
    \"*\[y/n\]\" {set timeout 30; send \"y\r\";}
  }
  expect eof"

#---------------end mysql-client----------------------#

