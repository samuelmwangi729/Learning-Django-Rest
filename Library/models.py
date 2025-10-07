from django.db import models

# Create your models here.
class AuthorTitles:
    MR = "mr"
    MRS="mrs"

    choices = (

        (MR,"mr"),
        (MRS,"mrs")
    )
class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name 
    
class Author(models.Model):
    title = models.CharField(max_length=5,choices=AuthorTitles.choices)
    name = models.CharField(max_length=200)
    bio = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.title} {self.name}"


class Books(models.Model):
    title = models.CharField(max_length=20,blank=False)
    author = models.ForeignKey(Author,on_delete=models.DO_NOTHING,related_name="books",null=True,blank=True)
    genre = models.CharField(max_length=30)
    description = models.TextField()
    ISBN = models.IntegerField(unique=True)

    def __str__(self):
        return self.title