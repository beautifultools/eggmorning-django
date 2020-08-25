from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('main/slide', views.get_man_slide, name='main_slide'),
    path('signup', views.signup, name='signup'),
]
