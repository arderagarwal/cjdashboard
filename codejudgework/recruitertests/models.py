from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from recruiter.models import Recruiter , UserLevel
User = get_user_model()

class Test(models.Model):
    recruiter =  models.ForeignKey(User, null = True , on_delete=models.CASCADE,related_name='tests')
    testname = models.CharField(max_length=200)
    create_date= models.DateTimeField(default=timezone.now())
    userlevel = models.ForeignKey(UserLevel, null=True, on_delete=models.CASCADE,related_name='userlevel' )
    def __str__(self):
        return self.testname
