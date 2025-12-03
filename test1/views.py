from django.shortcuts import render

# Create your views here.

def test1_page(request):
    return render(request, 'test.html')