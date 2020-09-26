from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class msg(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(max_length=50000)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.username)
    objects = models.Manager()
    class meta:
        managed = True
        db_table = 'msg'
