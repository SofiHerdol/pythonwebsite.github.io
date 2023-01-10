from django.shortcuts import render

def index_hi(request):
    return render(request, "index.html", context={})