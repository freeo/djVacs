echo off
SET all=./eyevacs/views.py ./eyevacs/views_pcpt.py ./eyevacs/models.py ./eyevacs/static/css/layout.css ./templates/eyevacs/transit_select.html
start "" C:/Program" "Files/Vim/vim73/gvim.exe --servername MAIN %all%


