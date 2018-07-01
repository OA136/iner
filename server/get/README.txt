1、get.py为攻击脚本，insert.py是将服务响应时间插入到数据库中
service-time.py是采集服务响应时间的指标，并将其暂存本机的redis数据库
settings.py存储着mysql数据库的信息，以及网卡名称

2、其他sh脚本主要为了测试在本机运行的准确性，server通过ssh命令来运行.py文件，
从而控制整个流程

3、python http://192.168.0.10/ 线程个数