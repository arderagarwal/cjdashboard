from django.db import models
from django.contrib.auth.models import User
class Recruiter(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    PhoneNo = models.BigIntegerField()
    def __str__(self):
        return self.user.username

class UserLevel(models.Model):
    Name = models.CharField(max_length=200)
    Level = models.CharField(max_length=200)
    def __str__(self):
        return self.Name

class Track(models.Model):
        name = models.CharField(max_length=200)
        def __str__(self):
            return self.name

class Contest(models.Model):
    name = models.CharField(max_length=200)
    track_id = models.ForeignKey(Track, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class TechnologyVertical(models.Model):
        name = models.CharField(max_length=200)

        class Meta:
            ordering = ('name',)

        def __str__(self):
            return self.name

class Assignment(models.Model):
        name = models.CharField(max_length=200)
        description = models.TextField()
        tags = models.TextField()
        track_id = models.ForeignKey(Track , on_delete=models.CASCADE)
        vertical_id = models.ForeignKey(TechnologyVertical, on_delete=models.CASCADE)
        def __str__(self):
            return self.name

class TestAssign(models.Model):
        contest_id = models.ForeignKey(Contest, on_delete=models.CASCADE)
        assignment_id= models.ForeignKey(Assignment, on_delete=models.CASCADE)
        language = models.CharField(max_length=200)
        user_id = models.ForeignKey(UserLevel, on_delete=models.CASCADE)
        user_email = models.EmailField()
        test_link = models.CharField(max_length=200)
        status = models.BooleanField(default=False)
        language_allowed = models.CharField(max_length=200)
        def __str__(self):
            return self.assignment_id

class DetailedReport(models.Model):
        sonar_project_id = models.CharField(max_length=256)
        s3_bucket_path = models.CharField(max_length = 256)
        language = models.CharField(max_length=200)
        test_id = models.ForeignKey(TestAssign, on_delete=models.CASCADE)
        #result id is the default primary key
        def __str__(self):
            return self.result_id
