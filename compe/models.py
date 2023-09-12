from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='uploads/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Problem(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Categorys')

    def __str__(self):
        return self.title


class Choice(models.Model):
    title = models.CharField(max_length=100)
    completed = models.IntegerField(default=120)
    unfinished = models.IntegerField(default=0)
    zone = models.IntegerField(default=60)
    total = models.IntegerField(default=0)

    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, related_name='Problems')

    def __str__(self):
        return self.title

