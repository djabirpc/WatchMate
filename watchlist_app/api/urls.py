from django.urls import path,include
from rest_framework.routers import DefaultRouter

from watchlist_app.api.views import (WatchListAV,
                                        WatchDetailAV,
                                        StreamPlatformVS,
                                        StreamPlatformMVS,
                                        ReviewList,
                                        ReviewDetail,
                                        ReviewCreate,
                                        UserReview,
                                        WatchListFilter,
                                        WatchListPagination)

router = DefaultRouter()
router.register('stream', StreamPlatformMVS, basename='streamplatform')

urlpatterns = [
    path('list/',WatchListAV.as_view(),name='movie-list'),
    path('<int:pk>/',WatchDetailAV.as_view(),name='movie-details'),
    path('listf/',WatchListFilter.as_view(),name='watch-filter'),
    path('listp/',WatchListPagination.as_view(),name='watch-pagination'),

    path('',include(router.urls)),

    # path('stream/',StreamPlatformAV.as_view(),name='stream-list'),
    # path('stream/<int:pk>',StreamPlatformDetailAV.as_view(),name='stream-detail'),

    # path('review',ReviewList.as_view(),name='review-list'),
    # path('review/<int:pk>',ReviewDetail.as_view(),name='review-details'),

    path('<int:pk>/review/',ReviewList.as_view(),name='review-list'),
    path('<int:pk>/review-create/',ReviewCreate.as_view(),name='review-create'),
    path('review/<int:pk>/',ReviewDetail.as_view(),name='review-detail'),
    # path('review/<str:username>/',UserReview.as_view(),name='user-review-detail'),
    path('review/',UserReview.as_view(),name='user-review-detail'),

    
]
