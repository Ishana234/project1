from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Participant

def participant_registration(request):
    if request.method == 'POST':
        # Get data from form submission
        name = request.POST.get('name')
        branch = request.POST.get('branch')
        semester = request.POST.get('semester')
        college_id = request.POST.get('college_id')
        status = request.POST.get('status', 'Registered')  # You can also get the status from the form if needed
        
        # Save the participant data to the backend
        participant = Participant(
             # Assuming the logged-in user is participating
            name=name,
            branch=branch,
            semester=semester,
            college_id=college_id,
            status=status,
            registered_at=timezone.now()  # Automatically set the registration time
        )
        participant.save()

        # Redire  # Make sure you have a success page or another view to redirect to

    # For GET requests, render the registration form
    return render(request, 'participant.html')
