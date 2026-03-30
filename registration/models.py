from django.db import models

class Project(models.Model):
    topic = models.CharField(max_length=200)
    languages_used = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)

    def __str__(self):
        return self.topic


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    project = models.OneToOneField(
        Project,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.first_name