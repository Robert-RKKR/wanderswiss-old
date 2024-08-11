## Backend - server configuration
### Python - virtual environment
**Create a new virtual environment:**
```bash
python3 -m venv venv
```
**Activate virtual environment:**
```bash
source venv/bin/activate
```

### GitHub - base account configuration
```bash
git config --global user.name <USERNAME>
git config --global github.token <TOKEN>
```

### Docker

**Run a new postgres container**
```bash
sudo docker run --name capybara-postgres -e POSTGRES_USER=postgres_admin -e POSTGRES_DB=capybara -e POSTGRES_PASSWORD='jt3g339d25rg0ea24' -p 5432:5432 -d postgres:latest
sudo docker run --name capybara-redis -d -p 6379:6379 redis
# With network:
sudo docker network create capybara_network
sudo docker run --name capybara-postgres -e POSTGRES_USER=postgres_admin -e POSTGRES_DB=capybara -e POSTGRES_PASSWORD='jt3g339d25rg0ea24' -p 5432:5432 --network capybara_network -d postgres:latest
sudo docker run --name capybara-redis --network capybara_network  -d -p 6379:6379 redis
```
**Show all containers**
```bash
sudo docker ps -a
```
**Start / stop / remove container**
```bash
sudo docker start <NAME>
sudo docker stop <NAME>
sudo docker rm <NAME>
```
**Base commands**
```bash
sudo docker-compose build
sudo docker-compose up
sudo docker-compose run -rm app sh -c <NAME>
```
**Clean all containers**
```bash
docker system prune -a --volumes
```
**Restart and run docker compose**
```bash
docker-compose down
docker-compose up --build
```

## Backend - app configuration

### Back up - database
**Backup data:**
```bash
python manage.py dumpdata inventory connections.Template connections.Policy management.Administrator management.GlobalSettings > backup_data.json
```
**Load backup:**
```bash
python manage.py loaddata backup_data.json
```

### celery - commands
```bash
celery -A capybara worker -Q collect_hosts -l INFO
celery -A capybara worker --loglevel=info
celery -A capybara beat --loglevel=info
```

### Pytest  - commands
```bash
export DJANGO_SETTINGS_MODULE=capybara.settings
```

### Pip install commands
```bash
pip install django
pip install django-jazzmin
pip install django-channels
pip install channels_redis
pip install django-celery-beat
pip install psycopg2-binary
pip install django-json-widget
pip install django-jsonform
pip install colorama
pip install pytest-django
pip install djangorestframework
pip install djangorestframework-extensions
pip install cryptography
pip install jinja2
pip install django-filter
pip install whitenoise
```

## Other information

### Open APIs
[All open APIs forum](https://rapidapi.com/collection/list-of-free-apis)
