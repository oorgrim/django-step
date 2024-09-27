from django.db import models

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio=models.TextField(null=True, blank=True)
    pic = models.ImageField(null=True, blank=True, upload_to="images/profile/")
    insta = models.textField(User, null=True, on_delete=models.Model)
def __str__(self):
    return str(self.user)
