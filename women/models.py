from django.db import models
from  django.urls import reverse



class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return self.name
    

class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, null=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.title
    
    @permalink
    def get_absolute_url(self):
        return ("post-detail", [self.slug,])

    class Meta:
        verbose_name_plural = 'Women'