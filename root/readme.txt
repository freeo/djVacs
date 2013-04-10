Note: all script files have to be executed from within this parent folder! This is due to the corresponding "shell", which is invoked by:

python manage.py shell --plain

This is needed for the relative adressing to work properly from within the "scripts" folder.

Other commands , which are used frequently *(google them):
python manage.py syncdb
python manage.py schemamigration eyevacs --initial
python manage.py schemamigration eyevacs --auto
python manage.py migrate eyevacs
python django-admin.py makemessages --all
python django-admin.py compilemessages

