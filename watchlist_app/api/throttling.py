from rest_framework.throttling import UserRateThrottle

class ReviewCreateThrottle(UserRateThrottle):
    scope = 'review-create'

class ReviewListhrottle(UserRateThrottle):
    scope = 'review-list'