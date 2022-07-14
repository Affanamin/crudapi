from django.db import models
from account.models import User

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    #task_id = models.AutoField(primary_key=True)  
    title = models.TextField(max_length=200,null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    # class Meta:
    #     db_table = 'Notes'

