from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models
from django.dispatch import receiver


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=150, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Follow(models.Model):
    follow_from = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    follow_to = models.ForeignKey(User, related_name='follower', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f'{self.follow_from} follows {self.follow_to}'


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=500)
    slug = models.SlugField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} - {self.body[:30]}'

    class Meta:
        ordering = ('-created_at',)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userComment')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='postComment')
    body = models.TextField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} commented for {self.post} : {self.body[:30]}'

    class Meta:
        ordering = ('-created_at',)
