from django.db import models

# Create your models here.
class Tasks(models.Model) :
  title=models.CharField(max_length=100)
  descritpion=models.CharField(max_length=300)
  status=models.CharField(max_length=20,default='pending',choices=[('pending','pending'),('in_progress','in_progress'),('Completed','Completed')])
  priority=models.CharField(max_length=1,default=1,choices=[(1,'Low'),(2,'Medium'),(3,'Completed')])
  created_at=models.DateTimeField(auto_now_add=True)
  update_at=models.DateTimeField(auto_now_add=True)

  