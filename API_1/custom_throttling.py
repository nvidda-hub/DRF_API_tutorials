from rest_framework.throttling import UserRateThrottle

class CustomThrottlingForUser(UserRateThrottle):
    scope = 'new_user'