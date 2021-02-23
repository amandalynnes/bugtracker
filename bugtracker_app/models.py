from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser


# Create your models here.
# Your Ticket model should have the following fields:

# Title: str
# Time / Date filed: datetime
# Description: str
# User who filed ticket: FK (Foreign Key)
# Status of ticket: str
# Possible statuses
# New
# In Progress
# Done
# Invalid
# hint: https://docs.djangoproject.com/en/3.0/ref/models/fields/#choices
# User assigned to ticket: FK
# User who completed the ticket: FK

class CustomUser(AbstractUser):
    email = models.EmailField()
    password = models.CharField(max_length=40)

    def __str__(self):
        return self.username

class TicketItem(models.Model):
    new = 'NW'
    done = 'DN'
    in_prograss = 'IP'
    invalid = 'IN'
    ticket_status_choices = [
        (new,'New'),
        (done,'Done'),
        (in_prograss, 'In_Prograss'),
        (invalid,'Invalid'),
    ]
    title = models.CharField(max_length=40)
    dt_filed = models.DateTimeField(default=now)
    description = models.TextField(max_length=150)
    filed_by = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)
    ticket_status = models.CharField(
        max_length=2,
        choices=ticket_status_choices,
        default=new,
    )
    # assigned_to = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)
    # completed_by = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
