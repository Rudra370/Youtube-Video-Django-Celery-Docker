from django.http import JsonResponse
from utils.paginator import PaginatorService

class CustomResponse(JsonResponse):
    def __init__(self, data:dict, paginator:PaginatorService=None, **kwargs):
        data = {
            'data': data,
        }
        if paginator:
            data['page'] = paginator.page
            data['page_size'] = paginator.page_size
            data['has_next'] = paginator.has_next()
            data['pages'] = paginator.pages()
        super().__init__(data)