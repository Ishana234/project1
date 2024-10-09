from django.urls import path
from .views import  participant_registration  # Ensure both views are imported

urlpatterns = [
 # Map the home view to the root URL of the app
    path('register/', participant_registration, name='participant_registration'),
]

