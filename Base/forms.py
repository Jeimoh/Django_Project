from django.forms import ModelForm
from .models import Rooms,Message
class RoomForm(ModelForm):
    class Meta:
        model = Rooms
        fields = '__all__'

class MessagesForm(ModelForm):
    class Meta:
        model = Message
        fields = ['body','User']


