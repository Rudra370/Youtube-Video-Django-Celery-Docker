# Steps to setup the project

## 1. Clone the repository

```bash
git clone https://github.com/Rudra370/Youtube-Video-Django-Celery-Docker.git
```

## 2. Create folder for static files and media files

```bash
mkdir staticfiles
```

```bash
mkdir media
```

## 3. Create .env file

```bash
touch .env
```

## 4. Add YOUTUBE_KEYS in .env file

Keys must be separated by comma

```bash
YOUTUBE_KEYS=xyz,abc,123
```

## 5. Run docker containers

```bash
docker-compose up --build
```

This command will build the docker images and run the container

If you want to run the containers in background, use this command

```bash
docker-compose up --build -d
```

## 6. Run migrations

Run this command in another terminal

```bash
docker-compose exec backend python manage.py migrate
```

## 7. Create superuser

```bash
docker-compose exec backend python manage.py createsuperuser
```

## 8. Uncomment celery config in core/celery.py

We can't run this celery beat before migrations are done

```python
app.conf.beat_schedule = {
    'fetch_video': {
        'task' : 'fetch_video',
        'schedule': crontab(minute='*/5'),
    }
}
```

You can change the schedule as per your requirement

## 9. Restart the containers

```bash
docker-compose down
```

```bash
docker-compose up
```

## 10. Go to admin panel

```bash
http://localhost:8000/admin
```

## 11. Login with superuser credentials

Here you can view, edit, filter and sort all youtube video details

Admin panel view is also optimized to query least data from database

### 12. Get list of videos

```bash
http://localhost:8000/video/
```

You can also add page and page_size query parameters

By default page_size is 10 and page is 1

```bash
http://localhost:8000/video/?page=1&page_size=10
```

### 13. Query videos

```bash
http://localhost:8000/video/query/?q=your query string
```
