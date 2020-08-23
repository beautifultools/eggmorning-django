from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('main/slide', views.MainSlide.as_view(), name='main_slide'),
    path('main/slide/save', views.save_main_slide, name='main_slide_save'),
]
