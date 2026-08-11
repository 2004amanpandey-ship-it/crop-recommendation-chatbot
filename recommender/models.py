# recommender/models.py
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    # future: address, city, etc.

    def __str__(self):
        return self.user.get_full_name() or self.user.username

class Prediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='predictions')
    N = models.FloatField()
    P = models.FloatField()
    K = models.FloatField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    ph = models.FloatField()
    rainfall = models.FloatField()
    predicted_label = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} -> {self.predicted_label} ({self.created_at:%Y-%m-%d %H:%M})"



# naya code add kr rhi notice ka 
# 🔥 NOTICE MODEL (User module ke liye)
class Notice(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    link = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ['-date']   # latest notice upar aayega

    def __str__(self):
        return f"{self.title} ({self.date})"
    