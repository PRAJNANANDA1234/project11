from django.shortcuts import render

# Create your views here.
def pink(request):
    return render(request,'pink.html')