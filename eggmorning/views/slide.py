from django.http import JsonResponse

from eggmorning.models import MainSlide


def get_main_slide_list(request):
    result = MainSlide.objects.all().values()
    return JsonResponse({'result': list(result)}, safe=False)


def get_one_main_slide(request, slide_id):
    filtered_slide_list = MainSlide.objects.filter(id=slide_id).values()
    if not filtered_slide_list:
        filtered_slide_list = ['']
    return JsonResponse({'result': filtered_slide_list[0]}, safe=False)

