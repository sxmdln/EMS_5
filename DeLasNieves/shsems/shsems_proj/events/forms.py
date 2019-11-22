from django.forms import ModelForm

from .models import Event



class EventCreateForm(ModelForm):
	class Meta:
		model = Event
		fields = ('name', 'description', 'poster', 'max_slots', 'date_from', 'date_to', 'time_from', 'time_to')
