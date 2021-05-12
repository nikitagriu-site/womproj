from django.urls import path, re_path

from . import views
urlpatterns = [
    path('cats/<int:catid>/', views.category),
    re_path(r'^archive/(?P<year>[0-9]{4})/', views.archive)
    
    ]
