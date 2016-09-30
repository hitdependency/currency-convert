from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', SubscriptionsView.as_view()),
    url(r'^(?P<id>.+)/$', SubscriptionsDetailView.as_view())
]
