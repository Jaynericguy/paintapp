# import Http Response from django
from django.shortcuts import render, redirect
from app.models import Room
from app.forms import RoomForm
# create a function
def viewHome(request):
    return render(request, "home.html")

def viewRooms(request):
    context ={
        "data":"Viewing all rooms",
        "list":Room.objects.all()
    }
    return render(request, "roomsview.html", context)

def viewRoom(request, slug):
    room=Room.objects.filter(slug=slug)
    context ={
        "data":"Viewing a rooms dimensions and calculations",
        "list": room
    }
    if request.method == 'POST':
        room.delete()
        return redirect('/viewRooms/')
    else:
        return render(request, "roomview.html", context)

def addRooms(request):
    context ={
        "data":"Add/Remove a room",
        "list":Room.objects.all(),
        "form":RoomForm()
    }
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            obj = Room()
            obj.name = form.cleaned_data['name']
            obj.width = form.cleaned_data['width']
            obj.depth = form.cleaned_data['depth']
            obj.height = form.cleaned_data['height']
            obj.save()
            return redirect('/viewRooms/')
        else:
            pass
    else:
        return render(request, "roomsadd.html", context)

    