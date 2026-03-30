from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.first_name


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    students = models.ManyToManyField(Student, blank=True)

    def __str__(self):
        return self.name