@ECHO OFF&PUSHD %~DP0 &TITLE MBRREP
mode con cols=50 lines=30
color 9F
@echo. ��Ҫ����Ա��Ȩ������Ȩ�ޣ��������Ȩ�����򽫻��˳�
@PAUSE
chkdsk
sfc /scannow
