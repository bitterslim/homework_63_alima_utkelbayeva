from django.contrib.auth import get_user_model
from django.db import models

class Post(models.Model):
    user = models.ForeignKey(verbose_name='User', to=get_user_model(), related_name='posts', null=True, blank=True,on_delete=models.CASCADE)
    description = models.CharField(verbose_name='Description', null=False, blank=False, max_length=200)
    image = models.ImageField(verbose_name='Photo', null=False, blank=False, upload_to='post_image')
    likes = models.IntegerField(verbose_name='Likes', default=0)
    created_at = models.DateTimeField(verbose_name='Created at', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='Changed at', auto_now=True)


class Comment(models.Model):
    user = models.ForeignKey(verbose_name='User', to=get_user_model(), related_name='comments', null=True, blank=True, on_delete=models.CASCADE)
    post = models.ForeignKey(verbose_name='Posts', to='posts.Post', related_name='comments', null=True, blank=True, on_delete=models.CASCADE)
    comment_text = models.CharField(verbose_name='Comment', null=False, blank=False, max_length=200)

class Like(models.Model):
    class Like(models.Model):
        user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
        post = models.ForeignKey('Post', on_delete=models.CASCADE)

        class Meta:
            unique_together = (('user', 'publication'),)


