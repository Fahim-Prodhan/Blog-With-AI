from django.db import models
from .utils import summarize_text

class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    summary = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.summary and self.content:
            self.summary = summarize_text(self.content)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
