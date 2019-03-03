from django.db import models

# Create your models here.
class Data(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    course = models.CharField(max_length=20)
    level = models.CharField(max_length=20)
'''
# ALTERNATIVE
class Data2(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    COURSE_CHOICES = (
        ('Py','Python'),
        ('Jv', 'JAVA'),
        ('Ad', 'ADROID'),
    )
    LEVEL_CHOICES = (
        ('B', 'Beginner'),
        ('S', 'Standard'),
        ('A', 'Advanced'),
    )
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    course = models.CharField(max_length=2, choices=COURSE_CHOICES)
    level = models.CharField(max_length=1, choices=LEVEL_CHOICES)
'''