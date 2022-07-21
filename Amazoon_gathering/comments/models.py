from django.db import models

# Create your models here.
class Link(models.Model):
    link =models.CharField(max_length=300)
    state=models.IntegerField(null=True,blank=True)
    def __str__(self):
        return self.link
class Comment(models.Model):
    comment = models.CharField(max_length=1000)
    address = models.ForeignKey(Link,on_delete=models.CASCADE)
    def __str__(self):
        return self.comment