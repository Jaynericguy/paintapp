=== Creation / edits have been made to the following files listed below ===  
/django/app/ap/forms.py  
/django/app/app/urls.py  
/django/app/app/models.py  
/django/app/app/settings.py ==> tweaks have been made here and further tweaks nee to be made to be hide .envs for this .py file.  
/django/app/app/veiws.py
/django/app/app/static/gif/room.gif
/django/app/app/templates/((home, index, roomsview, roomview, roomsadd)).html
/django/app/app/migrations/((0001...,0002...0003...,)).py ==> can simply run django migrations to interact with postgres database, in past ive manually had to update entries in postgres production environments for sentry users to get them access at old workspace.  
  
=== THE TASK ===  
  
Django + postgres  
  
=== USEFUL COMMANDS ===  
DOCKER_BUILDKIT=1 docker build . -t jabl3s/paintapp-django-armv8  
docker build . -t jabl3s/paintapp-django-armv8 --platform linux/arm64/v8  
docker push jabl3s/paintapp-django-armv8  

  
