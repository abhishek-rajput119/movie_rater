from django.shortcuts import HttpResponse

# Create your views here.
def first_view(request):
    return HttpResponse("Setup completed")
