from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.forms import ModelForm
from django.contrib.postgres.fields import ArrayField, IntegerRangeField

# starting to get model heavy in the default models file. Moving to break things up for the app for
# better management purposes


class Update(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300, unique=True,)
    content = models.TextField()
    author = models.ForeignKey("auth.CustomUser", on_delete=models.CASCADE, related_name='fp_updates')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
