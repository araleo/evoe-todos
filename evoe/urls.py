from django.contrib import admin
from django.urls import include
from django.urls import path

from todo.views import register

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),

    # accounts
    path('accounts/', include('django.contrib.auth.urls'), name='accounts'),
    path('register/', register, name='register'),

    # api
    path('api/', include('api.urls')),

    # app
    path('', include('todo.urls'), name='todo'),
]
