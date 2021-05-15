from django.urls import path

from . import views
urlpatterns = [
    path('about/', views.about, name='about'),
    path('', views.home, name='home'),
    path('add-page/', views.add_page, name='add-page'),
    path('login/', views.login, name='login'),
    path('post/<int:id>/', views.show_post, name='post')
    ]
