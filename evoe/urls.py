from django.contrib import admin
from django.urls import include
from django.urls import path

from todo.views import register


urlpatterns = [
    # admin
    path('admin/', admin.site.urls),

    # api
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),

    # app
    path('todo/', include('todo.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register),
]
