from django.db import models


class Tweet(models.Model):
    id = models.CharField( max_length = 80, primary_key = True )
    created_at = models.CharField( max_length = 1000 )
    text = models.CharField( max_length = 5000 )
    user_name = models.CharField( max_length = 500 )
    user_screenname = models.CharField( max_length = 500 )
    location = models.CharField( max_length = 500 )
    description = models.CharField( max_length = 5000 )
    url = models.CharField( max_length = 2048 )
