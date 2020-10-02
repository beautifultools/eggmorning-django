from django.contrib.auth import authenticate
from ..models.user import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        nickname = request.POST.get('nickname', '')
        phone = request.POST.get('phone', '')
        birth = request.POST.get('birth', '2020-08-20')
        gender = request.POST.get('gender', '')

        if email and password and nickname:
            User.objects.create_user(
                email=email,
                nickname=nickname,
                password=password,
                phone=phone,
                birth=birth,
                gender=gender
            )
            return JsonResponse({'result': True}, safe=False)
        else:
            return JsonResponse({'result': False, 'message': 'email or password or nickname is empty'}, safe=False)


@csrf_exempt
def login(request):
    username = request.GET.get('id', '')
    password = request.GET.get('password', '')

    if username and password:
        user = authenticate(email=username, password=password)
        if user is not None:
            return JsonResponse({'result': True}, safe=False)
        else:
            return JsonResponse({'result': False, 'message': 'id or password is not correct.'}, safe=False)
    else:
        return JsonResponse({'result': False, 'message': 'id or password is empty.'}, safe=False)

