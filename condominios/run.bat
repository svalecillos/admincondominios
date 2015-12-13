@ECHO OFF
cd ../../Scripts/
dir
activate
cd ../admincondominios/condominios

if "%1" == "web" goto iniciar
if "%1" == "migrar" goto crear_migracion
if "%1" == "db" goto migrar



:iniciar
goto iniciar_defecto

:iniciar_defecto
python manage.py runserver 1025 --settings=condominios.settings.local

:iniciar_puerto
python manage.py runserver "%2" --settings=condominios.settings.local

:crear_migracion
python manage.py makemigrations %2 --settings=condominios.settings.local

:migrar
python manage.py migrate %2 --settings=condominios.settings.local

