from django.http import JsonResponse
from datetime import datetime, timedelta

from eggmorning.models import MainSlide


def get_main_slide_list(request):
    result = MainSlide.objects.all().values()
    return JsonResponse({'result': list(result)}, safe=False)


def get_one_main_slide(request, slide_id):
    filtered_slide_list = MainSlide.objects.filter(id=slide_id).values()
    if not filtered_slide_list:
        filtered_slide_list = ['']
    return JsonResponse({'result': filtered_slide_list[0]}, safe=False)


def create_dummy_slide(request):
    current_slides_count = MainSlide.objects.all().count()
    target_num = current_slides_count + 1
    main_slide = MainSlide(
        title=f'test{target_num}',
        image="https://cookieandkate.com/images/2018/09/crispy-fried-egg-recipe.jpg",
        username=f'testuser{target_num}',
        priority=target_num,
        start_date=datetime.now(),
        end_date=datetime.now() + timedelta(days=30)
    )
    main_slide.save()
    return JsonResponse({'result': True}, safe=False)

