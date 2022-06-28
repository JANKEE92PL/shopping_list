from unicodedata import name
from django.shortcuts import render
from .models import ShoppingItem

# Create your views here.

def mylist(request):
    if request.method == 'POST':
        print('Received data:' , request.POST['itemName'])
        ShoppingItem.objects.create(name= request.POST['itemName'])
    return render(request, 'shopping_list.html')