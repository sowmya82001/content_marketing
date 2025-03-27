from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Content(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class SocialMedia(models.Model):
    platform_name = models.CharField(max_length=100)  # e.g., Facebook, Twitter
    profile_url = models.URLField()  # Your social media profile link
    description = models.TextField(blank=True, null=True)  # Optional description
    icon = models.ImageField(upload_to='social_icons/', blank=True, null=True)  # Optional icon

    def __str__(self):
        return self.platform_name
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Auto add timestamp

    def __str__(self):
        return f"{self.name} - {self.email}"
