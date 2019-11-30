@ECHO OFF&PUSHD %~DP0 &TITLE MBRREP
mode con cols=50 lines=30
color 9F
@echo. 需要管理员特权，请检查权限，如果不授权，程序将会退出
@PAUSE
chkdsk
sfc /scannow
