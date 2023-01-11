from datetime import datetime
from typing import List, Optional, Tuple
from core.settings import YOUTUBE_KEYS
import requests
from video.models import Video, Thumbnail

class YoutubeService:

    def __init__(self, keyword: str, published_after: datetime) -> None:
        '''
            :param keyword: keyword to search
            :param published_after: datetime object
        '''
        self.keyword = keyword
        # converting datetime to 2023-01-10T10:06:11Z format
        self.published_after = published_after.strftime("%Y-%m-%dT%H:%M:%SZ")
        self.api_keys = YOUTUBE_KEYS.split(',')
        self.current_key = 0

    
    def __make_request(self, retry:bool=False)-> Tuple[Optional[str], Optional[dict]]:
        '''
            :return: Tuple[Optional[str], Optional[dict]]
            returns a tuple of error and response
        '''

        path = "https://youtube.googleapis.com/youtube/v3/search"
        params = {
            "part": "snippet",
            "q": self.keyword,
            "type": "video",
            "publishedAfter": self.published_after,
            "key": self.api_keys[self.current_key]
        }
        headers = {
            "Accept": "application/json"
        }

        try:
            response = requests.get(path, params=params, headers=headers)
            response.raise_for_status()
            return None, response.json()
        except Exception as err:
            if not retry:
                self.current_key += 1
                if self.current_key < len(self.api_keys):
                    return self.__make_request(retry=True)
            return str(err), None
    
    def get_videos(self) -> Tuple[Optional[str], Optional[List[Video]]]:
        '''
            retun: Tuple[Optional[str], Optional[List[Video]]]
        '''
        err, response = self.__make_request()
        if err:
            return err, None
        try:
            videos = []
            for item in response.get('items', []):
                if not isinstance(item, dict):
                    continue
                video = Video.objects.create(
                    video_id=item.get('id', {}).get('videoId'),
                    title=item.get('snippet', {}).get('title'),
                    description=item.get('snippet', {}).get('description'),
                    published_at=self.get_date_time_from_str(item.get('snippet', {}).get('publishedAt')),
                    channel_id=item.get('snippet', {}).get('channelId'),
                    channel_title=item.get('snippet', {}).get('channelTitle'),
                )
                thumbnails = []
                for key, value in item.get('snippet', {}).get('thumbnails', {}).items():
                    thumbnails.append(Thumbnail(
                        video=video,
                        type=key,
                        url=value.get('url'),
                        width=value.get('width'),
                        height=value.get('height'),
                    ))
                Thumbnail.objects.bulk_create(thumbnails)
                videos.append(video)
            return None, videos
        except Exception as err:
            return str(err), None
    
    def get_date_time_from_str(self, date_time_str: str) -> datetime:
        '''
            retun: datetime
        '''
        return datetime.strptime(date_time_str, "%Y-%m-%dT%H:%M:%SZ")
