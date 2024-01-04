### === Creation / edits have been made in all the files listed below ===  
  
Note, when serving static content like images or gif django is less prefered, ideally use s3 bucket or whatever cdn, then simply link to with href...  
  
/django/app/app/forms.py  
/django/app/app/urls.py  
/django/app/app/models.py  
/django/app/app/settings.py ==> only tweaks have been made here, further tweaks need to be made to hide .envs for this .py file.  
/django/app/app/veiws.py  
/django/app/app/static/gif/room.gif  
/django/app/app/templates/((home, index, roomsview, roomview, roomsadd)).html  
/django/app/app/migrations/((0001...,0002...0003...,)).py ==> can simply run django migrations to interact with postgres database, in past ive manually had to update entries in postgres production environments for sentry users to get them access at old workspace alongside using migrations to recover database from backup.    
  
### === THE TASK ===  
  
Django + postgres  ==> Ive configured django with postgres in such a way that any room created by the app is stored in the postgres databse as name, width, height, depth, creation-date and slug. This allows for my django model to operate freely on this information to get volume, floor-size etc etc. This url-slug is also all the information that is required in the store to then dynamically create the page to view/((update-wip)) individual rooms width, height, depth information in the database via my django forms methods accesed in associated views.py. Currently, a room is fixed in dimensions once created and has to be deleted and re-created by the user to make single changes to say its width, can simply extend the django form a bit to allow tweaking of pre-existing room data to avoid re-entering all dimensions again.     
  
This django app creates and stores as many rooms as the slug randomness or database size constraints for name width height depth slug creation-date allows, so quite a lot knowing postgres with such minimal info. Has been succesfully working in my rke cluster to modify any rooms I create, am just missing functionality screenshots/demo of https://github.com/jabl3s/OLD_rke1_arm_v1  :c         
  
### === USEFUL COMMANDS ===  
DOCKER_BUILDKIT=1 docker build . -t jabl3s/paintapp-django-armv8  
docker build . -t jabl3s/paintapp-django-armv8 --platform linux/arm64/v8  
docker push jabl3s/paintapp-django-armv8  
##  
docker compose up -d --no-deps --build web    
docker compose run web python manage.py makemigrations||migrate
##  
 
git remote -v    ==> check if its connecting via https or ssh, if not ssh do below for git push to work:::  
git remote set-url origin git@github.com:junder-git/K3scluster_django_postgres_demo_app.git  
  
git pull         ==> If updating locally via git pull be sure to delete any local conflicting files then run pull  
git commit       ==> Ctrl+o ==> Ctrl+x for nano save  
git push  
  
