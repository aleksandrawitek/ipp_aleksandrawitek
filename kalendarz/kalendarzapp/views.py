from django.shortcuts import render


# Create your views here.


def glowna(request):
    return render(request, 'kalendarzapp/glowna.html', {})