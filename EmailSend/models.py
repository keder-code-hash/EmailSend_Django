from django.db import models
import os  
from dotenv import load_dotenv
load_dotenv() 
from datetime import datetime
class EmailStore(models.Model):
    from_email=models.EmailField(blank=False,default=os.environ['EMAIL_HOST_USER'])
    username=models.CharField(max_length=100)
    send_to=models.EmailField(blank=False)
    send_at=models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.username