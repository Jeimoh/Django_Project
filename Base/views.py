from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from .models import Rooms,Message
from .forms import RoomForm,MessagesForm

#rooms = [
#    {'id': 1, 'name' : 'Lets learn Python'},
#    {'id': 2, 'name' : 'Front End developers'},
#    {'id': 3, 'name' : 'Lets do Django'},
#    {'id': 4, 'name' : 'Lets do soft skills here'},
#    {'id': 5, 'name' : 'hello there'},
#]

def home(request):
    rooms = Rooms.objects.all()
    context = {'rooms' : rooms}
    return render (request,'Base/home.html', context)

def room(request,pk):
    room = Rooms.objects.get(id = pk)
    messages = Message.objects.filter(room = room)
    context = {'room': room,'messages':messages}
    
    return render (request,'Base/room.html',context)

def CreateRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('/')

    context = {'form': form}
    return render(request, 'Base/create_room.html', context )

def updateRoom(request,pk):
    room = Rooms.objects.get(id = pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance = room)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form':form}
    return render(request, 'Base/create_room.html', context)
def deleteRoom(request,pk):
    room = Rooms.objects.get(id = pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance = room)
        if form.is_valid():
            room.delete()
            return redirect('/')
    context = {'form':form,'room':room}
    return render(request, 'Base/delete_room.html', context)

def CreateMessage(request,pk):
    room = Rooms.objects.get(id = pk)
    form = MessagesForm()
    if request.method == 'POST':
        form = MessagesForm(request.POST)
        if form.is_valid():
            roomie = room
            body = form.cleaned_data['body']
            User = form.cleaned_data['User']
            valid_data = {'body':body,'room':roomie,'user':User}
            valid_form = MessagesForm(valid_data)
            if valid_form.is_valid():
                valid_form.save()
                return redirect('Base/room.html')
    context = {'form': MessagesForm,'room':room}
    return render(request, 'Base/create_message.html', context)



 
    
    

