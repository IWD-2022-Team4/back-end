from django.db import models

# Create your models here.

disabilties = (
("ADHD", "Attention Deficit Hyperactivity Disorder (ADHD)"),
("LD","Learning Disabilities"), 
("MD", "Mobility Disabilities"), 
("MedD", "Medical Disabilities"), 
("PsyD", "Psychiatric Disabilities"), 
("PTSD", "Traumatic Brain Injury (TBI) and Post-Traumatic Stress Disorder (PTSD)"), 
("VD", "Visual Impairments"),
("DF","Deaf and Hard of Hearing"),
("ASD","Autism Spectrum Disorders"),
("O", "Other")
)

class User(models.Model):
    name = models.CharField("Name", max_length=240)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=60)
    disability = models.CharField(max_length=6, choices=disabilties, default='O')
    other = models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.name


class Host(models.Model):
    name = models.CharField("Name", max_length=240)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=60)
    disability = models.CharField(max_length=6, choices=disabilties, default='O')
    other = models.CharField(max_length=5, null=True)

    def __str__(self):
        return self.name