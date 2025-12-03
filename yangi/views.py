from django.shortcuts import render

def about_page(request):
    return render(request, "about.html")

def test_page(request):
    return render(request, "test.html")

def contacts_page(request):
    return render(request, "contact.html")
