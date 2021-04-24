from django.forms import ModelForm

from .models import Polls

class CreatePollForm(ModelForm):
    class Meta:
        model = Polls
        fields = ['question', 'name', 'option_one', 'option_two', 'option_three']
