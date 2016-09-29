from django.contrib import admin
from django.conf.urls import url, include

from rest_framework.authtoken import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/', include('users.urls')),
    url(r'^currencies/', include('subscriptions.urls'))
]

# login-auth
urlpatterns += [
    url(r'^auth/', views.obtain_auth_token)
]