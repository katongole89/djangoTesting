from django.db import models

# Create your models here.
#from accounts.models import customUser
from django.utils.timezone import now

# Create your models here.
class verificationDetails(models.Model):
    phoneNumber= models.CharField(max_length= 200, blank=False)
    otp= models.CharField(max_length=50, blank=False)
    validated = models.BooleanField(default= False)
    dateCreated = models.DateTimeField(default=now)

    def __str__(self):
        return self.phoneNumber + '--'+ self.otp + '--'+ str(self.validated) + '--' + str(self.dateCreated)
