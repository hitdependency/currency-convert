from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^(?P<id>\d+)/$', UserDetailView.as_view()),
    url(r'^$', UsersView.as_view()),
    url(r'^(?P<id>\d+)/subscriptions/', UserSubscriptionsControl.as_view()),
]
