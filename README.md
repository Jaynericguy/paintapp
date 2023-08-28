=== THE TASK ===  

See my django app and postgres backend here... https://paint.jabl3s.uk 

=== USEFUL COMMANDS ===  
DOCKER_BUILDKIT=1 docker build . -t jaynericguy/paintapp-django-armv8  
docker build . -t jaynericguy/paintapp-django-armv8 --platform linux/arm64/v8  
docker push jaynericguy/paintapp-django-armv8  

  
