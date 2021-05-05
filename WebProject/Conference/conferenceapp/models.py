from django.db import models

# Create your models here.
class Registrationform (models.Model):
    
    name           = models.CharField(max_length=100, blank=True)
    email          = models.CharField(max_length = 100, blank = True)
    district       = models.CharField(max_length = 100, blank = True)
    profession     = models.CharField(max_length = 100, blank = True)
    # Phone_number   = models.CharField(max_length = 100, blank = True)
    # residence = models.CharField(max_length = 100, blank = True, null=True)
    
    

    def __str__ (self):
        return self.name