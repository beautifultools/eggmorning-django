from django.http import HttpResponse
from django.http import JsonResponse

from . import models


# Create your views here.

def index(request):
    models.Hotel.check()
    return HttpResponse("Hello, world.")


def get_man_slide(request):
    result = models.MainSlide.objects.all().values()
    return JsonResponse({'result': list(result)}, safe=False)


def get_session(request):
    result = models.MainSlide.objects.all().values()
    return JsonResponse({'result': list(result)}, safe=False)


def signup(request):
    user_id = request.GET.get('id', '')
    password = request.GET.get('password', '')
    name = request.GET.get('name', '')
    phone = request.GET.get('phone', '')
    birth = request.GET.get('birth', '2020-08-20')
    gender = request.GET.get('gender', '')

    if user_id and password:
        new_user = models.User(user_id=user_id, password=password, name=name, phone=phone, birth=birth, gender=gender)
        new_user.save()
        return JsonResponse({'result': True}, safe=False)
    else:
        return JsonResponse({'result': False, 'message': 'id or password is empty'}, safe=False)



