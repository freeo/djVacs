TITLE EYEVACS: OXIQUATL loading fixtures
ECHO OFF
REM echo off, so it doesnt print ALL the lines!
REM This batch file loads all json fixtures for the experimental OXIQUATL eyevacs experiment!

REM CLS CLEARS the DOS screen
CLS

REM ACTUAL CODE
ECHO loading fixtures for the eyevacs experiment OXIQUATL

python manage.py loaddata EXP_OXIQUATL_de_1_FIX

python manage.py loaddata OXIQUATL_CT2_ID1.json
python manage.py loaddata OXIQUATL_CT3_ID2.json
python manage.py loaddata OXIQUATL_CT4_ID3.json
python manage.py loaddata OXIQUATL_CT5_ID4.json
python manage.py loaddata OXIQUATL_CT6_ID5.json
python manage.py loaddata OXIQUATL_CT7_ID6.json
python manage.py loaddata OXIQUATL_CT8_ID7.json

REM PAUSE is for: press any key to continue...
PAUSE

