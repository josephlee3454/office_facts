from django.db import models
from django.contrib.auth import get_user_model



# Create your models here.
class Office_facts(models.Model):
  author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  fact_name = models.TextField(max_length=20)
  fact_body = models.TextField(max_length=400)
  video_link = models.URLField(max_length = 200) 
  season = models.SmallIntegerField() 
  episode = models.SmallIntegerField()
  fact_post_date = models.DateTimeField(auto_created=True)
  fact_update_post = models.DateTimeField(auto_created=True)



  def __str__(self):
    self.author

