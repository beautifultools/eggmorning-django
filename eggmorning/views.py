from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.http import JsonResponse
from datetime import datetime
from . import models


# Create your views here.

def index(request):
    models.Hotel.check()
    return HttpResponse("Hello, world.")


class MainSlide(View):
    def get(self, request):
        queryset = models.MainSlide.check()
        return JsonResponse({'result': 123})

    def put(self, request):
        queryset = MainSlide(priority=1, url='http://test/')
        result = queryset.save()
        print(f'result : {result}')
        return HttpResponse("Put 요청을 잘받았다")


def save_main_slide(request):
    queryset = models.MainSlide(priority=1, img_url='http://test/', start_date=datetime.today(), end_date=datetime.today())
    queryset.save()
    # print(f'result : {result}')
    return HttpResponse("Put 요청을 잘받았다")
