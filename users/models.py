from django.db import models
from django.contrib.auth.models import AbstractUser
from  django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.signals import pre_save
from django.dispatch import receiver
from datetime import datetime

class CustomUserManager(BaseUserManager):
    def create_user(self ,email, password=None):
        if not email:
            raise ValueError("You must enter email to create new user")

        user = self.model(
            email=self.normalize_email(email),
            password=password
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, password):
        user = self.create_user(
            email=email,
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user
class User(AbstractUser):
    username=models.CharField(max_length=40, null=True)
    mobile_phone = models.CharField(max_length=15,validators=[RegexValidator('^0(10|11|12|15)\d{8}$',message="please enter egyptian mobile phone: like= 01012345678")])
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
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

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
    is_featured= models.BooleanField(null=True,blank=True)
    featuring_date= models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.title

#a trigger to auto update featuring date when the project is featured
@receiver(pre_save, sender=Project)
def update_project_on_save(sender, instance, **kwargs):
    if instance.id:
        old_project = Project.objects.get(pk=instance.id)
        if instance.is_featured and not old_project.is_featured:
            instance.featuring_date= datetime.now()

class Comment(models.Model):
    content = models.CharField(max_length=200, null=True)
    user = models.ForeignKey('User', null=True, on_delete=models.CASCADE)
    project = models.ForeignKey('Project', null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.content

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

