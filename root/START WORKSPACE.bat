REM START cmd.exe
REM START python manage.py shell

REM
SET all=./eyevacs/views.py ./eyevacs/views_pcpt.py ./eyevacs/urls.py 
REM SET vimcmds=-c <C-wv>
rem START C:\Program" "Files\Vim\vim73\gvim.exe --servername LOG "./DJANGO LEARNING LOG.f30"
START C:/Program" "Files/Vim/vim73/gvim.exe --servername MAIN %all% %vimcmds%


REM START "C:\Program Files\Vim\vim73\gvim.exe -p3 ./eyevacs/views.py ./eyevacs/urls.py ./eyevacs/views_pcpt.py"
START Console2.bat
