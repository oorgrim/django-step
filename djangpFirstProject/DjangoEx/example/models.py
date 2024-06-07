from django.db import models

# Create your models here.
class Class(models.Model):
    count_of_stud = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'count of stud = {self.count_of_stud}'