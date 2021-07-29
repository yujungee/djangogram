from django.db import models
from djangogram.users import modls as user_model
# Create your models here.

class TimeStamedModel(models.Model):
    create_at = models.DataTimeField(auto_now_add=True)
    updated_at = models.DataTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Post(TimeStamedModel):
    author = models.ForeignKey(
                user_model.User,
                null=True,
                on_delete=models.CASCADE,
                related_name= 'post_author')
    image = models.ImageField(blank=True)
    cpation = models.TextField(blank=True)
    image_likes = models.ManyToManyField(user_model.User, related_name='post_image_likes')

class Comment(TimeStamedModel):
    author = models.ForeignKey(
        user_model.User,
        null=True,
        on_delete=models.CASCADE,
        related_name='post_author')
    posts = models.ForeignKey(
        Post,
        null=True,
        on_delete=models.CASCADE,
        related_name='comment_post')
    contents = models.TextField(blank=True)
