from django.db import models

# Create your models here.

disabilties = (("Attention Deficit Hyperactivity Disorder (ADHD)", "Attention Deficit Hyperactivity Disorder (ADHD) "),
("Learning Disabilities","Learning Disabilities "), 
("Mobility Disabilities", "Mobility Disabilities "), 
("Medical Disabilities", "Medical Disabilities "), 
("Psychiatric Disabilities", "Psychiatric Disabilities "), 
("Traumatic Brain Injury (TBI) and Post-Traumatic Stress Disorder (PTSD)", "Traumatic Brain Injury (TBI) and Post-Traumatic Stress Disorder (PTSD) "), 
("Visual Impairments", "Visual Impairments "),
("Deaf and Hard of Hearing","Deaf and Hard of Hearing "),
("Autism Spectrum Disorders","Autism Spectrum Disorders "),
("Other", "Other "))

class User(models.Model):

    name = models.CharField("Name", max_length=240)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=60)
    disability = models.CharField(max_length=100, choices=disabilties, default='Other')
    other = models.CharField(max_length=50, null=True)
    bio = models.TextField(null=True)
    host = models.BooleanField(null=True, default=False)
    family_number = models.IntegerField(default=1, null=True)

    def __str__(self):
        return self.name


class Host(models.Model):

    name = models.CharField("Name", max_length=240)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=60)
    disability = models.CharField(max_length=100, choices=disabilties, default='Other')
    other = models.CharField(max_length=5, null=True)
    bio = models.TextField(null=True)
    host = models.BooleanField(null=True,default=True)
    available = models.BooleanField(null=True, default=True)
    family_number = models.IntegerField(default=1, null=True)


    def __str__(self):
        return self.name