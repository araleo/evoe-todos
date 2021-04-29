from django.urls import include
from django.urls import path
from rest_framework import renderers
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'api'

todo_list = views.ToDoViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('todos/', todo_list, name='todo-list'),
    path('todos/<int:pk>/', views.ToDoDetail.as_view(), name='todo-detail'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
])