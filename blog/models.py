from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    title = models.CharField( max_length=150, )
    description = models.TextField(max_length=100000)
    # author = models.OneToOneField(User, on_delete=models.CASCADE)

class contact(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField(max_length=70)
    message=models.CharField(max_length=100)

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    picture = models.ImageField(default='default.jpg',upload_to='profile_pics/',null=True, blank = True, )

    def __str__(self):
        return f'{self.user.username} profile'