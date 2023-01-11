from django.db import models

# {
#     "kind": "youtube#searchResult",
#     "etag": "fQHIoRFZ7LhAR97AL-ywo1kmlDs",
#     "id": {
#         "kind": "youtube#video",
#         "videoId": "sd8ecOToG38"
#     },
#     "snippet": {
#         "publishedAt": "2023-01-11T09:00:57Z",
#         "channelId": "UCMk9Tdc-d1BIcAFaSppiVkw",
#         "title": "Ukraine Russia War News | War News | Zelenskyy |  यूक्रेन में महीनों बाद...Putin को जीत की सौगात!",
#         "description": "कब्जे में नमक की खान... बखमुट का काउंटडाउन! यूक्रेन में महीनों बाद.",
#         "thumbnails": {
#             "default": {
#                 "url": "https://i.ytimg.com/vi/sd8ecOToG38/default.jpg",
#                 "width": 120,
#                 "height": 90
#             },
#             "medium": {
#                 "url": "https://i.ytimg.com/vi/sd8ecOToG38/mqdefault.jpg",
#                 "width": 320,
#                 "height": 180
#             },
#             "high": {
#                 "url": "https://i.ytimg.com/vi/sd8ecOToG38/hqdefault.jpg",
#                 "width": 480,
#                 "height": 360
#             }
#         },
#         "channelTitle": "TIMES NOW Navbharat",
#         "liveBroadcastContent": "none",
#         "publishTime": "2023-01-11T09:00:57Z"
#     }
# }

# from datetime import datetime

# s = "2023-01-11T09:00:57Z"
# d = datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ")
# print(d)

class Video(models.Model):
    video_id = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    published_at = models.DateTimeField()
    channel_title = models.CharField(max_length=255)
    channel_id = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    thumbnails: models.QuerySet["Thumbnail"]

class Thumbnail(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="thumbnails")
    url = models.URLField()
    width = models.IntegerField()
    height = models.IntegerField()
    type = models.CharField(max_length=255)