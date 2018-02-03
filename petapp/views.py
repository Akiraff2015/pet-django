from django.shortcuts import render
from .models import Pet

# Create your views here.
def index(request):
    if request.method == 'GET':
        print("hello get")

    if request.method == 'POST':
        new_pet = Pet()
        new_pet.save()

        print("hello post")

    return render(request, 'petapp/index.html')