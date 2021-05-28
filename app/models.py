from django.db import models

# Create your models here.

class Skills(models.Model):
    skills = models.CharField(max_length=50)
    skill_percent = models.CharField(max_length=50)
    about_me = models.TextField()
    

class Project(models.Model):
    proj_name = models.CharField(max_length=80)
    proj_description = models.TextField()
    proj_url = models.URLField(max_length=100)

    #def __


class ModelApi(models.Model):
    model_name = models.CharField(max_length=50)
    model_description = models.TextField()
    model_file = models.CharField(max_length=50)
