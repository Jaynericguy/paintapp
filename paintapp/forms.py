# creating a form 
# import the standard Django Forms
# from built-in library
from django.forms import ModelForm
from paintapp.models import Room

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'width', 'depth', 'height']