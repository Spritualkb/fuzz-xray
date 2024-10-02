@echo off
:: 获取当前时间戳
for /f "tokens=1-5 delims=:. " %%a in ("%date% %time%") do (
    set timestamp=%%a-%%b-%%c_%%d-%%e
)

:: 设置文件名
set filename=proxy_%timestamp%.html

:: 运行命令并输出到包含时间戳的文件
xray.exe webscan --listen 127.0.0.1:7777 --html-output %filename%

pause
