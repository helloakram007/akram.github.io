from django.db import models

# Create your models here.
class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    email=models.EmailField(blank=True)
    subject=models.TextField(blank=True)
    content=models.TextField(blank=True)

    def __str__(self):
        return self.name +" "+ self.subject

class Blog(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.TextField(blank=True)
    author=models.CharField(blank=True,max_length=1000)
    tags=models.CharField(blank=True,max_length=1000)
    content=models.TextField(blank=True)
    image=models.ImageField(blank=True,upload_to="blog/images")
    time=models.DateTimeField(blank=True)
    readtime=models.CharField(blank=True,max_length=120)
    def __str__(self):
        return self.title + " " + self.tags

class Portfolio(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(blank=True,max_length=1000)
    tags=models.CharField(blank=True,max_length=1000)
    date=models.DateTimeField(blank=True)
    image=models.ImageField(blank=True,upload_to="project/images")
    def __str__(self):
        return self.name + " " + self.tags
class Files(models.Model):
    sno=models.AutoField(primary_key=True)
    file=models.FileField(blank=True,upload_to='files')
    name = models.CharField(blank=True,max_length=200)
    def __str__(self):
        return self.name


