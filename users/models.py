from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    mobile_phone = models.CharField(max_length=15, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=40, null=True, blank=True)
    facebook_account = models.URLField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to = 'images/', default='')
    project_reports = models.ManyToManyField('Project',through='Report', related_name='reports', blank=True)
    project_rates = models.ManyToManyField('Project', through='Rate', related_name='rates', blank=True)
    project_donations = models.ManyToManyField('Project', through='Donation',related_name='donations', blank=True)
    comment_reports = models.ManyToManyField('Comment', related_name='reports', blank=True)
    email = models.EmailField(('email address'), unique=True)
    signup_confirmation = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
class Category(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class Project(models.Model) :
    title = models.CharField(max_length=70, null=True)
    details = models.CharField(max_length=150, null=True, blank=True)
    total_target = models.FloatField(null=True, blank=True)
    start_date = models.DateField(null= True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    category = models.ForeignKey('Category', null=True, on_delete=models.CASCADE)
    owner = models.ForeignKey('User', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.CharField(max_length=200, null=True)
    user = models.ForeignKey('User', null=True, on_delete=models.CASCADE)
    project = models.ForeignKey('Project', null=True, on_delete=models.CASCADE)

class Rate(models.Model):
    user= models.ForeignKey('User', null=True, on_delete=models.CASCADE)
    project = models.ForeignKey('Project', null=True, on_delete=models.CASCADE)
    rate = models.FloatField(null=True)

class Donation(models.Model):
    user= models.ForeignKey('User', null=True, on_delete=models.CASCADE)
    project = models.ForeignKey('Project', null=True, on_delete=models.CASCADE)
    amount = models.FloatField(null=True)

class Report(models.Model):
    user= models.ForeignKey('User', null=True, on_delete=models.CASCADE)
    project = models.ForeignKey('Project', null=True, on_delete=models.CASCADE)
    report_content = models.FloatField(null=True)

class Project_pictures(models.Model):
    project = models.ForeignKey('Project', null=True, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to = 'images/', default='')

class Project_tags(models.Model):
    project = models.ForeignKey('Project', null=True, on_delete=models.CASCADE)
    tag = models.CharField(max_length=50)

