���ݿ��˵����
	result��	�洢���ܽ��
	originals��	�洢ÿ�ι���������ָ��ֵ
	inf��		�ݴ�ÿ�ι���������ָ��ֵ
	SERVICE:	�ݴ�ÿ�ι����ķ�����Ӧʱ��
	tags��		�洢��result��������յĹ�һ������

1����̨���нű����ɿ�ʼ�������ִ�У�
	nohup ./control.sh > ./log/control.log &

2������������control.sh�н��е���

3��avg_inf.py:��һ�ι����ɼ�����ָ���Ϊһ����������service��ֵ��������ͳ�ƣ���������뵽result����

4��cpu.py drop.py tcp_mem.py width.py �ֱ������ɼ�cpuƵ�ʡ������ʡ�tcp���������ڴ桢����ռ��

5��init.py:��ʼ��inf��SERVICE���������е�������� result_init.py:��result���е��������

6��getrecords_num.py����ȡ�ɼ�ָ�������

7��connections.sh:����ͳ������������tcp_mem.py���ã�drop.sh��drop.py����

8��dealwith_inf.py������������ָ����뵽inf���У���ɾ������ǰ������ݣ�ֻ���������׶ε����ݣ�ɾ��SERVICE��null�ļ�¼��
֮���临�Ƶ�originals����

9��insert_every_table.py�����ɼ���ָ���redis�д��뵽���ݿ��inf��

10��kill.sh��kill���вɼ�ָ��ĳ���kill-attack.sh����ͣ����

11��start.sh����ʼ�ɼ�ָ�� start-attack.sh:��ʼ����

12��allrun.sh:���߼��������ã���control.sh���ã�����޸Ĺ���ǰ��ʱ��




�ɼ��׶Σ���ָ����뱾����redis���ݿ⣬�ڹ����Լ��ɼ��������ٽ������ݿ�д�������
settings.py�д洢��mysql���ݿ���Ϣ���Լ���������

13��scp-get-to-acckers.sh��
		�ǽ���Ŀ¼�µ�get�ļ��зַ��������ߵļ�Ŀ¼�£�
		���Զ�����ssh���ܵ�¼
		֮����һ�������ߣ�accker����ִ��./get�µ�install-package.sh�ű���������װ����redis��mysql�ͻ��ˣ�
		�����ڴ˽ű��м���acckers��IP�б���
	delete-get-to-acckers.sh��
		�������߼�Ŀ¼�µ�get�ļ���ɾ��
14����ǰĿ¼�µ�install-package.sh������װ����redis��mysql�ͻ���
