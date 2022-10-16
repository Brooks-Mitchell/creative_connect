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

