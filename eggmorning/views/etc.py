from django.http import HttpResponse

from eggmorning import models


# Create your views here.
def index(request):
    models.Hotel.check()
    return HttpResponse("Hello, world.")
