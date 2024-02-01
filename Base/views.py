from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from .models import Rooms
from .forms import RoomForm

#rooms = [
#    {'id': 1, 'name' : 'Lets learn Python'},
#    {'id': 2, 'name' : 'Front End developers'},
#    {'id': 3, 'name' : 'Lets do Django'},
#    {'id': 4, 'name' : 'Lets do soft skills here'},
#    {'id': 5, 'name' : 'hello there'},
#]

def home(request):
    rooms = Rooms.objects.all()
    return render (request,'Base/home.html', {'rooms' : rooms})

def room(request,pk):
    room = Rooms.objects.get(id = pk)
    content = {'room': room}
    return render (request,'Base/room.html',content)

def CreateRoom(request):
    form = RoomForm
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save() 
            #return redirect('/')

    context = {'form': form}
    return render(request, 'Base/create_room.html', context )
    
    

