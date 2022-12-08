> === THE TASK ===

See my django app and postgres backend here... http://junder.ddns.net ==> Need to be able to edit and remove the rooms otherwise all is working and took me about 6hrs total time to get to where it is now 

Software Challenge - Paint Calculator

The purpose of this software challenge is to give you an opportunity to showcase how you think code should be written. It should be a demonstration of your skills and opinions.
Instructions

The solution should be completed using a TDD approach
Consider the use of comments where appropriate
Ensure your code is clean and readable. We value readable code over “clever” solutions
Ensure your solution contains a README with instructions on how to build and run your application
Your submission should be in the form of a Git repository
You should use Git tooling to provide a granular commit history
You are free to use whatever tools, libraries, and frameworks that you see fit
Prefer using technologies relevant to the role. For example, using web technologies for a web role
Don’t be shy to showcase your DevOps enthusiasm or experience!
State any assumptions made
Limit your time to 4 hours, and explain what you would refine if you had more time on the project
Scenario
Write a program that takes as input the dimensions of a room and outputs the following:

Area of the floor
Amount of paint required to paint the walls
Volume of the room

> === FONTEND SECTION ===

used to interact with the database from docker shell

python manage.py shell    
from app.models import Room
room.name = "room_one"
room.width = 1
room.depth = 1 # set everything to avoid not null exception
room.height = 1
room.save()
Room.objects.all()[0].name

> === BACKEND SECTION ===

Navigate to the django dir then run:::

python manage.py makemigrations <myapp>
docker-compose up -d --build
docker-compose exec web python manage.py migrate

,for local development with postgresql docker services currently excluded from the git.

docker-compose exec web python manage.py createsuperuser
(((root githubpass)))
  
DELETE FROM public.app_room
  
> === USEFUL COMMANDS ===

  docker-compose up -d

  docker-compose down

  DOCKER_BUILDKIT=1 docker build . -t jaynericguy/paintapp-django-armv8

  docker push jaynericguy/paintapp-django-armv8
