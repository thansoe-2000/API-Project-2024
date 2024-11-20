from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.


class Group(models.Model):
    name = models.CharField(max_length=200)
    leader = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True)
    
    def __str__(self):
        return self.name
    
    
class Member(models.Model):
    GENDER_CHOICES = [
        ('Male','Male'),
        ('Female','Female'),
    ]
    # BLOOD_CHOICES = [
    #     ('b', 'B'),
    #     ('a', 'A'),
    #     ('o', 'O'),
    # ]
    LANGUAGE_CHOICES = [
        ('A+', 'A+'),
        ('C#', 'c#'),
        ('Dart', 'Dart'),
        ('Fluter', 'Flutter'),
        ('NodeJs', 'Nodejs'),
        ('Networking', 'Networking'),
        ('Python', 'Python'),
        
    ]
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default=None)
    languages = MultiSelectField(choices=LANGUAGE_CHOICES, blank=True, null=True)
    groups = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True)
    birth_date = models.DateField()
    bio = models.TextField(blank=True)
    
    def __str__(self):
        return self.name



    