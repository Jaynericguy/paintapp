# import Http Response from django
from django.shortcuts import render, redirect
from app.models import Room
from app.forms import RoomForm
# create a function
def viewHome(request):
    return render(request, "home.html")

# create a function
def viewRooms(request):
    # create a dictionary to pass
    # data to the template
    context ={
        "data":"Viewing all rooms",
        "list":Room.objects.all()
    }
    # return response with template and context
    return render(request, "roomsview.html", context)

def viewRoom(request, slug):
    room=Room.objects.filter(slug=slug)
    context ={
        "data":"Viewing a rooms dimensions and calculations",
        "list": room
    }
    if request.method == "POST":
        if request.POST['Delete']:
            room.delete()
            return render(request, "roomsview.html", context)
        elif request.POST['Edit']:
            pass
        else:
            pass
    else:
        # return response with template and context
        return render(request, "roomview.html", context)



# create a function
def addRooms(request):
    # create a dictionary to pass
    # data to the template
    context ={
        "data":"Add/Remove a room",
        "list":Room.objects.all(),
        "form":RoomForm()
    }
    # return response with template and context
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            obj = Room() #gets new object
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

    