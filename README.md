# learn-drf
``` Dockerizing```

## Installations

```sh
sudo docker-compose build
sudo docker-compose -f docker-compose-dev.yml run --rm web python manage.py makemigrations
sudo docker-compose -f docker-compose-dev.yml run --rm web python manage.py migrate
sudo docker-compose -f docker-compose-dev.yml run --rm web python manage.py create_groups_and_permissions
sudo docker-compose -f docker-compose-dev.yml up
```