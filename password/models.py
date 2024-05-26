from django.db import models
from django.contrib.auth.models import User

class Password(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1,related_name='passwords')
    pub_date = models.DateTimeField("Date published", auto_now_add=True)
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    choice_text = models.CharField(max_length=100,blank=True, null=True)

    def __str__(self):
        return self.password
