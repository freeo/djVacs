echo off
REM START powershell.exe -noexit -command "python manage.py shell --plain"
REM python manage.py shell --plain
REM -Command python manage.py shell 
START "" C:\Console2\Console.exe "E:\djVacs\root\python manage.py shell" -t "django iPython" -t "djVacs" -t "runserver"
