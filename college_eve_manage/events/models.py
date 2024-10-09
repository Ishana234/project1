from django.db import models




    

class Participant(models.Model):
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    semester = models.IntegerField()
    college_id = models.CharField(max_length=100)
    registered_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20, 
        choices=[
            ('Registered', 'Registered'), 
            ('Checked-in', 'Checked-in'), 
            ('Cancelled', 'Cancelled')
        ]
    )

    def __str__(self):
        return self.name




