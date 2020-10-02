from django.urls import path

from .views import slide
from .views import user
from .views import etc

urlpatterns = [
    path('', etc.index, name='index'),
    path('main/slide', slide.get_main_slide_list, name='main_slide'),
    path('main/slide/<int:slide_id>', slide.get_one_main_slide, name='main_slide'),
    path('user', user.signup, name='signup'),
    path('session', user.login, name='login')
]
