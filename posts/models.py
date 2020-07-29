from django.db import models

class Post(models.Model):
    post_title=models.CharField(max_length=200)
    post_text = models.CharField(max_length=10000)
    pub_date = models.DateTimeField('date published')
    image= models.ImageField(null=True,blank=True, upload_to="images/")

    def __str__(self):
        return self.post_title

# Create your models here.
