from __future__ import absolute_import, unicode_literals

from celery import shared_task
from django.conf import settings

from core.celery import app

from django.contrib.contenttypes.models import ContentType

from datetime import timedelta

from django.utils import timezone

from video.service import YoutubeService


@app.task(name="fetch_video")
def fetch_video(*args, **kwargs):
    youtube_service = YoutubeService(keyword="news", published_after=timezone.now() - timedelta(days=1))
    err, videos = youtube_service.get_videos()

    if err:
        print("Error while fetching videos: ", err)
    else:
        for video in videos:
            print(video, "saved")

