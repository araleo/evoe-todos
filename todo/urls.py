from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.home, name='index'),
    path('<int:todo_id>/', views.detail, name='detail'),
    path('readthedocs', views.docs, name='docs'),
]
