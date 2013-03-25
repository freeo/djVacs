
echo off

start "" C:\Console2\Console.exe "E:\djVacs\root\python manage.py shell" -t "django iPython" -t "djVacs" -t "runserver"

set all=./eyevacs/views.py ./eyevacs/views_pcpt.py ./eyevacs/models.py ./eyevacs/static/css/layout.css ./templates/eyevacs/transit_select.html
start "" C:/Program" "Files/Vim/vim73/gvim.exe --servername MAIN %all% 


