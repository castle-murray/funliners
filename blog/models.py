from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    use = models.CharField(max_length=500)
    problem = models.CharField(max_length=500)
    context = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


# class PostComment(models.Model):
#     content = models.TextField()
#     c_author = models.ForeignKey(User, on_delete=models.CASCADE)
# #    c_author = models.ForeignKey(
# #        User, on_delete=models.CASCADE)
#     date_posted = models.DateTimeField(default=timezone.now)
#     original_post = models.ForeignKey(
#         'Post', on_delete=models.CASCADE)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    post = models.ForeignKey(
        'Post', related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
