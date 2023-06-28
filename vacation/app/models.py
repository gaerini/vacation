from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Timetable(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    Date = models.DateField(auto_now_add=True)

    
class Timeblock(models.Model):
    timetable_id = models.ForeignKey(Timetable, on_delete=models.CASCADE, related_name='timetable_id')
    starttime = models.IntegerField()
    endtime = models.IntegerField()
    detail = models.CharField(max_length=50)

class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    count = models.IntegerField()



