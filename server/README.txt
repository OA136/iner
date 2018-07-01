数据库表说明：
	result：	存储汇总结果
	originals：	存储每次攻击的所有指标值
	inf：		暂存每次攻击的所有指标值
	SERVICE:	暂存每次攻击的服务响应时间
	tags：		存储从result计算的最终的归一化数据

1、后台运行脚本即可开始总体测试执行：
	nohup ./control.sh > ./log/control.log &

2、参数可以在control.sh中进行调整

3、avg_inf.py:将一次攻击采集到的指标归为一条，并根据service的值进行区间统计，并将其存入到result表中

4、cpu.py drop.py tcp_mem.py width.py 分别用来采集cpu频率、丢包率、tcp连接数和内存、带宽占用

5、init.py:初始化inf和SERVICE表，即将其中的数据清空 result_init.py:将result表中的数据清空

6、getrecords_num.py：获取采集指标的条数

7、connections.sh:用来统计连接数，被tcp_mem.py调用，drop.sh被drop.py调用

8、dealwith_inf.py：用来将攻击指标加入到inf表中，并删除攻击前后的数据，只保留攻击阶段的数据，删除SERVICE是null的记录，
之后将其复制到originals表中

9、insert_every_table.py：将采集的指标从redis中存入到数据库表inf中

10、kill.sh：kill所有采集指标的程序，kill-attack.sh：暂停攻击

11、start.sh：开始采集指标 start-attack.sh:开始攻击

12、allrun.sh:起到逻辑控制作用，被control.sh调用，其可修改攻击前后时长




采集阶段，将指标存入本机的redis数据库，在攻击以及采集结束后，再进行数据库写入操作；
settings.py中存储着mysql数据库信息，以及网卡名称

13、scp-get-to-acckers.sh：
		是将本目录下的get文件夹分发到攻击者的家目录下，
		并自动配置ssh免密登录
		之后再一个测试者（accker）中执行./get下的install-package.sh脚本（用来安装配置redis和mysql客户端）
		可以在此脚本中加入acckers的IP列表即可
	delete-get-to-acckers.sh：
		将攻击者家目录下的get文件夹删除
14、当前目录下的install-package.sh用来安装配置redis和mysql客户端
