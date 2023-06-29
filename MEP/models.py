from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Question(models.Model):
    statement = models.TextField()
    choice_a = models.CharField(max_length=255, null=True)
    choice_b = models.CharField(max_length=255, null=True)
    choice_c = models.CharField(max_length=255, null=True)
    choice_d = models.CharField(max_length=255, null=True)
    correct = models.CharField(max_length=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.statement
