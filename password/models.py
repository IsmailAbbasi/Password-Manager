from django.db import models

class Password(models.Model):
    pub_date = models.DateTimeField("Date published", auto_now_add=True)
    password = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    choice_text = models.CharField(max_length=100)

    def __str__(self):
        return self.password
