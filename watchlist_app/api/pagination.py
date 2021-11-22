from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination

class WatchListPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'p'
    page_size_query_param = 'size'
    max_page_size = 10 # meme si size = 100 tab9a twarilo 10
    last_page_strings = 'end'

#offset = 10
#it means we will skip first 10 elements 
#and load result from 11
class WatchListLOPagination(LimitOffsetPagination):
    default_limit = 3
    max_limit = 5
    limit_query_param = 'limit'
    offset_query_param = 'start'

class WatchListCPagination(CursorPagination):
    page_size = 3
    ordering = 'created'
    cursor_query_param = 'record'