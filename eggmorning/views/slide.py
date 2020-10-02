from django.http import HttpResponse
from django.http import JsonResponse
from django.core.serializers import serialize

from eggmorning import models


# Create your views here.

def index(request):
    models.Hotel.check()
    return HttpResponse("Hello, world.")


def get_main_slide_list(request):
    result = models.MainSlide.objects.all().values()
    return JsonResponse({'result': list(result)}, safe=False)


def get_one_main_slide(request, slide_id):
    filtered_slide_list = models.MainSlide.objects.filter(id=slide_id).values()
    if not filtered_slide_list:
        filtered_slide_list = ['']
    return JsonResponse({'result': filtered_slide_list[0]}, safe=False)

