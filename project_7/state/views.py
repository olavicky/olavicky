from django.shortcuts import render


# Create your views here.
def city(request):
    return render(request, "state/index.html")
