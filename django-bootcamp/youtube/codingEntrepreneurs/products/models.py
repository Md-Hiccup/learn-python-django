from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

# Create your models here.
class Product(models.Model):
    # id = models.AutoField()
    ## To not to delete the user
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    ## To delete the user
    # user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField(null=True, blank=True)
    price = models.IntegerField(default=0)
