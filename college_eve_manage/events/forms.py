# events/forms.py

from django import forms
from .models import Participant  # Make sure this points to your Participant model

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'branch', 'semester', 'college_id' ,'status']
