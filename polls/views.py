from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello this is supposed to be the index page.")

# Create your views here.
