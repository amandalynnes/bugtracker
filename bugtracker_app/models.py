from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now
from django.conf import settings

# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField()
    password = models.CharField(max_length=40)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    

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
    description = models.TextField(max_length=350)
    filed_by = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE, related_name="filed_by")
    ticket_status = models.CharField(
        max_length=2,
        choices=ticket_status_choices,
        default=new,
    )
    assigned_to = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE, related_name="assigned_to")
    completed_by = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE, related_name="completed_by")

    def __str__(self):
        return self.title
