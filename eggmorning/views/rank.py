from django.http import JsonResponse

from eggmorning.models import HotelScore, RankCategory


def get_rank_cat_list():
    result = RankCategory.objects.all().values()
    return JsonResponse({'result': list(result)}, safe=False)


def get_top_rank_list(request, category_code):
    filtered_slide_list = HotelScore.objects.filter(category=category_code).order_by('score').values()
    if not filtered_slide_list:
        filtered_slide_list = ['']
    return JsonResponse({'result': filtered_slide_list[0]}, safe=False)

