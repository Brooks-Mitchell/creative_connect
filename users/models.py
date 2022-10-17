from django.db import models
from django.contrib.auth.models import User
# from PIL import Image


class User_Profile(models.Model):

    ROLE_OPTIONS = (
        ('animator', 'Animator'),
        ('scriptwriter', 'Scriptwriter'),
        ('audio engineer', 'Audio Engineer'),
        ('graphic design', 'Graphic Design'),
        ('videographer', 'Videographer'),
        ('video editor', 'Video Editor'),
        ('none', 'None')
    )

    COMMITMENT_LEVEL = (
        ('casual', 'Casual'),
        ('side project', 'Side Project'),
        ('1 priority', '#1 Priority')
    )


    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_bio = models.TextField(max_length=320, default="", blank=True)
    user_yoe = models.IntegerField(default=0)
    user_role = models.CharField(max_length=80, choices=ROLE_OPTIONS, default='none')
    user_commitment_level = models.CharField(max_length=80, choices=COMMITMENT_LEVEL, default='Casual')
    # image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    
    def __str__(self):
        return f'{self.user.username} Profile'
    

